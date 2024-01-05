from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from pymongo.errors import OperationFailure
import datetime  
import time

client = MongoClient('localhost', 27017)
# dab = client["FaceAttendance"]

db = client.get_database("FaceAttendance")

user="Vedant"
password="IMPOM"
    
# Checking Attendance
prof=db[user].find_one({"Type": "data", "Date": "2023-11-08", "Class": "CS203"})
stud=db[user].find_one({"Type": "list", "Class": "CS203"})

bul = {True: 1, False: 0}

for i in stud["Data"]:
    try:
        print(str(i[1])+" was "+["absent.", "present."][bul['1'==(prof["Data"])[i[0]]]])
    except:
        print(str(i[1])+" was "+"absent.")