# SQLite3_HBMQTT_Plugins
# setup
it is important that before installing you modify the queries in the file ```__init__.py``` so that the broker queries the correct tables and the correct columns!
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
# In case of bugs please contact me.
