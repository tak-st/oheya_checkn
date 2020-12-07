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

      temp_data = mesdata.MeasureClass(temp.get_temperature(), device_id)
      gps_data = mesdata.MeasureClass(gps.get_gps(), device_id)
      co2_data = mesdata.MeasureClass(co2.read_all(), device_id)

      print("~~~~~~~")
      time.sleep(1)

      temp_data.data_print()
      co2_data.data_print()
      gps_data.dataprint()

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
