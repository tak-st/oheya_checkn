import threading
import time
import wiringpi
import setup
import loop
import os
from humansensor import humansensor as human

"""
from device.co2 import getco2 as co2
from device.gps import getgps as gps
from device.temperature import temperature as temp
"""

#セットアップのインスタンス生成
first_setup = setup.FirstSetup()
#デバイスIDの取得
device_id = first_setup.get_device_id()
#ローカーデータベースの生成
if os.path.isfile("my_air_data.db"):
    print("DB is exist")
else:
    first_setup.create_database()

"""
def main_loop():
    while True:
        try:
            # 各センサーのデータ取得
            temp_data = temp.get_temperature()
            gps_data = gps.get_gps()
            co2_data = co2.read_all()

            if temp_data is not None:
                Temperature = mesdata.MeasureClass(temp_data, device_id)
                Temperature.data_print()
                if cnt == 0:
                    Temperature.data_display()
            else:
                print("temperature is none")

            if gps_data is not None:
                Gps = mesdata.MeasureClass(gps_data, device_id)
                Gps.data_print()
                if cnt == 1:
                    Gps.data_display()
            else:
                print("gps is none")

            if co2_data is not None:
                Co2 = mesdata.MeasureClass(co2_data, device_id)
                Co2.data_print()
                if cnt == 2:
                    Co2.data_display()
            else:
                print("co2 is none")

            time.sleep(3)

        except KeyboardInterrupt:
            break
"""

#thread_human = threading.Thread(target=human.get_human)
thread_get_data = threading.Thread(target=loop.get_data)
thread_print_data = threading.Thread(target=loop.print_data)
thread_post_db = threading.Thread(target=loop.post_db)
#thread_human.setDaemon(True)
thread_get_data.setDaemon(True)
thread_print_data.setDaemon(True)
thread_post_db.setDaemon(True)
#thread_human.start()
thread_get_data.start()
thread_print_data.start()
thread_post_db.start()

while True:
    pass
