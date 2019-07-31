# SQLite3_HBMQTT_Plugins
# download
```
git clone https://github.com/jacoposartini/SQLite3_HBMQTT_Plugins.git
```
# setup
it is important that before installing you modify the queries in the file ```__init__.py``` so that the broker queries the correct tables and the correct columns!
```
	cursor.execute(f"""
	SELECT password FROM MQTT_authmqtt WHERE username = '{username}'
	""")# EDIT WITH YOUR QUERY TO GET THE PASSWORD
				
	cursor.execute(f"""
	SELECT id FROM MQTT_authmqtt WHERE username = '{username}'
	""")# EDIT WITH YOUR QUERY TO GET THE USER ID

	cursor.execute(f"""
	SELECT topic FROM MQTT_topic WHERE mqtt_user_id = '{id}'
	""")# EDIT WITH YOUR QUERY TO GET THE USER'S ALLOWED TOPICS
```

# install
To install, simply run the command:
```
	python3 setup.py install
```
# run
To use the plugin use the following configuration:
```
	'sqlite-database': 'YOUR SQLITE3 DATABASE LOCATION',
	'auth': {
		'allow-anonymous': False,
		'plugins': [
			'auth_anonymous', 'auth_sqlite'
		]
	},
	'topic-check': {
		'enabled': True,
		'plugins': [
			'topic_sqlite'
		]
	}
```
To execute an example script, run the command:
```
	python3 example_broker.py
```
# in case of bugs please contact me.
