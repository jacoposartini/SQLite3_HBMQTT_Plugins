from setuptools import find_packages, setup
setup(
    name="sqlite3-hbmqtt",
    version="1.0.0",
    description="HBMQTT plugins for SQLite3!",
    author="Jacopo Sartini",
    author_email="jacopo.sartini.developer@gmail.com",
    url="https://github.com/jacoposartini/SQLite3_HBMQTT_Plugins",
    license="MIT",
    packages=find_packages(),
    install_requires=[
		"hbmqtt",
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        "hbmqtt.broker.plugins": [
            "auth_sqlite = SQLite3_HBMQTT_Plugins:SQLiteAuthPlugin",
            "topic_sqlite = SQLite3_HBMQTT_Plugins:SQLiteTopicAccessControlPlugin",
        ]
    }
)
