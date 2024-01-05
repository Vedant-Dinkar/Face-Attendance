from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from pymongo.errors import OperationFailure
import datetime  
import time

client = MongoClient('localhost', 27017)
# dab = client["FaceAttendance"]

db = client.get_database("FaceAttendance")

log = db.get_collection("LogXY")

user="Vedant"
password="IMPOM"
    
# existing_profile = log.find_one({"Name": user, "Password": password})
# if existing_profile:
#     log = db.get_collection("LogXY")
#     print("EXISTS!")
# else:
#     aadmi=db.get_collection("LogXY")
#     print("DOES NOT EXIST!")

#app.get("/")

# userData = db[user]

student_data = [
    (0, 190001060, 'SURENDAR KETHAVATH'),
    (1, 220001001, 'AADISH JAIN'),
    (2, 220001002, 'ABHINAV GANGIL'),
    (3, 220001003, 'ADITI ASHISH WEKHANDE'),
    (4, 220001004, 'ADITYA KSHITIZ'),
    (5, 220001005, 'ADITYA SACHIN MASTUD'),
    (6, 220001006, 'ADITYA YADAV'),
    (7, 220001007, 'AMAN PRATAP SINGH'),
    (8, 220001008, 'AMIT TIWARI'),
    (9, 220001009, 'ANIRUDH GAUTAM'),
    (10, 220001010, 'ANNAMSHETTI SUMANTH'),
    (11, 220001011, 'ARAVAPALLI PAVAN KUMAR'),
    (12, 220001012, 'ATHARVA ANIL SANGAWAR'),
    (13, 220001013, 'ATHARVA NANOTI'),
    (14, 220001014, 'AVIRAL SHARMA'),
    (15, 220001015, 'AYITHA TRIBUVAN'),
    (16, 220001016, 'BALABHADRA RITHVIK'),
    (17, 220001017, 'BHARAT KAURAV'),
    (18, 220001018, 'BHAVANAM SAI PAVAN KUMAR REDDY'),
    (19, 220001019, 'BHUKYA HAVISH'),
    (20, 220001020, 'CHANDEKAR RIDDHI UMESH'),
    (21, 220001021, 'CHERUPALLY VINAY'),
    (22, 220001022, 'CHIRANJIVI KESHAV'),
    (23, 220001023, 'DARBHA KALYANA SRIRAM'),
    (24, 220001024, 'DARSHIL PATEL'),
    (25, 220001025, 'DEBASISH PADHY'),
    (26, 220001026, 'DEEPAK YADAV'),
    (27, 220001027, 'DEVANSHI CHHATBAR'),
    (28, 220001028, 'EDULA BHOOMIKA'),
    (29, 220001029, 'GARIMA UPADHYAY'),
    (30, 220001031, 'GUNTUKU RISHWANTH SAI'),
    (31, 220001032, 'HITESH MAURYA'),
    (32, 220001033, 'JAY SOLANKI'),
    (33, 220001034, 'JONNALAGADDA SAI PRANAY DEEP'),
    (34, 220001035, 'KALWAGHE PRANAV SANTOSH'),
    (35, 220001036, 'KAMBAM SAI RUCHITHA'),
    (36, 220001037, 'KANAK NAGAR'),
    (37, 220001038, 'KAPUGANTY VENKATA SATYA TEJA'),
    (38, 220001039, 'KARAN JALINDAR JADHAV'),
    (39, 220001040, 'KODUDULA NIKETH REDDY'),
    (40, 220001041, 'KONETI TEJASWINI'),
    (41, 220001042, 'LALIT'),
    (42, 220001043, 'MADAN P'),
    (43, 220001044, 'MALLAVARAPU SAI VARSHITH'),
    (44, 220001045, 'MISHA JAIN'),
    (45, 220001046, 'MUDE ANKITHA'),
    (46, 220001047, 'MUDE HEMA DEEPIKA'),
    (47, 220001048, 'MUSKAN'),
    (48, 220001049, 'NAREN KUMAR SAI KAJA'),
    (49, 220001050, 'NEERUPAM'),
    (50, 220001051, 'NIKITA SANJAY TAYADE'),
    (51, 220001052, 'P C UMA MAHESH'),
    (52, 220001053, 'PANCHANGAM AKHILESH'),
    (53, 220001054, 'PANTHAM RAJA KRISHNA'),
    (54, 220001055, 'PAPPALA TEJASWINI'),
    (55, 220001056, 'PARAM BANSAL'),
    (56, 220001057, 'PARTH SHARADRAO DESHMUKH'),
    (57, 220001058, 'PRADEEP KUMAR REBBAVARAPU'),
    (58, 220001059, 'PRANJAY CHOUHAN'),
    (59, 220001060, 'PRATHAM GUPTA'),
    (60, 220001061, 'PRINCE KUMAR GUPTA'),
    (61, 220001062, 'PRIYANSH VERMA'),
    (62, 220001063, 'RISHI BHARAT JUNGHARE'),
    (63, 220001064, 'S RUTHVIK'),
    (64, 220001065, 'SAI SANJANA REDDY ALGUBELLY'),
    (65, 220001066, 'SAKET MESHRAM'),
    (66, 220001067, 'SAKET PRASHANT THAMKE'),
    (67, 220001068, 'SAMYAK DHYANI'),
    (68, 220001069, 'SANJEET KUMAR'),
    (69, 220001070, 'SARTHAK BRAR'),
    (70, 220001071, 'SATYA NARAYAN'),
    (71, 220001073, 'SHAIK SUHANA'),
    (72, 220001074, 'SHAURYA KSHITIJ KHETARPAL'),
    (73, 220001075, 'SHIVRAJ RATHORE'),
    (74, 220001076, 'SIDDHESH NITIN WAJE'),
    (75, 220001077, 'VASHISTHA NARAYAN CHATURVEDI'),
    (76, 220001078, 'VEDANT DINKAR'),
    (77, 220001079, 'VIJIT BALSORI'),
    (78, 220001080, 'VINEET VERMA'),
    (79, 220001081, 'VOTTE SRIYANS REDDY'),
    (80, 220001082, 'YANNAM YESWANTH REDDY'),
    (81, 220002018, 'ARNAV NIRMAL JAIN'),
    (82, 220002029, 'BORRA GNANA VENKATA SHIVA'),
    (83, 220002063, 'PRASAD AKANKSHA'),
    (84, 220002081, 'VEDANT UPADHYAY')
]

# Inserting Students
stu={"Type": "list", "Class": "CS203", "Data": student_data}
db[user].insert_one(stu)
stud=db[user].find_one({"Type": "list", "Class": "CS203"})

print(len(stud["Data"]))


# Checking Attendance
da={"Type": "data", "Date": datetime.datetime.now(), "Class": "CS203", "Data": "01011101110111111011011111101101"}
db[user].insert_one(da)

prof=db[user].find_one({"Type": "data", "Class": "CS203"})

index=4 #AK
present='1'==(prof["Data"])[index]
print(present)

bul = {True: 1, False: 0}

for i in stud["Data"]:
    try: 
        print(i[2]+" was "+["absent.", "present."][bul['1'==(prof["Data"])[i[0]]]])
    except:
        print(i[2]+" was "+"absent.")


# Changing normal attendance to Binary String:
'''final = []
for face in faces:
    max_score=0.35
    max_roll=0
    for roll in base_embeddings:
        for e1 in base_embeddings[roll]:
            score = compareEmbedding(e1,face['embedding'])
            if max_score<score:
                max_score = score
                max_roll = roll

    if(max_roll!=0):
        final.append(max_roll)
        

final = set(final)
att=""
for i in range(len(stud["Data"])):
    if stud["Data"][1] in final:
        att+="1"
    else:
        att+="0"

da={"Type": "data", "Date": datetime.datetime.now(), "Class": "CS203", "Data": att}
db[user].insert_one(da)
        
# print(file.filename, ":")
# print(final)
output = output.union(final)'''
