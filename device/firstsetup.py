#coding:utf-8
from uuid import getnode as get_mac
import random
import math

class setup:
    def __init__(self):
        #MACアドレスをランダムなシード値で再作成
        random.seed(get_mac())
        mac = math.floor(random.random()*1000000)


    def main(self):
        #LCDに表示
        lcd = LCD(2,0x027,True)
        lcd.message(str(mac),1)
