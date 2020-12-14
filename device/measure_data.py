from lcddisplay import jlcd
import operate_database as op
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
    local = op.OperateLocalDatabase()
    remote = op.OperateRemoteDatabase()
    time = datetime.datetime.now()

    if "temp" in self.measure_data:
      local.insert_data(self.device_id, 0, str(self.measure_data["temp"]), str(time))
      local.insert_data(self.device_id, 1, str(self.measure_data["humidity"]), str(time))
    elif "latitude" in self.measure_data:
      local.insert_data(self.device_id, 2, str(self.measure_data["latitude"]), str(time))
      local.insert_data(self.device_id, 3, str(self.measure_data["longitude"]), str(time))
    elif "co2" in self.measure_data:
      local.insert_data(self.device_id, 4, str(self.measure_data["co2"]), str(time))
    elif "Dust" in self.measure_data:
      local.insert_data(self.device_id, 5, str(self.measure_data["dust"]), str(time))
    elif "Gas" in self.measure_data:
      local.insert_data(self.device_id, 6, str(self.measure_data["gas"]), str(time))

  def data_print(self):
    print(str(self.measure_data))
