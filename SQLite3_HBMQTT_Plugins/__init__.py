from hbmqtt.plugins.authentication import BaseAuthPlugin
from hbmqtt.plugins.topic_checking import BaseTopicPlugin
import asyncio
import sqlite3

class SQLiteAuthPlugin(BaseAuthPlugin):
	def __init__(self, context):
		super().__init__(context)
		try:
			self.database = self.context.config["sqlite-database"]
		except KeyError:
			self.database = False
			self.context.logger.warning(
            	"'sqlite-database' key not found in configuration")

	@asyncio.coroutine
	def authenticate(self, *args, **kwargs):
		session = kwargs.get("session", None)
		username = session.username
		password = session.password
		if username and self.database:
			with sqlite3.connect(self.database) as conn:
				cursor = conn.cursor()
				cursor.execute(f"""
				SELECT password FROM MQTT_authmqtt WHERE username = '{username}'
				""")# EDIT WITH YOUR QUERY TO GET THE PASSWORD
				if password == cursor.fetchone()[0]:
					return True
		return False


class SQLiteTopicAccessControlPlugin(BaseTopicPlugin):
	def __init__(self, context):
		super().__init__(context)
		try:
			self.database = self.context.config["sqlite-database"]
		except KeyError:
			self.database = False
			self.context.logger.warning(
            	"'sqlite-database' key not found in configuration")

	@staticmethod
	def topic_ac(topic_requested, topic_allowed):
		req_split = topic_requested.split('/')
		allowed_split = topic_allowed.split('/')
		ret = True
		for i in range(max(len(req_split), len(allowed_split))):
			try:
			    a_aux = req_split[i]
			    b_aux = allowed_split[i]
			except IndexError:
			    ret = False
			    break
			if b_aux == '#':
			    break
			elif (b_aux == '+') or (b_aux == a_aux):
			    continue
			else:
			    ret = False
			    break
		return ret

	@asyncio.coroutine
	def topic_filtering(self, *args, **kwargs):
		filter_result = super().topic_filtering(*args, **kwargs)
		if filter_result and self.topic_config['enabled']:
			session = kwargs.get('session', None)
			req_topic = kwargs.get('topic', None)
			username = session.username
			if req_topic and username and self.database:
				with sqlite3.connect(self.database) as conn:
					cursor = conn.cursor()
					cursor.execute(f"""
					SELECT id FROM MQTT_authmqtt WHERE username = '{username}'
					""")# EDIT WITH YOUR QUERY TO GET THE USER ID
					id = cursor.fetchone()[0]
					cursor.execute(f"""
					SELECT topic FROM MQTT_topic WHERE mqtt_user_id = '{id}'
					""")# EDIT WITH YOUR QUERY TO GET THE USER'S ALLOWED TOPICS
					
					"""
					SELECT MQTT_topic.topic 
					FROM MQTT_authmqtt, MQTT_topic 
					WHERE MQTT_authmqtt.username = '{username}'
					AND MQTT_topic.mqtt_user_id = MQTT_authmqtt.id
					"""
					for row in cursor.fetchall():
						allowed_topic = row[0]
						if self.topic_ac(req_topic, allowed_topic):
							return True
			return False
