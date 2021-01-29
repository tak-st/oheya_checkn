#coding:utf-8
import sqlite3
import connect_database as db
import pymysql

class OperateLocalDatabase:
  def __init__(self):
    pymysql.install_as_MySQLdb()
    self.DATABASE = 'my_air_data.db'

  def select_data(self, sensor_id):
    connection = sqlite3.connect(self.DATABASE)
    cursor = connection.cursor()
    
    try:
        cursor.execute("SELECT * FROM device_data WHERE ?", (sensor_id,))
        device_data = cursor.fetchall()

        return device_data
    except sqlite3.Error as e:
      print(e)
    finally:
      connection.close()

  def insert_data(self, device_id, sensor_id, sensor_data, time):
    connection = sqlite3.connect(self.DATABASE)
    cursor = connection.cursor()
    
    try:
        cursor.execute("INSERT INTO device_data VALUES (?, ?, ?, ?)", (device_id, sensor_id, sensor_data, time))
        connection.commit()
    except sqlite3.Error as e:
      print(e)
    finally:
      connection.close()

  def comparison_time(self, time):
    connection = sqlite3.connect(self.DATABASE)
    cursor = connection.cursor()
    
    try:
        cursor.execute("SELECT * FROM device_data WHERE time > ?", (time,))
        data = cursor.fetchall()

        return data
    except sqlite3.Error as e:
      print(e)
    finally:
      connection.close()

class OperateRemoteDatabase:
  def __init__(self):
    self.connection = db.connect_air_database()

  def select_data(self, sensor_id):
    cursor = self.connection.cursor()
    
    try:
        cursor.execute("SELECT * FROM device_data WHERE ?", (sensor_id,))
        device_data = cursor.fetchall()

        return device_data
    except pymysql.Error as e:
      print(e)
    finally:
      self.connection.close()

  def insert_data(self, device_id, sensor_id, sensor_data, time):
    cursor = self.connection.cursor()
    try:
        cursor.execute("INSERT INTO device_data VALUES(%s, %s, %s, %s)", (device_id, sensor_id, sensor_data, time))
        self.connection.commit()
    except pymysql.Error as e:
      print(e)
      self.connection.close()

  def select_maxtime(self, device_id):
    cursor = self.connection.cursor()
    try:
        cursor.execute("SELECT MAX(time) FROM device_data WHERE ? GROUP BY device_id", (device_id,))
        maxtime = cursor.fetchone()
        
        return maxtime
    except pymysql.Error as e:
        print(e)
    finally:
        self.connection.close()
