from pqueue import PriorityQueue
import pymysql


conn = pymysql.connect(host='localhost', user='root',
                       password="Bikram@2004", db='train')
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


def iterateAllSeats():
    seats = getALlSeatNumber()
    index = len(seats) // 2
    flag = True

    temp = seats[index]

    # seat allocate iteration
    for i in temp:
        print(i, end="\t")
    else:
        print()
        for j in range(1, 9):
            if flag == True:
                index -= j
                for k in seats[index]:
                    print(k, end="\t")
                flag = False
                print()
            else:
                index += j
                for k in seats[index]:
                    print(k, end="\t")
                flag = True
                print()

    return


def allocateSeat(item, x):
    query = "update general set name = '{}', age = {}, gender = '{}', status = True where seat_no = {}".format(
        item["first_name"] + ' ' + item["last_name"], item["age"], item["gender"], x)
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
        item = l.append(item)
        singleAllocateSeat(l)
    return


details = [
    [
        {'first_name': 'Arijit', 'last_name': 'Singh', 'age': 50, 'gender': 'male'},
        {'first_name': 'Shreya', 'last_name': 'Ghoshal',
            'age': 40, 'gender': 'female'},
        {'first_name': 'Sonu', 'last_name': 'Nigam', 'age': 55, 'gender': 'male'},
        {'first_name': 'Lata', 'last_name': 'Mangeshkar',
            'age': 70, 'gender': 'female'}
    ],
    [
        {'first_name': 'John', 'last_name': 'Doe', 'age': 25, 'gender': 'male'}
    ],
    [
        {'first_name': 'Alice', 'last_name': 'Smith', 'age': 30, 'gender': 'female'},
        {'first_name': 'Bob', 'last_name': 'Johnson', 'age': 35, 'gender': 'male'}
    ],
    [
        {'first_name': 'Emma', 'last_name': 'Brown', 'age': 28, 'gender': 'female'},
    ],
    [
        {'first_name': 'Daniel', 'last_name': 'Williams', 'age': 40, 'gender': 'male'},
        {'first_name': 'Grace', 'last_name': 'Miller', 'age': 62, 'gender': 'female'}
    ],
    [
        {'first_name': 'Ryan', 'last_name': 'Davis', 'age': 32, 'gender': 'male'},
        {'first_name': 'Sophia', 'last_name': 'Wilson',
            'age': 29, 'gender': 'female'},
        {'first_name': 'Michael', 'last_name': 'Jones', 'age': 45, 'gender': 'male'}
    ],
    [
        {'first_name': 'Mukesh', 'last_name': 'Ambani', 'age': 65, 'gender': 'male'}
    ],
    [
        {'first_name': 'Ethan', 'last_name': 'Martinez', 'age': 38, 'gender': 'male'},
        {'first_name': 'Ava', 'last_name': 'Lee', 'age': 26, 'gender': 'female'},
        {'first_name': 'William', 'last_name': 'Taylor', 'age': 33, 'gender': 'male'}
    ],
    [
        {'first_name': 'Mia', 'last_name': 'Johnson', 'age': 31, 'gender': 'female'},
        {'first_name': 'James', 'last_name': 'Clark', 'age': 29, 'gender': 'male'},
        {'first_name': 'Noah', 'last_name': 'Ramirez', 'age': 41, 'gender': 'male'},
        {'first_name': 'Liam', 'last_name': 'Perez', 'age': 67, 'gender': 'male'}
    ],
    [
        {'first_name': 'Emily', 'last_name': 'Anderson',
            'age': 23, 'gender': 'female'},
        {'first_name': 'Abigail', 'last_name': 'Hill',
            'age': 28, 'gender': 'female'},
        {'first_name': 'Isabella', 'last_name': 'Baker',
            'age': 30, 'gender': 'female'},
        {'first_name': 'Logan', 'last_name': 'Garcia', 'age': 64, 'gender': 'male'},
        {'first_name': 'Olivia', 'last_name': 'Moore', 'age': 27, 'gender': 'female'}
    ]
]

pq = PriorityQueue()

for i in range(len(details)):
    pq.push(details[i], len(details[i]), i)

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
