from lcddisplay import jlcd
import connect_database as db
import MySQLdb
import pymysql

class MeasureClass:

  def __init__(self, data):
    self.measure_data = data

  def data_display(self):
    lcd = jlcd.Jlcd(2,0x27,True)

    if type(self.measure_data) is dict :
      count = 1

      for measure_data_value in measure_data.values():
        lcd.message(str(self.measure_data), count)
        count += 1

    else:
      lcd.message(str(self.measure_data), 1)
      lcd.message(str(self.measure_data), 2)

  def data_post_db(self):
    pymysql.install_as_MySQLdb()
    connection = db.connect_air_database()
    cursor = connection.cursor()
    time = datetime.datetime.now()

    try:
      if type(self.measure_data) is dict:
        print("post" + self.measure_data)
      else:
        print("post" + self.measure_data)

    except MySQLdb.Error as e:
      print(e)

    connection.commit()
    connection.close()
