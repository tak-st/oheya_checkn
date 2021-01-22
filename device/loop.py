import time
#import simpleaudio as sa
import connect_database as db
import measure_data as data
import setup
import wiringpi
from pydub import AudioSegment
from pydub.playback import play
from co2 import mh_z19 as co2
from gps import getgps as gps
from gas import gas
from temperature import temperature as temp


class Loop:
    def __init__(self):

        # セットアップのインスタンス生成
        first_setup = setup.FirstSetup()
        # デバイスIDの取得
        self.device_id = first_setup.get_device_id()
        # ボタン識別用のカウント
        self.button_count = 0
        #ボタンが押されたという証
        self.display_flg = False
        #データが変わったという証
        self.temp_change_flg = False
        self.gps_change_flg = False
        self.co2_change_flg = False
        self.gas_change_flg = False

        # 各センサーのデータ取得
        self.temp_data = {"temp": 0, "humidity": 0}
        self.gps_data = {"latitude": 0, "longitude": 0}
        self.co2_data = {"co2": 0}
        self.gas_data = {"gas": 0}

    def get_data(self):

        while True:

            temp_data = temp.get_temperature()
            gps_data = gps.get_gps()
            co2_data = co2.read_all()
            gas_data = gas.get_gas()

            if self.temp_data != temp_data:
                self.temp_data = temp_data
                self.temp_change_flg = True
            else:
                self.temp_change_flg = False

            if self.gps_data != gps_data:
                self.gps_data = gps_data
                self.gps_change_flg = True
            else:
                self.gps_change_flg = False

            if self.co2_data != co2_data:
                self.co2_data = co2_data
                self.co2_change_flg = True
            else:
                self.co2_change_flg = False

            if self.gas_data != gas_data:
                self.gas_data = gas_data
                self.gas_change_flg = True
            else:
                self.gas_change_flg = False

            time.sleep(5)

    def post_db(self):

        while True:

            # 0はやエラーは送信しない
            if isinstance(self.temp_data, dict) and 0 not in self.temp_data.values():
                temp_data_class = data.MeasureData(self.temp_data, self.device_id)
                temp_data_class.data_post_db()

            if isinstance(self.gps_data, dict) and 0 not in self.gps_data.values():
                gps_data_class = data.MeasureData(self.gps_data, self.device_id)
                gps_data_class.data_post_db()

            if isinstance(self.co2_data, dict) and self.co2_data["co2"] != 0:
                co2_data_class = data.MeasureData(self.co2_data, self.device_id)
                co2_data_class.data_post_db()

            if isinstance(self.gas_data, dict) and 0 not in self.gas_data.values():
                gas_data_class = data.MeasureData(self.gas_data, self.device_id)
                gas_data_class.data_post_db()

            time.sleep(10)

    def print_data(self):

        while True:
            # ０やエラーは表示しない
            # ボタンで表示切り替え

            if self.button_count == 0:
                if isinstance(self.temp_data, dict) and 0 not in self.temp_data.values():
                    temp_data_class = data.MeasureData(self.temp_data, self.device_id)
                    if self.display_flg is True:
                        temp_data_class.data_display()
                        temp_data_class.data_print()
                        self.display_flg = False
                    if self.temp_change_flg is True:
                        temp_data_class.data_display()
                        self.temp_change_flg = False

            elif self.button_count == 1:
                if isinstance(self.gps_data, dict) and 0 not in self.gps_data.values():
                    gps_data_class = data.MeasureData(self.gps_data, self.device_id)
                    if self.display_flg is True:
                        gps_data_class.data_display()
                        gps_data_class.data_print()
                        self.display_flg = False
                    if self.gps_change_flg is True:
                        gps_data_class.data_display()
                        self.gps_change_flg = False

            elif self.button_count == 2:
                if isinstance(self.co2_data, dict) and self.co2_data["co2"] != 0:
                    co2_data_class = data.MeasureData(self.co2_data, self.device_id)
                    if self.display_flg is True:
                        co2_data_class.data_display()
                        co2_data_class.data_print()
                        self.display_flg = False
                    if self.co2_change_flg is True:
                        co2_data_class.data_display()
                        self.co2_change_flg = False

            elif self.button_count == 3:
                display_flag = True
                if isinstance(self.gas_data, dict) and 0 not in self.gas_data.values():
                    gas_data_class = data.MeasureData(self.gas_data, self.device_id)
                    if self.display_flg is True:
                        gas_data_class.data_display()
                        gas_data_class.data_print()
                        self.display_flg = False
                    if self.gas_change_flg is True:
                        gas_data_class.data_display()
                        self.gas_change_flg = False

    def check_bt(self):

        bt1 = 6
        bt2 = 13
        bt3 = 19
        bt4 = 26

        flg1 = False
        flg2 = False
        flg3 = False
        flg4 = False

        wiringpi.wiringPiSetupGpio()

        wiringpi.pinMode(bt1, 0)
        wiringpi.pinMode(bt2, 0)
        wiringpi.pinMode(bt3, 0)
        wiringpi.pinMode(bt4, 0)

        wiringpi.pullUpDnControl(bt1, 2)
        wiringpi.pullUpDnControl(bt2, 2)
        wiringpi.pullUpDnControl(bt3, 2)
        wiringpi.pullUpDnControl(bt4, 2)

        while True:

            if wiringpi.digitalRead(bt1) == 0:
                if flg2 is False:
                    self.button_count -= 1
                    print("- button" + str(self.button_count))
                    flg2 = True
                    self.display_flg = True

                if self.button_count == -1:
                    self.button_count = 3
            else:
                flg2 = False

            if wiringpi.digitalRead(bt2) == 0:
                if flg1 is False:
                    self.button_count += 1
                    print("+button" + str(self.button_count))
                    flg1 = True
                    self.display_flg = True
                    
                if self.button_count == 4:
                    self.button_count = 0
            else:
                flg1 = False


"""
def soundEffect(num):

    button_pin = 19
    
    # GPIO初期化
    wiringpi.wiringPiSetupGpio()

    # GPIOを出力モード(1)に設定
    wiringpi.pinMode(button_pin, 0)

    # 端子に何も接続されていない場合の状態を設定
    # 3.3Vの場合には「2」（プルアップ）
    # 0Vの場合は「1」と設定する（プルダウン）
    wiringpi.pullUpDnControl(button_pin, 2)

    flg = False
    state = 1
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
                wav1 = sa.WaveObject.from_wave_file("音声ファイルのルートを指定する")
                play_obj = wav1.play()
            elif num == 2:
                wav2 = sa.WaveObject.from_wave_file("音声ファイルのルートを指定する")
                play_obj = wav2.play()
            elif num == 3:
                wav3 = sa.WaveObject.from_wave_file("音声ファイルのルートを指定する")
                play_obj = wav2.play()
            
            play_obj.wait_done()

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
    button_pin1 = 6
    button_pin2 = 13

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
            temp_data_class.data_display()
        elif cnt == 1:
            soundEffect(2)
            gps_data_class.data_display()
        else:
            soundEffect(3)
            gas_data_class.data_display()
"""
