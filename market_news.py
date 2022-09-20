import requests
import json
from datetime import datetime, timedelta

results = {"item": {}}

try:
    f = open("market_news.json", "r")
    data2 = json.load(f)
    date = data2["item"][0]["published"]
    date_from = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
except:
    data2 = {"item": []}
    date_from = datetime(2021, 12, 31)  # <change to select days // Year-Month-Day
date_to = datetime.today()  # <change to select days // Year-Month-Day
# date_to=datetime(2022, 9, 1)
timestamp_from = int(datetime.timestamp(date_from)) * 1000
timestamp_to = int(datetime.timestamp(date_to)) * 1000

number_wanted = 11000
copy = None
lowstday = date_to

running = True
while running == True:

    URL = f"https://api.news.eu.nasdaq.com/news/query.action?type=json&showAttachments=true&showCnsSpecific=true&showCompany=true&countResults=false&freeText=&company=&market=Main%20Market,+Helsinki&cnscategory=&fromDate={timestamp_from}&toDate={timestamp_to}&globalGroup=exchangeNotice&globalName=NordicMainMarkets&displayLanguage=en&language=&timeZone=CET&dateMask=yyyy-MM-dd+HH%3Amm%3Ass&limit={2000}&start=0&dir=DESC"

    r = requests.get(url=URL)
    data = r.json()

    if data["results"]["item"] != {}:
        for i in range(0, len(data["results"]["item"])):
            if number_wanted <= 0:
                running = False
                continue
            entry = data["results"]["item"][i]
            if entry["headline"] not in results["item"]:
                number_wanted -= 1
                headline = entry["headline"]
                results["item"][headline] = {"company": entry["company"], "messageUrl": entry["messageUrl"],
                                             "published": entry["published"], "headline": headline}
                print(entry["published"])
                # print(results)
                if datetime.strptime(entry["published"], '%Y-%m-%d %H:%M:%S') < lowstday:
                    lowstday = datetime.strptime(entry["published"], '%Y-%m-%d %H:%M:%S')

    if lowstday == copy:
        running = False
    else:
        copy = lowstday

    timestamp_to = int(datetime.timestamp(lowstday)) * 1000

new_list = []
print(data)
for x in results["item"].keys():
    new_list.append(results["item"][x])
for x in data2["item"]:
    new_list.append(x)
data2 = {"item": new_list}

with open("market_news5550.json", "w") as outfile:
    json_object = json.dumps(data2, indent=4)
    outfile.write(json_object)