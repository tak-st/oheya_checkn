import time
from gps import getgps as gps
from humansensor import humansensor as human
from lcddisplay import jlcd
from temperature import temperature as temp
from co2 import getco2 as co2

lcd = jlcd.Jlcd(2,0x27,True)

while 1 :
  try :
    temp_val = temp.get_temperature()
    gps_val = gps.get_gps()
    co2_val = co2.get_co2()

    print("~~~~~~~")
    time.sleep(1)

    print(temp_val)
    lcd.message(str(temp_val["temp"]))
    time.sleep(5)

    print(gps_val)
    lcd.message(str(gps_val["latitude"]), 1)
    lcd.message(str(gps_val["longitude"]), 2)
    time.sleep(5)

    print(co2_val)
    lcd.message(str(co2_val))
    time.sleep(5)

    time.sleep(10)

  except KeyboardInterrupt:
    break
