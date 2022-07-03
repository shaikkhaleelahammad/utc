import requests
import json

def getTimezoneJson(file_url):
    try:
        file_stream = requests.get(file_url,stream=True)
        with open('timezones.json', 'wb') as tz_json:
            for data in file_stream:
                tz_json.write(data)
        print("downloaded the timezone")
    except Exception as e:
        print(f"Excecption is downloading the Timezone json file ${e}")

def readJson(filepath):
    try:
        jsonFile = open(filepath, 'r')
        data = json.load(jsonFile)
        return data
    except Exception as e:
        print(f"Exception is loading the json file ${e}")

def getMatch(jsondata,requiredValue):
    try:
        timezoneText = None
        for timeZone in jsondata:
            if requiredValue in timeZone["value"]:
                #print(f"timezone of ${requiredValue} is ${requiredValue[\"text\"]} ")
                timezoneText = str(timeZone['text'])
                break
        return timezoneText
    except Exception as e:
        print(f"Exception in getting the value ${e}")

def getOffset(jsondata,requiredValue):
    try:
        timezoneText = None
        for timeZone in jsondata:
            if float(requiredValue) == timeZone["offset"]:
                timezoneText = str(timeZone['text'])
                break
        return timezoneText
    except Exception as e:
        print(f"Exception in getting the value ${e}")

def main():
    try:
        file_url = "https://raw.githubusercontent.com/dmfilipenko/timezones.json/master/timezones.json"
        getTimezoneJson(file_url)
        jsondata = readJson("timezones.json")
        if jsondata is not None:
            for timeZone in jsondata:
                print(timeZone)
        else:
            print("input dataset is empty")
            exit(1)
        timezoneValue = getMatch(jsondata,"UTC-11")
        print(f"timezoneText ${timezoneValue}")
        timezoneValue = getOffset(jsondata,"5.5")
        print(f"timezoneText ${timezoneValue}")

    except Exception as e:
        print(f"unable to process Timezone ")


main()
