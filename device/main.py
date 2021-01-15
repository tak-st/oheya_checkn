import threading
import time
import wiringpi
import setup
import loop
import os
from humansensor import humansensor as human

#セットアップのインスタンス生成
first_setup = setup.FirstSetup()
#デバイスIDの取得
device_id = first_setup.get_device_id()

#リモートデータベースにデバイスID
first_setup.post_device_id()
#ローカーデータベースの生成
if os.path.isfile("my_air_data.db"):
    print("DB is exist")
else:
    first_setup.create_database()

#loopクラスのインスタンス生成
Loop = loop.Loop()

thread_human = threading.Thread(target=human.get_human)
thread_get_data = threading.Thread(target=Loop.get_data)
thread_print_data = threading.Thread(target=Loop.print_data)
thread_post_db = threading.Thread(target=Loop.post_db)
thread_human.setDaemon(True)
thread_get_data.setDaemon(True)
thread_print_data.setDaemon(True)
thread_post_db.setDaemon(True)
thread_human.start()
thread_get_data.start()
thread_print_data.start()
thread_post_db.start()

while True:
    pass
