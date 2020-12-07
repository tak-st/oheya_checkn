import threading
import time
import wiringpi
from co2 import getco2 as co2
from gps import getgps as gps
from humansensor import humansensor as human
from lcddisplay import jlcd as lcd
from temperature import temperature as temp

# ボタンを繋いだGPIOの識別番号
button_pin1 = 18
button_pin2 = 23

# GPIO初期化
wiringpi.wiringPiSetupGpio()

# GPIOを出力モード(1)に設定
wiringpi.pinMode(button_pin1,0)
wiringpi.pinMode(button_pin2,0)

# 端子に何も接続されていない場合の状態を設定
# 3.3Vの場合には「2」（プルアップ）
# 0Vの場合は「1」と設定する（プルダウン）
wiringpi.pullUpDnControl(button_pin1, 2)
wiringpi.pullUpDnControl(button_pin2, 2)

lcd = jlcd.Jlcd(2, 0x27, True)

device_id = 1111

# lcdの切り替え用
cnt = 0


def push_button():
    # ボタン入力を識別
    # GPIO端子の状態を読み込む
    # ボタンを押すと「0」、放すと「1」になる
    # GPIOの状態が0V(0)であるか比較

    global cnt
    # チャタリング対策用
    flg1 = False
    flg2 = False
    while True:
        if (wiringpi.digitalRead(button_pin1) == 0):
            if flg1 is False:
                cnt += 1
            flg1 = True
        else:
            flg1 = False

        if (wiringpi.digitalRead(button_pin2) == 0):
            if flg2 is False:
                cnt -= 1
                flg2 = True
            if cnt == -1:
                cnt = 2
            elif cnt == -2:
                cnt = 1
        else:
            flg2 = False

        if cnt == 3:
            cnt = 0
        elif cnt == -3:
            cnt = 0


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

thread_main = threading.Thread(target = main_loop)
thread_human = threading.Thread(target=human.get_human)
thread_button = threading.Thread(target=push_button)
thread_main.setDaemon(True)
thread_human.setDaemon(True)
thread_button.setDaemon(True)
thread_main.start()
thread_human.start()
thread_button.start()

while True:
  pass