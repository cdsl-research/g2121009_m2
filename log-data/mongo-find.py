from unittest import IsolatedAsyncioTestCase
import pymongo
from datetime import datetime
import csv
import matplotlib.pyplot as plt
from dateutil.relativedelta import relativedelta
import re

count = 0

data = []

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["access_log"]

my_collection = db["new-cdsl"]

"""
mouth = ['Aug/2021', 'Sep/2021', 'Oct/2021', 'Nov/2021', 'Dec/2021', 'Jan/2022', 'Feb/2022', 'Mar/2022', 'Apr/2022', 'May/2022', 'Jun/2022']

for m in range(len(mouth)):
    for i in range(1, 32):
        if i < 10:
            results = my_collection.find(filter={'time':{'$regex':'0'+str(i)+'/'+mouth[m]}})
            count = len(list(results))
            data.append(count)
        else:
            results = my_collection.find(filter={'time':{'$regex':str(i)+'/'+mouth[m]}})
            count = len(list(results))
            data.append(count)
"""

date_from = datetime(2021, 8, 1)
date_to = datetime(2021, 9, 1)

"""
for i in range(1, 12):
    date_to = date_from + relativedelta(months=1)
    data = my_collection.find({"time":{"$gte":date_from, "$lte":date_to}})
    
    with open("log-data-mouth.csv", 'a') as file:
        print(date_from,'~', date_to, len(list(data)), file=file)

    date_from = date_to
"""

for i in range(11):
    #for n in range(31):
        #for t in range(24):
            data = my_collection.find({
                "time":{"$gte":date_from, "$lte":date_to},  
                "path": {"$not":re.compile("^(?=.*xmlrpc).*$") }
                # {"path": {"$not":{"regex":".*xmlrpc\.php.*" }}}
                })
            
            with open("log-data-months3.csv", 'a') as file:
                print(date_from,'~', date_to, len(list(data)), file=file)
                date_from = date_from + relativedelta(months=1)
                date_to = date_to + relativedelta(months=1)



#plt.plot(data)
#plt.savefig("access-log.png")

'''
for i in range(1, 32):
    results = my_collection.find(filter={'time':{'$regex':str(i)+'/Apr/2021'}})
    count = len(list(results))
    print(count)
'''
'''
results = my_collection.find(filter={'time':{'$regex':'01/Apr/2021'}})
print(len(list(results)))
'''
#print(list(my_collection.find({}, {"_id": 0,"time":1})))