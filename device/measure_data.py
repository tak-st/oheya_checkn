from lcddisplay import jlcd
import connect_database as db
import MySQLdb
import pymysql

class MeasureClass:

  def __init__(self, data, device_id):
    self.measure_data = data
    self.device_id = device_id

  def data_display(self):
    lcd = jlcd.Jlcd(2,0x27,True)

    if "temp" in self.measure_data:
      lcd.message("キオン : " + str(self.measure_data["temp"]), 1)
      lcd.message("シツド : " + str(self.measure_data["humidity"]), 2)
    elif "co2" in self.measure_data:
      lcd.message("CO2 : " + str(self.measure_data["co2"]), 1)
      lcd.message("", 2)
    elif "latitude" in self.measure_data:
      lcd.message("イド : " + str(self.measure_data["latitude"]), 1)
      lcd.message("ケイド : " + str(self.measure_data["longitude"]), 2)

  def data_post_db(self):
    pymysql.install_as_MySQLdb()
    connection = db.connect_air_database()
    cursor = connection.cursor()
    time = datetime.datetime.now()

    if "temp" in self.measure_data:
      cur.execute("INSERT INTO device_data VALUES('" + str(1) + "','" + "temperature"
                  + "','" + str(time) + "','" + str(self.measure_data["temp"]) + "')")
      cur.execute("INSERT INTO device_data VALUES('" + str(1) + "','" + "humidity"
                  + "','" + str(time) + "','" + str(self.measure_data["humidity"]) + "')")
    elif "co2" in self.measure_data:
      cur.execute("INSERT INTO device_data VALUES('" + str(1) + "','" + "co2"
                  + "','" + str(time) + "','" + str(self.measure_data["co2"]) + "')")
    elif "latitude" in self.measure_data:
      cur.execute("INSERT INTO device_data VALUES('" + str(1) + "','" + "latitude"
                  + "','" + str(time) + "','" + str(self.measure_data["latitude"]) + "')")
      cur.execute("INSERT INTO device_data VALUES('" + str(1) + "','" + "longitude"
                  + "','" + str(time) + "','" + str(self.measure_data["longitude"]) + "')")

    except MySQLdb.Error as e:
      print(e)

    connection.commit()
    connection.close()

  def data_print(self):
    print(str(self.measure_data))
