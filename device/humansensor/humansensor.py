from datetime import datetime
import time
import RPi.GPIO as GPIO

#インターバル
interval=3
#スリープタイム
sleeptime=2
#使用するGPIO
GPIO_PIN=18

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN,GPIO.IN)

def get_human():
    try:
        print("cancel:CTRL+C")
        cnt=1
        while True:
            #センサー感知
            if(GPIO.input(GPIO_PIN)==GPIO.HIGH):
                now=datetime.now().strftime('%Y/%m/%d %H:%M:%S')

                print(now+":"+str("{0:05d}".format(cnt)) + "回目の人感知")
                cnt+=1
                time.sleep(sleeptime)
            else:
                print(GPIO.input(GPIO_PIN))
                time.sleep(interval)
    except KeyboardInterrupt:
        print("終了処理中…")
    finally:
        GPIO.cleanup()
        print("GPIO　Clean")
