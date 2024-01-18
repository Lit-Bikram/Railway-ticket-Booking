import pymysql

conn = pymysql.connect(host='localhost',user='root',password = "Bikram@2004",db='train')

cur = conn.cursor()

create = """CREATE TABLE general (
    seat_no INT PRIMARY KEY,
    compartment INT,
    seat_type VARCHAR(15),
    name VARCHAR(50),
    age INT,
    gender VARCHAR(10),
    status BOOLEAN DEFAULT FALSE
);"""

# cur.execute(create)

for i in range(72):
    seatType = ["left_upper","left_middle","left_lower","side_upper","right_upper","right_middle","right_lower","side_lower"]
    seat = seatType[ i % 8 ]
    
    row = """
        INSERT INTO general (seat_no, compartment, seat_type)
        VALUES ({},{},"{}");
    """.format(i + 1,(i // 8) + 1,seat)

    # cur.execute(row)

cur.close()
    
cur = conn.cursor(pymysql.cursors.DictCursor)

# all = []
# for i in range(9):
#     temp = []
#     for j in range(8):
#         row = "select * from general where seat_no = {}".format((i+1)*(j+1))
#         cur.execute(row)
#         item = cur.fetchall()
#         temp.append(item[0])
#     all.append(temp)
    
# for i in all:
#     print(i,"\n\n")

conn.commit()

cur.close()
conn.close()
