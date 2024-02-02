from pqueue import PriorityQueue
import pymysql
import csv
import create_file as cfile

conn = pymysql.connect(host='localhost', user='root',password="Bikram@2004", db='train')
cur = conn.cursor(pymysql.cursors.DictCursor)


def createReferece(x):

    row = "select * from general where seat_no = {}".format(x)
    cur.execute(row)
    item = cur.fetchall()
    item = item[0]
    return item


def getALlSeatNumber():
    seats = []
    x = 1
    for i in range(9):
        temp = []
        for j in range(8):
            temp.append(x)
            x += 1
        seats.append(temp)

    return seats


# def iterateAllSeats():
#     seats = getALlSeatNumber()
#     index = len(seats) // 2
#     flag = True

#     temp = seats[index]

#     # seat allocate iteration
#     for i in temp:
#         print(i, end="\t")
#     else:
#         print()
#         for j in range(1, 9):
#             if flag == True:
#                 index -= j
#                 for k in seats[index]:
#                     print(k, end="\t")
#                 flag = False
#                 print()
#             else:
#                 index += j
#                 for k in seats[index]:
#                     print(k, end="\t")
#                 flag = True
#                 print()

#     return


def allocateSeat(item, x):
    query = "update general set name = '{}', age = {}, gender = '{}', status = True where seat_no = {}".format(item["first_name"] + ' ' + item["last_name"], item["age"], item["gender"], x)
    cur.execute(query)
    return


def singleAllocateSeat(item):
    seat_num = getALlSeatNumber()
    index = len(seat_num) // 2
    flag = True

    temp = seat_num[index]

    # seat allocate iteration
    item = item[0]

    for i in temp:
        seat = createReferece(i)

        if seat["status"] == 0:
            if item["age"] >= 60 and seat["seat_type"][-6:] != "_lower":
                continue
            else:
                allocateSeat(item, i)
                return
        else:
            continue
    else:
        for j in range(1, 9):
            if flag == True:
                index -= j
                for k in seat_num[index]:
                    seat = createReferece(k)
                    if seat["status"] == 0:
                        if item["age"] >= 60 and seat["seat_type"][-6:] != "_lower":
                            continue
                        else:
                            allocateSeat(item, k)
                            return
                    pass
                flag = False
            else:
                index += j
                for k in seat_num[index]:
                    seat = createReferece(k)
                    if seat["status"] == 0:
                        if item["age"] >= 60 and seat["seat_type"][-6:] != "_lower":
                            continue
                        else:
                            allocateSeat(item, k)
                            return
                    pass
                flag = True
        else:
            cfile.waitingList(item)
    return


def checkAvailability(item, arr):
    members = len(item)
    query = "select count(*) as count from general where status is FALSE and seat_no >= {} and seat_no <= {};".format(
        arr[0], arr[-1])
    cur.execute(query)
    item = cur.fetchall()
    item = item[0]
    count = item["count"]

    if members <= count:
        return True
    return False


def multipleAllocateSeat(items):
    for item in items:
        l = []
        l.append(item)
        singleAllocateSeat(l)
    return

pq = PriorityQueue()

with open('data/passengers.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    count = 0
    for row in reader:
        temp = []
        for i in range(0,len(row),4):
            record = {}
            record["first_name"] = row[i]
            record["last_name"] = row[i + 1]
            record["age"] = int(row[i + 2])
            record["gender"] = row[i + 3]
            temp.append(record)
        pq.push(temp, len(temp),count)
        # temp is a list of dictionaries
        count += 1

while pq.heap:
    popped_item = pq.pop()
    if len(popped_item) == 1:
        singleAllocateSeat(popped_item)
    else:
        multipleAllocateSeat(popped_item)
    # print(popped_item, len(popped_item), "\n")

conn.commit()

cur.close()
conn.close()
