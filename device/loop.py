import time
import connect_database as db
import measure_data as data
import setup
from pydub import AudioSegment
from pydub.playback import play
from co2 import mh_z19 as co2
from gps import getgps as gps
from gas import gas
from temperature import temperature as temp

#セットアップのインスタンス生成
first_setup = setup.FirstSetup()
#デバイスIDの取得
device_id = first_setup.get_device_id()

# 各センサーのデータ取得
temp_data = {"temp": 0, "humidity": 0}
gps_data = {"latitude": 0, "longitude": 0}
co2_data = {"co2": 0}
gas_data = {"gas": 0}


def get_data():
    
    # グローバル変数
    global temp_data
    global gps_data
    global co2_data
    global gas_data
    
    while True:
        temp_data = temp.get_temperature()
        gps_data = gps.get_gps()
        co2_data = co2.read_all()
        gas_data = gas.get_gas()
        time.sleep(5)

def post_db():
    
    # グローバル変数
    global temp_data
    global gps_data
    global co2_data
    global gas_data
    
    while True:
        
        #0はやエラーは送信しない
        if isinstance(temp_data, dict) and 0 not in temp_data.values():
            temp_data_class = data.MeasureData(temp_data, device_id)
            temp_data_class.data_post_db()
        
        if isinstance(gps_data, dict) and 0 not in gps_data.values():
            gps_data_class = data.MeasureData(gps_data, device_id)
            gps_data_class.data_post_db()
        
        if isinstance(co2_data, dict) and co2_data["co2"] != 0:
            co2_data_class = data.MeasureData(co2_data, device_id)
            co2_data_class.data_post_db()
            
        if isinstance(gas_data, dict) and 0 not in gas_data.values():
            gas_data_class = data.MeasureData(gas_data, device_id)
            gas_data_class.data_post_db()

        time.sleep(10)

def print_data():
    # グローバル変数
    global temp_data
    global gps_data
    global co2_data
    global gas_data
    
    while True:
        #０やエラーは表示しない
        #ボタンで表示切り替え
        if isinstance(temp_data, dict) and 0 not in temp_data.values():
            temp_data_class = data.MeasureData(temp_data, device_id)
            temp_data_class.data_print()
            temp_data_class.data_display()
            time.sleep(3)
            
        if isinstance(gps_data, dict) and 0 not in gps_data.values():
            gps_data_class = data.MeasureData(gps_data, device_id)
            gps_data_class.data_print()
            gps_data_class.data_display()
            time.sleep(3)
            
        if isinstance(co2_data, dict) and co2_data["co2"] != 0:
            co2_data_class = data.MeasureData(co2_data, device_id)
            co2_data_class.data_print()
            co2_data_class.data_display()
            time.sleep(3)
            
        if isinstance(gas_data, dict) and 0 not in gas_data.values():
            gas_data_class = data.MeasureData(gas_data, device_id)
            gas_data_class.data_print()
            gas_data_class.data_display()
            time.sleep(3)

def soundEffect(num):

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


def lcd_display():
    # グローバル変数
    global temp_data
    global gps_data
    global co2_data
    global gas_data

    #データクラスの初期化
    temp_data_class = data.MeasureData(temp_data, device_id)
    gps_data_class = data.MeasureData(gps_data, device_id)
    co2_data_class = data.MeasureData(co2_data, device_id)
    gas_data_class = data.MeasureData(gas_data, device_id)

    # ボタンを繋いだGPIOの識別番号
    button_pin1 = 18
    button_pin2 = 23

    # GPIO初期化
    wiringpi.wiringPiSetupGpio()

    # GPIOを出力モード(1)に設定
    wiringpi.pinMode(button_pin1, 0)
    wiringpi.pinMode(button_pin2, 0)

    # 端子に何も接続されていない場合の状態を設定
    # 3.3Vの場合には「2」（プルアップ）
    # 0Vの場合は「1」と設定する（プルダウン）
    wiringpi.pullUpDnControl(button_pin1, 2)
    wiringpi.pullUpDnControl(button_pin2, 2)
    # チャタリング対策用
    flg1 = False
    flg2 = False
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

        if cnt == 3:
            cnt = 0
        elif cnt == -3:
            cnt = 0

        if cnt == 0:
            soundEffect(1)
            temp_data_class.data_display()
        elif cnt == 1:
            soundEffect(2)
            gps_data_class.data_display()
        else:
            soundEffect(3)
            gas_data_class.data_display()
