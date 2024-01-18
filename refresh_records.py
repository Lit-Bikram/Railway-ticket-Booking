import pymysql

conn = pymysql.connect(host='localhost',user='root',password = "Bikram@2004",db='train')
cur = conn.cursor(pymysql.cursors.DictCursor)

query = "update general set name = NULL, age = NULL, gender = NULL, status = FAlSE"
cur.execute(query)

conn.commit()
cur.close()
conn.close()