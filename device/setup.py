#coding:utf-8
from uuid import getnode as get_mac
from lcddisplay import jlcd
import random
import math
import sqlite3
import subprocess

class first_setup:
    def __init__(self):
        #MACアドレスをランダムなシード値で再作成
        random.seed(get_mac())
        mac = math.floor(random.random()*1000000)

    def id_display(self):
        #LCDに表示
        lcd = jlcd.Jlcd(2,0x27,True)
        lcd.message(str(self.mac),1)

    def create_database(self):
        DATABASE = 'my_air_data.db'
        conn = sqlite3.connect(DATABASE)
        device_sql = '''
                CREATE TABLE IF NOT EXISTS device(
                device_id VARCHAR NOT NULL,
                device_name VARCHAR NOT NULL,
                PRIMARY KEY (device_id))
            '''
        sensor_sql = '''
                CREATE TABLE IF NOT EXISTS senosr(
                sensor_id INTEGER NOT NULL,
                sensor_name VARCHAR,
                sensor_type VARCHAR,
                sensor_unit VARCHAR,
                sensor_min INTEGER,
                sensor_max INTEGER,
                PRIMARY KEY (sensor_id))
            '''
        device_data_sql = '''
                CREATE TABLE IF NOT EXISTS device_data(
                device_id VARCHAR NOT NULL,
                sensor_id INTEGER NOT NULL,
                time INTEGER NOT NULL,
                sensor_data INTEGER,
                PRIMARY KEY (device_id, sensor_id, time),
                FOREIGN KEY (device_id) REFERENCES device(device_id),
                FOREIGN KEY (sensor_id) REFERENCES sensor(sensor_id))
            '''
        conn.execute(device_sql)
        conn.execute(sensor_sql)
        conn.execute(device_data_sql)

        conn.commit()
        conn.close()
