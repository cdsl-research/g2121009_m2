from asyncore import write
from cmath import log
from email import header
import json
from re import X
import csv
from sqlite3 import Date
import glob
from time import strptime
import datetime
from datetime import date
import pymongo

count = 0

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["access_log"]

my_collection = db["new2-cdsl"]

files = glob.glob("./ito2/var.log.nginx.access.wp.log/*")
for file in files:
    print(file)
    new_line = []
    
    with open(file) as f: 
        line = f.read().splitlines()
        
        for i in line:
            log_data = json.loads(i)
            log_newdata = log_data
            log_agent = log_data["agent"]
            log_time = log_data["time"]
            log_path = log_data["path"]
            dat = datetime.datetime.strptime(log_time, '%d/%b/%Y:%H:%M:%S %z')
            log_newdata["time"] = dat
            
            if 'bot' not in log_agent and 'WordPress' not in log_agent and 'Automate' not in log_agent and 'xmlrpc.php' not in log_path:
                my_collection.insert_one(log_newdata)

            #if 'bot' not in log_agent and 'WordPress' not in log_agent:
                #year = log_data['time'][7:11]
                #date = log_data['time'][0:6]
                #time = log_data['time'][12:20]
                #print(log_data)
        
        """
        with open('./'+year+'.csv','a', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(date)
            print(time, file=file)
        """