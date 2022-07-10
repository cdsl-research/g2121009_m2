import pymongo
from asyncore import write
from cmath import log
from email import header
import json
from re import X
import csv
from sqlite3 import Date
import glob

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["access_log"]

my_collection = db["cdsl"]


files = glob.glob("./ito2/var.log.nginx.access.wp.log/*")
for file in files:
    print(file)
    
    with open(file) as f: 
        line = f.read().splitlines()
        
        for i in line:
            log_data = json.loads(i)
            log_agent = log_data['agent']
            
            
                #year = log_data['time'][7:11]
                #date = log_data['time'][0:6]
                #time = log_data['time'][12:20]
                print(log_data)
        
                data = log_data
        
                my_collection.insert_one(data)