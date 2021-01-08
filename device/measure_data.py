from lcddisplay import jlcd
import operate_database as op
import setup
import datetime

class MeasureData:

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
    elif "dust" in self.measure_data:
      lcd.message("ホコリ : " + str(self.measure_data["dust"]), 1)
      lcd.message("", 2)
    elif "gas" in self.measure_data:
      lcd.message("ガス : " + str(self.measure_data["gas"]), 1)
      lcd.message("", 2)

  def data_post_db(self):
    local = op.OperateLocalDatabase()
    #remote = op.OperateRemoteDatabase()
    #setup = setup.Setup()
    time = datetime.datetime.now()

    if "temp" in self.measure_data:
      local.insert_data(self.device_id, 0, str(self.measure_data["temp"]), str(time))
      local.insert_data(self.device_id, 1, str(self.measure_data["humidity"]), str(time))
      """
      if setup.check_device_id():
        remote.insert_data(self.device_id, 0, str(self.measure_data["temp"]), str(time))
        remote.insert_data(self.device_id, 1, str(self.measure_data["humidity"]), str(time))
      """

    elif "latitude" in self.measure_data:
      local.insert_data(self.device_id, 2, str(self.measure_data["latitude"]), str(time))
      local.insert_data(self.device_id, 3, str(self.measure_data["longitude"]), str(time))
      """
      if setup.check_device_id():
        remote.insert_data(self.device_id, 2, str(self.measure_data["latitude"]), str(time))
        remote.insert_data(self.device_id, 3, str(self.measure_data["longitude"]), str(time))
    """

    elif "co2" in self.measure_data:
      local.insert_data(self.device_id, 4, str(self.measure_data["co2"]), str(time))
      """
      if setup.check_device_id():
        remote.insert_data(self.device_id, 4, str(self.measure_data["co2"]), str(time))
    """

    elif "dust" in self.measure_data:
      local.insert_data(self.device_id, 5, str(self.measure_data["dust"]), str(time))
      
      """
      if setup.check_device_id():
        remote.insert_data(self.device_id, 5, str(self.measure_data["dust"]), str(time))
    """

    elif "gas" in self.measure_data:
      local.insert_data(self.device_id, 6, str(self.measure_data["gas"]), str(time))
      """
      if setup.check_device_id():
        remote.insert_data(self.device_id, 6, str(self.measure_data["gas"]), str(time))
    """
      
      """
    remote_max_time = remote.select_maxtime(self.device_id)

    with local.comparison_time(remote_max_time) as unsent_data:
      for sent_data in unsent_data:
        remote.insert_data(sent_data[0], sent_data[1], sent_data[2], sent_data[3])
    """

  def data_print(self):
    print(str(self.measure_data))
