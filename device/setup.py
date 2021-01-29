#coding:utf-8
from uuid import getnode as get_mac
from lcddisplay import jlcd
import random
import math
import sqlite3
import subprocess
import connect_database as db
import pymysql

class FirstSetup:
    def __init__(self):
        #MACアドレスをランダムなシード値で再作成
        random.seed(get_mac())
        self.mac = math.floor(random.random()*1000000)
        pymysql.install_as_MySQLdb()
        self.lcd = jlcd.Jlcd(2,0x27,True)

    def get_device_id(self):
        return self.mac

    def id_display(self):
        #LCDに表示
        self.lcd.message("Please input ID", 1)
        self.lcd.message(str(self.mac),2)

    def create_database(self):
        DATABASE = 'my_air_data.db'
        conn = sqlite3.connect(DATABASE)

        device_sql = '''
                CREATE TABLE IF NOT EXISTS device(
                device_id VARCHAR NOT NULL,
                device_name VARCHAR,
                PRIMARY KEY (device_id))
            '''
        sensor_sql = '''
                CREATE TABLE IF NOT EXISTS sensor(
                sensor_id INTEGER NOT NULL,
                sensor_name VARCHAR,
                sensor_type VARCHAR,
                sensor_unit VARCHAR,
                sensor_min REAL,
                sensor_max REAL,
                PRIMARY KEY (sensor_id))
            '''
        device_data_sql = '''
                CREATE TABLE IF NOT EXISTS device_data(
                device_id VARCHAR NOT NULL,
                sensor_id INTEGER NOT NULL,
                sensor_data INTEGER,
                time INTEGER NOT NULL,
                PRIMARY KEY (device_id, sensor_id, time),
                FOREIGN KEY (device_id) REFERENCES device(device_id),
                FOREIGN KEY (sensor_id) REFERENCES sensor(sensor_id))
            '''
        conn.execute(device_sql)
        conn.execute(sensor_sql)
        conn.execute(device_data_sql)

        #device表にアドレスを挿入
        conn.execute(f'INSERT INTO device(device_id, device_name) values("{self.mac}", null)')

        #sensor表にデータを挿入
        conn.execute('''INSERT INTO sensor(
            sensor_id, sensor_name, sensor_type, sensor_unit, sensor_min, sensor_max)
            values(0, "DHT22", "Temperature", "°C", -50, 120)'''
            )

        conn.execute('''INSERT INTO sensor(
            sensor_id, sensor_name, sensor_type, sensor_unit, sensor_min, sensor_max)
            values(1, "DHT22", "Humid", "%", 0, 100)'''
            )
        conn.execute('''INSERT INTO sensor(
            sensor_id, sensor_name, sensor_type, sensor_unit, sensor_min, sensor_max)
            values(2, "GYSFDMAXB", "Latitude", "", 0, 360)'''
            )

        conn.execute('''INSERT INTO sensor(
            sensor_id, sensor_name, sensor_type, sensor_unit, sensor_min, sensor_max)
            values(3, "GYSFDMAXB", "Longitude", "", 0, 360)'''
            )

        conn.execute('''INSERT INTO sensor(
            sensor_id, sensor_name, sensor_type, sensor_unit, sensor_min, sensor_max)
            values(4, "MH-Z19B", "CO2", "ppm", 0, 9999)'''
            )

        conn.execute('''INSERT INTO sensor(
            sensor_id, sensor_name, sensor_type, sensor_unit, sensor_min, sensor_max)
            values(5, "GP2Y1026AU0F", "Dust", "mg/m³", 0, 9999)'''
            )

        conn.execute('''INSERT INTO sensor(
            sensor_id, sensor_name, sensor_type, sensor_unit, sensor_min, sensor_max)
            values(6, "MQ-135", "Gas", "", 0, 1000)'''
            )

        conn.commit()
        conn.close()
        
    def post_device_id(self):
        connection = db.connect_air_database()
        device_id = self.mac
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO device VALUES(%s,%s)", (device_id, 'aaa'))
            connection.commit()
        except pymysql.Error as e:
            print(e)
        finally:
            connection.close()

    def check_device_id(self):
        connection = db.connect_air_database()
        device_id = self.mac
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT device_id FROM device WHERE device_id = %s", (self.mac,))
            device_id = cursor.rowcount
        finally:
            connection.close()

        if device_id == self.mac:

            return True

        return False

class SetUp:
    def __init__(self):
        #MACアドレスをランダムなシード値で再作成
        random.seed(get_mac())
        self.mac = math.floor(random.random()*1000000)
        pymysql.install_as_MySQLdb()

    def check_device_id(self):
        connection = db.connect_air_database()
        device_id = 0
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT device_id FROM device WHERE device_id = %s", (self.mac,))
            device_id = cursor.fetchone()
        finally:
            connection.close()

        if device_id[0] == str(self.mac):

            return True

        return False
