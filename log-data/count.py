import csv ,copy
import datetime as dt
import locale

csv_file = open("./log-data-hours3.csv", "r")
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

data_list = list()

yobiList =["日","月","火","水","木","金","土"]
# localeモジュールで時間のロケールを'ja_JP.UTF-8'に変更する
locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
data = {}
initData = {}
dataYobi = {}
for i in range(24):
    initData.update({(i,0)})

for yobiKKK in yobiList:
    dataYobi.update({yobiKKK:copy.deepcopy(initData)})

#print(dataYobi)    

yobiCount = 0

for fin in f:
    time = fin[0]
    count = int(fin[1])
    spTime = time.split(" ")
    year = int(spTime[0].split("-")[0])
    month = int(spTime[0].split("-")[1])
    day = int(spTime[0].split("-")[2])
    hour = int(spTime[1].split(":")[0])
    date = dt.date(year, month, day)
    yobi = date.strftime('%a')
    # yobi = yobiList[yobiCount]
    if hour + 9 < 24:
        hour += 9
    else:
        hour = (hour + 9) - 24
        
        
    if count > 400:
        print(f"{year}-{month}-{day} {hour}時  count : {count}")
    else:
    
        countBefore = dataYobi[yobi][hour]
        count += countBefore
        
        dataYobi[yobi].update({(hour,count)})
        
        if hour == 23:
            
            yobiCount += 1
            if yobiCount == 7:
                yobiCount = 0

print(dataYobi)

for yobiKobetu in yobiList:
    for k,v in dataYobi[yobiKobetu].items():
        t = list()
        t.append(k)
        t.append(v)
        with open('log-sp-dataV5.csv', 'a') as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerow(t)