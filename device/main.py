import time
from gps import getgps as gps
from humansensor import humansensor as human
from temperature import temperature as temp
from co2 import getco2 as co2

lcd = jlcd.Jlcd(2,0x27,True)

device_id = 1111

def main_loop():
  while True :
    try :

      #各センサーのデータ取得
      temp_data = temp.get_temperature()
      gps_data = gps.get_gps()
      co2_data = co2.read_all()

      """
      ここにスイッチを判別する条件分岐
      """

      if temp_data is not None :
        Temperature = mesdata.MeasureClass(temp_data, device_id)
        Temperature.data_print()
        """
        ここをflgでif分岐してください
        Temperature.data_display()
        """
      else:
        print("temperature is none")

      if gps_data is not None :
        Gps = mesdata.MeasureClass(gps_data, device_id)
        Gps.data_print()
        """
        ここをスイッチのflgでif分岐してください
        Gps.data_display()
        """
      else:
        print("gps is none")

      if co2_data is not None :
        Co2 = mesdata.MeasureClass(co2_data, device_id)
        Co2.data_print()
        """
        ここをスイッチのflgでif分岐してください
        Co2.data_display()
        """
      else:
        print("co2 is none")

      time.sleep(3)

      except KeyboardInterrupt:
        break

thread_main = threading.Thread(target = main_loop)
thread_human = threading.Thread(target = human.get_human)
thread_main.setDaemon(True)
thread_human.setDaemon(True)
thread_main.start()
thread_human.start()

while True:
  pass
