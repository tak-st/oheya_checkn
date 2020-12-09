#coding:utf-8
from uuid import getnode as get_mac
from lcddisplay import jlcd
import random
import math
import sqlite3
import subprocess
import connect_database as db
import MySQLdb
import pymysql

class FirstSetup:
    def __init__(self):
        #MACアドレスをランダムなシード値で再作成
        random.seed(get_mac())
        self.mac = math.floor(random.random()*1000000)
        pymysql.install_as_MySQLdb()
        self.lcd = jlcd.Jlcd(2,0x27,True)

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
                time INTEGER NOT NULL,
                sensor_data INTEGER,
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
            values(1, "DHT22", "Temperature", "°C", -50, 120)'''
            )

        conn.execute('''INSERT INTO sensor(
            sensor_id, sensor_name, sensor_type, sensor_unit, sensor_min, sensor_max)
            values(2, "DHT22", "Humid", "%", 0, 100)'''
            )
        conn.execute('''INSERT INTO sensor(
            sensor_id, sensor_name, sensor_type, sensor_unit, sensor_min, sensor_max)
            values(3, "GYSFDMAXB", "Latitude", "", 0, 360)'''
            )

        conn.execute('''INSERT INTO sensor(
            sensor_id, sensor_name, sensor_type, sensor_unit, sensor_min, sensor_max)
            values(4, "GYSFDMAXB", "Longitude", "", 0, 360)'''
            )

        conn.execute('''INSERT INTO sensor(
            sensor_id, sensor_name, sensor_type, sensor_unit, sensor_min, sensor_max)
            values(5, "MH-Z19B", "CO2", "ppm", 0, 9999)'''
            )

        conn.execute('''INSERT INTO sensor(
            sensor_id, sensor_name, sensor_type, sensor_unit, sensor_min, sensor_max)
            values(6, "GP2Y1026AU0F", "Dust", "mg/m³", 0, 9999)'''
            )

        conn.execute('''INSERT INTO sensor(
            sensor_id, sensor_name, sensor_type, sensor_unit, sensor_min, sensor_max)
            values(7, "MQ-135", "Gas", "", 0, 1000)'''
            )

        conn.commit()
        conn.close()

    def check_device_id(self):
        connection = db.connect_air_database()
        device_id = 0
        try:
            with connection.cursor() as cursor:
                sql = f'''SELECT device_id FROM device WHERE device_id = {self.mac}'''
                cursor.execute(sql)
                device_id = cursor.rowcount
        finally:
            connection.close()

        if device_id == self.mac:
            lcd.message("Authentication", 1)
            lcd.msssage("successful", 2)

            return True
        else:
            self.lcd.message("Authentication", 1)
            self.lcd.msssage("failed", 2)

            return False
