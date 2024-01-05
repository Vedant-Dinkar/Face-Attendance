from fastapi import FastAPI, File, UploadFile, Form, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2AuthorizationCodeBearer
import logging
import numpy as np
import cv2
from PIL import Image
from mtcnn import MTCNN
import insightface
import math
import pickle
import motor
from motor import motor_asyncio
import json
from pymongo import MongoClient
import csv
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
import datetime
import httpx
from typing import List
from fastapi import Form
from fastapi import File, UploadFile, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import random


app = FastAPI()

class Item(BaseModel):
    data: list

# # OAuth2 config
# oauth2_scheme = OAuth2AuthorizationCodeBearer(
#     tokenUrl="token",
#     authorizationUrl="login",
# )

try:
    ct = MongoClient("mongodb://localhost:27017/")
    database = ct["Attendance_Face"]
    print("Connected to MongoDB successfully")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")


oauth2_scheme = OAuth2AuthorizationCodeBearer(tokenUrl="token", authorizationUrl="login")

model = insightface.app.FaceAnalysis(name="buffalo_l")
model.prepare(ctx_id=-1)

client = MongoClient('localhost', 27017)

db = client.get_database("FaceAttendance")

log = db.get_collection("LogXY")

user="Vedant"
user1="Vedant"
password="IMPOM"

students = {
    190001060: 'SURENDAR KETHAVATH',
    220001001: 'AADISH JAIN',
    220001002: 'ABHINAV GANGIL',
    220001003: 'ADITI ASHISH WEKHANDE',
    220001004: 'ADITYA KSHITIZ',
    220001005: 'ADITYA SACHIN MASTUD',
    220001006: 'ADITYA YADAV',
    220001007: 'AMAN PRATAP SINGH',
    220001008: 'AMIT TIWARI',
    220001009: 'ANIRUDH GAUTAM',
    220001010: 'ANNAMSHETTI SUMANTH',
    220001011: 'ARAVAPALLI PAVAN KUMAR',
    220001012: 'ATHARVA ANIL SANGAWAR',
    220001013: 'ATHARVA NANOTI',
    220001014: 'AVIRAL SHARMA',
    220001015: 'AYITHA TRIBUVAN',
    220001016: 'BALABHADRA RITHVIK',
    220001017: 'BHARAT KAURAV',
    220001018: 'BHAVANAM SAI PAVAN KUMAR REDDY',
    220001019: 'BHUKYA HAVISH',
    220001020: 'CHANDEKAR RIDDHI UMESH',
    220001021: 'CHERUPALLY VINAY',
    220001022: 'CHIRANJIVI KESHAV',
    220001023: 'DARBHA KALYANA SRIRAM',
    220001024: 'DARSHIL PATEL',
    220001025: 'DEBASISH PADHY',
    220001026: 'DEEPAK YADAV',
    220001027: 'DEVANSHI CHHATBAR',
    220001028: 'EDULA BHOOMIKA',
    220001029: 'GARIMA UPADHYAY',
    220001031: 'GUNTUKU RISHWANTH SAI',
    220001032: 'HITESH MAURYA',
    220001033: 'JAY SOLANKI',
    220001034: 'JONNALAGADDA SAI PRANAY DEEP',
    220001035: 'KALWAGHE PRANAV SANTOSH',
    220001036: 'KAMBAM SAI RUCHITHA',
    220001037: 'KANAK NAGAR',
    220001038: 'KAPUGANTY VENKATA SATYA TEJA',
    220001039: 'KARAN JALINDAR JADHAV',
    220001040: 'KODUDULA NIKETH REDDY',
    220001041: 'KONETI TEJASWINI',
    220001042: 'LALIT',
    220001043: 'MADAN P',
    220001044: 'MALLAVARAPU SAI VARSHITH',
    220001045: 'MISHA JAIN',
    220001046: 'MUDE ANKITHA',
    220001047: 'MUDE HEMA DEEPIKA',
    220001048: 'MUSKAN',
    220001049: 'NAREN KUMAR SAI KAJA',
    220001050: 'NEERUPAM',
    220001051: 'NIKITA SANJAY TAYADE',
    220001052: 'P C UMA MAHESH',
    220001053: 'PANCHANGAM AKHILESH',
    220001054: 'PANTHAM RAJA KRISHNA',
    220001055: 'PAPPALA TEJASWINI',
    220001056: 'PARAM BANSAL',
    220001057: 'PARTH SHARADRAO DESHMUKH',
    220001058: 'PRADEEP KUMAR REBBAVARAPU',
    220001059: 'PRANJAY CHOUHAN',
    220001060: 'PRATHAM GUPTA',
    220001061: 'PRINCE KUMAR GUPTA',
    220001062: 'PRIYANSH VERMA',
    220001063: 'RISHI BHARAT JUNGHARE',
    220001064: 'S RUTHVIK',
    220001065: 'SAI SANJANA REDDY ALGUBELLY',
    220001066: 'SAKET MESHRAM',
    220001067: 'SAKET PRASHANT THAMKE',
    220001068: 'SAMYAK DHYANI',
    220001069: 'SANJEET KUMAR',
    220001070: 'SARTHAK BRAR',
    220001071: 'SATYA NARAYAN',
    220001073: 'SHAIK SUHANA',
    220001074: 'SHAURYA KSHITIJ KHETARPAL',
    220001075: 'SHIVRAJ RATHORE',
    220001076: 'SIDDHESH NITIN WAJE',
    220001077: 'VASHISTHA NARAYAN CHATURVEDI',
    220001078: 'VEDANT DINKAR',
    220001079: 'VIJIT BALSORI',
    220001080: 'VINEET VERMA',
    220001081: 'VOTTE SRIYANS REDDY',
    220001082: 'YANNAM YESWANTH REDDY',
    220002018: 'ARNAV NIRMAL JAIN',
    220002029: 'BORRA GNANA VENKATA SHIVA',
    220002063: 'PRASAD AKANKSHA',
    220002081: 'VEDANT UPADHYAY'
}

from sklearn.metrics.pairwise import cosine_similarity
def compare(address1,address2):
    img1 = cv2.imread(address1)
    img2 = cv2.imread(address2)
    e1 = model.get(img1)[0]['embedding']
    e1 = e1/np.linalg.norm(e1)
    e2 = model.get(img2)[0]['embedding']
    e2 = e2/np.linalg.norm(e2) 
    return cosine_similarity([e1], [e2])[0][0]

def compareEmbedding(e1,e2):
    e1 = e1/np.linalg.norm(e1)
    e2 = e2/np.linalg.norm(e2) 
    return cosine_similarity([e1], [e2])[0][0]

def draw_bounding_boxes(image, coordinates):
    for coord in coordinates:
        x1, y1, x2, y2 = math.floor(coord['bbox'][0]), math.floor(coord['bbox'][1]), math.floor(coord['bbox'][2]), math.floor(coord['bbox'][3])
        color = (0, 255, 0)
        thickness = 1
        image = cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)
    return image

logging.basicConfig(
    level=logging.DEBUG,  # You can adjust the log level as needed (e.g., INFO, WARNING, ERROR)
    filename='fastapi.log',  # Log to a file
    filemode='a',  # Append to the log file
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    user="Vedant"
    password="BOMPOM"

    log = db.get_collection("LogXY")
    
    existing_profile = log.find_one({"Name": user, "Password": password})
    if existing_profile:
        return {"message": "Success!"}
    else:
        exist=log.find_one({"Name": user})
        if exist:
            return {"message": "Error! Username Exists! Hello World data_collection = dab[user]"+user}
        else:
            aadmi=db.get_collection("LogXY")
            mydict = { "Created": datetime.datetime.now()}
            db[user].insert_one(mydict)
    return {"message": "Hello "+user}

@app.post("/uploadfiles")
async def create_upload_files(files: List[UploadFile]):
    f = open("./final-attendance.csv", 'w')
    f.close()

    with open("./attendance_embeddings.pkl", 'rb') as file:
        base_embeddings = pickle.load(file)

    output = set()
    for file in files:
        photo = await file.read()
        nparr = np.fromstring(photo, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        faces = model.get(img)
        # print(faces)
        # img = draw_bounding_boxes(img, faces)
        # img = Image.fromarray(img)
        # print("hi")
        # img.save("./image.png")

        final = []
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
        # print(file.filename, ":")
        # print(final)
        output = output.union(final)

    output = list(output)
    output.sort()
 
    stud=db[user].find_one({"Type": "list", "Class": "CS203"})
    att=""
    for i in range(len(stud["Data"])):
        if str(stud["Data"][i][1]) in output:
            att+="1"
        else:
            att+="0"

    da={"Type": "data", "Date": str(datetime.datetime.now())[:10], "Class": "CS203", "Data": att}
    db[user].insert_one(da)

    with open("./final-attendance.csv", 'w+') as f: 
        for roll in output:
            f.write(str(roll)+","+students[int(roll)]+"\n")
        f.seek(0)

    # print(output)
    return {"present": output}
    # return FileResponse('./final-attendance.csv', filename='final-attendance.csv')
    
@app.get("/exportcsv")
async def export_csv():
    return FileResponse("./final-attendance"+".csv", filename='final-attendance.csv')

@app.post("llogin")
async def login(credentials: dict):
    username = credentials.get("username")
    password = credentials.get("password")

    user = log.find_one({"username": username, "password": password})

    if user:
        print("Good!")
        return {"message": "Login successful"}
    
    print("Bad!")    
    return {"message": "Login unsuccessfull"}

@app.post("/login")
async def login(id_token: str):
    print("Received token:", id_token)

    google_response = await httpx.get(
        f"https://www.googleapis.com/oauth2/v3/tokeninfo?id_token={id_token}"
    )

    print("Google response:", google_response.text)

    google_data = google_response.json()

    if "error_description" in google_data:
        raise HTTPException(status_code=401, detail="Invalid token")

    user_email = google_data["email"]
    return {"message": "Login successful", "user_email": user_email}

@app.get("/protected")
async def protected_route(token: str = Depends(oauth2_scheme)):
    # Access token is valid, handle protected route logic
    pass

@app.get("/courses")
async def course():
    kaksha="CS203"
    stud=db[user].find_one({"Type": "list", "Class": kaksha})
    bacche=[]
    for i in stud["Data"]:
        bacche.append((i[2], i[1]))

    print(bacche)
    return {"stulist": bacche}

@app.post("/cours")
async def cours(
    files: List[UploadFile] = File(...),
    rollNumbers: List[str] = Form(...),
):
    for roll, file in zip(rollNumbers, files):
        contents = await file.read()
        filename = f"{roll}_{file.filename}"
        with open(filename, "wb") as f:
            f.write(contents)
    
    print(rollNumbers)

    return {"message": "Files received successfully", "rollNumbers": rollNumbers}

@app.post("/log")
async def addUser():
    para

@app.get("/callback")
async def call():
    return {"message": "80085!"}