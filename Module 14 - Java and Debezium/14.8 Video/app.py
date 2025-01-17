import mysql.connector
from mysql.connector import Error
from pymysqlreplication import BinLogStreamReader


MYSQL_SETTINGS = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "Egyptiancobra27!",
    "database": "education",
}

def call_mysql():
    # server_id is your slave identifier, it should be unique.
    # set blocking to True if you want to block and wait
    # for the next event at the end of the stream
    stream = BinLogStreamReader(connection_settings=MYSQL_SETTINGS,
                                server_id=3,
                                blocking=True)

    for binlogevent in stream:
        binlogevent.dump()

    stream.close()

call_mysql()