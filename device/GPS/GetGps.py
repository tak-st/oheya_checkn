# coding:utf-8
import serial
import micropyGPS
import time

def getgps():
    gps = micropyGPS.MicropyGPS(9, 'dd') # MicroGPSオブジェクトを生成する
        # 引数はタイムゾーンの時差と出力フォーマット
    s = serial.Serial('/dev/serial0', 9600, timeout=10)
    s.readline() # 最初の1行は中途半端なデーターが読めることがあるので、捨てる
    
    for i in range(5) :
        sentence = s.readline().decode('utf-8') # GPSデーターを読み、文字列に変換する
        if sentence[0] != '$': # 先頭が'$'でなければ捨てる
             continue
        for x in sentence : # 読んだ文字列を解析してGPSオブジェクトにデーターを追加、更新する
            gps.update(x)
            
    h = gps.timestamp[0] if gps.timestamp[0] < 24 else gps.timestamp[0] - 24
    gpsval = {"latitude": gps.latitude[0], "longitude": gps.longitude[0], "timestamp": gps.timestamp[0]}
    
    return gpsval