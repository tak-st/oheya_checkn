import threading
import time
import pymysql
import wiringpi
import MySQLdb
import datetime
import connect_database as db
from pydub import AudioSegment
from pydub.playback import play
from device.co2 import getco2 as co2
from device.gps import getgps as gps
from device.humansensor import humansensor as human
from device.temperature import temperature as temp

device_id = 1111

# 各センサーのデータ取得
temp_data = 0
gps_data = 0
co2_data = 0


def get_data():
    # グローバル変数
    global temp_data
    global gps_data
    global co2_data

    temp_data = temp.get_temperature()
    gps_data = gps.get_gps()
    co2_data = co2.get_co2()


def soundEffect(num):
    # button_pin =

    # GPIO初期化
    wiringpi.wiringPiSetupGpio()

    # GPIOを出力モード(1)に設定
    wiringpi.pinMode(button_pin, 0)

    # 端子に何も接続されていない場合の状態を設定
    # 3.3Vの場合には「2」（プルアップ）
    # 0Vの場合は「1」と設定する（プルダウン）
    wiringpi.pullUpDnControl(button_pin, 2)

    flg = False
    state = 0
    lcd = LCD(2, 0x027, True)

    while True:
        if wiringpi.digitalRead(button_pin) == 0:
            if flg is False:
                if state == 0:
                    lcd.message("オンセイ:ON", 1)
                    time.sleep(2)
                    state = 1
                else:
                    lcd.message("オンセイ:OFF", 1)
                    time.sleep(2)
                    state = 0
                flg = True
        else:
            flg = False

        if state == 1:
            if num == 1:
                sound = AudioSegment.from_mp3("gs-16b-2c-44100hz.mp3")
                play(sound)
            elif num == 2:
                sound = AudioSegment.from_mp3("gs-16b-2c-44100hz.mp3")
                play(sound)
            elif num == 3:
                sound = AudioSegment.from_mp3("gs-16b-2c-44100hz.mp3")
                play(sound)


def menu_button():
    # ボタンを繋いだGPIOの識別番号
    # 左から戻る、進む、lcd_display、決定
    # button_pin1 =　
    # button_pin2 =
    # button_pin3 =
    # button_pin4 =

    # GPIO初期化
    wiringpi.wiringPiSetupGpio()

    # GPIOを出力モード(1)に設定
    wiringpi.pinMode(button_pin1, 0)
    wiringpi.pinMode(button_pin2, 0)
    wiringpi.pinMode(button_pin3, 0)
    wiringpi.pinMode(button_pin4, 0)

    # 端子に何も接続されていない場合の状態を設定
    # 3.3Vの場合には「2」（プルアップ）
    # 0Vの場合は「1」と設定する（プルダウン）
    wiringpi.pullUpDnControl(button_pin1, 2)
    wiringpi.pullUpDnControl(button_pin2, 2)
    wiringpi.pullUpDnControl(button_pin3, 2)
    wiringpi.pullUpDnControl(button_pin4, 2)

    # チャタリング対策用
    flg1 = False
    flg2 = False
    flg3 = False
    flg4 = False
    flg5 = False
    flg6 = False
    reset_flg = False
    cnt = 0

    while True:
        if wiringpi.digitalRead(button_pin1) == 0:
            if flg1 is False:
                cnt += 1
                flg1 = True
        else:
            flg1 = False

        if wiringpi.digitalRead(button_pin2) == 0:
            if flg2 is False:
                cnt -= 1
                flg2 = True
            if cnt == -1:
                cnt = 2
            elif cnt == -2:
                cnt = 1
        else:
            flg2 = False

        if wiringpi.digitalRead(button_pin3) == 0:
            if flg3 is False:
                lcd_display()
                flg3 = True

        if cnt == 2:
            cnt = 0
        elif cnt == -2:
            cnt = 0

        if cnt == 0:
            lcd.message("メニュー", 1)
            lcd.message("リセット", 2)
            if wiringpi.digitalRead(button_pin4) == 0:
                if flg4 is False:
                    lcd.message("データヲリセットシマスカ？", 1)
                    lcd.message("ヒダリ：キャンセル　ミギ：ケッテイ", 2)
                    flg4 = True

                    if wiringpi.digitalRead(button_pin3) == 0:
                        if flg5 is False:
                            reset_button()

                    if wiringpi.digitalRead(button_pin4) == 0:
                        if flg6 is False:
                            reset_flg = True
                            flg6 = True
                    else:
                        flg6 = False
                else:
                    flg4 = False

        if reset_flg is True:
            lcd.message("リセットシマシタ。", 1)
            # リセット処理を記述予定


def lcd_display():
    Temperature = mesdata.MeasureClass(temp_data, device_id)
    Gps = mesdata.MeasureClass(gps_data, device_id)
    Co2 = mesdata.MeasureClass(co2_data, device_id)

    # ボタンを繋いだGPIOの識別番号
    button_pin1 = 18
    button_pin2 = 23
    # メニューボタン
    # button_pin3 =

    # GPIO初期化
    wiringpi.wiringPiSetupGpio()

    # GPIOを出力モード(1)に設定
    wiringpi.pinMode(button_pin1, 0)
    wiringpi.pinMode(button_pin2, 0)
    wiringpi.pinMode(button_pin3, 0)

    # 端子に何も接続されていない場合の状態を設定
    # 3.3Vの場合には「2」（プルアップ）
    # 0Vの場合は「1」と設定する（プルダウン）
    wiringpi.pullUpDnControl(button_pin1, 2)
    wiringpi.pullUpDnControl(button_pin2, 2)
    wiringpi.pullUpDnControl(button_pin3, 2)
    # チャタリング対策用
    flg1 = False
    flg2 = False
    flg3 = False
    cnt = 0

    while True:
        # ボタン入力を識別
        # GPIO端子の状態を読み込む
        # ボタンを押すと「0」、放すと「1」になる
        # GPIOの状態が0V(0)であるか比較
        if wiringpi.digitalRead(button_pin1) == 0:
            if flg1 is False:
                cnt += 1
                flg1 = True
        else:
            flg1 = False

        if wiringpi.digitalRead(button_pin2) == 0:
            if flg2 is False:
                cnt -= 1
                flg2 = True
            if cnt == -1:
                cnt = 2
            elif cnt == -2:
                cnt = 1
        else:
            flg2 = False

        if wiringpi.digitalRead(button_pin3) == 0:
            if flg3 is False:
                menu_button()

        if cnt == 3:
            cnt = 0
        elif cnt == -3:
            cnt = 0

        if cnt == 0:
            soundEffect(1)
            Temperature.data_display()
        elif cnt == 1:
            soundEffect(2)
            Gps.data_display()
        else:
            soundEffect(3)
            Co2.data_display()
