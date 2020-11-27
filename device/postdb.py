
import MySQLdb
import datetime
import connect_database as db
import pymysql

def postnum():
  pymysql.install_as_MySQLdb()
  connection = db.connect_air_database()
  cur = connection.cursor()
  time = datetime.datetime.now()

  try:
    #CO2
    # cur.execute("INSERT INTO device_data VALUES('" + str(1) + "','" + "CO2" + "','" + str(Num.get("Co2")) + "','" + str(time) + "')")
    # cur.execute("INSERT INTO device_data VALUES('" + str(1) + "','" + "Temp" + "','" + str(Num.get("temperature")) + "','" + str(time) + "')")
    # cur.execute("INSERT INTO device_data VALUES('" + str(1) + "','" + "Locate" + "','" + str(Num.get("location")) + "','" + str(time) + "')")

  except MySQLdb.Error as e:
    print(e)

  con.commit()
  con.close()
