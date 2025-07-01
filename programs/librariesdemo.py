import os
print(os.getcwd())  # display current working directory

# display files
for file in os.listdir():
    print(file)

import math
print(math.tan(1))

## create directory
os.mkdir("programs")

# delete directory
os.rmdir("programs")

# get your OS info
import platform
print(platform.platform())

# todays time
import time
import datetime
print(datetime.datetime.now())

# display memory utilization
import psutil
print(psutil.virtual_memory())
print(psutil.disk_partitions())

import calendar
print(calendar.month(2025,7))
print(calendar.calendar(2025))


import random
alist = [45,7,12,76,3,67,32,6,0]
print(random.random())
random.shuffle(alist)
print(alist)
print(random.randrange(100,999))


## write to the file
fobj = open("files.txt","w")
fobj.write("python\n")
for file in os.listdir():
    fobj.write(file + "\n")
fobj.close()

import csv
fobj = open("employees.csv","w")
data = [["Name","Age","City"],["Ram",32,"NY"],["Amit",31,"Bng"]]
writer = csv.writer(fobj)
writer.writerows(data)

import json
book = {"chap1":10 , "chap2":20}
fobj = open("data.json","w")
json.dump(book,fobj)