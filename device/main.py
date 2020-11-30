import time
from gps import getgps as gps
from humansensor import humansensor as human
from lcddisplay import jlcd as lcd
from temperature import temperature as temp
from co2 import getco2 as co2


while 1 :
  try :
    print("~~~~~~~~~~")

  except KeyboardInterrupt:
    break
