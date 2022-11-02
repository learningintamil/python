#
# Learning in Tamil - Python 
# Example file - JSON Data
# 

from urllib.request import Request, urlopen
from urllib.error import URLError
import json

def printExcangeRateDetails(JSONObj):
    print("USD <=>", JSONObj["code"], "conversion:")
    for key in JSONObj:
        value = JSONObj[key]
        print("  {} = {}".format(key, value))

def processResults(jsonStringData):
    jsonData = json.loads(jsonStringData)
    print(jsonData["inr"])
    print(jsonData["inr"]["rate"])
    for key in jsonData:
        value = jsonData[key]
        #print("The key and value are:\n{} : {}".format(key, value))
        if (value["rate"] < 1):
            print(value["code"]+ " : " + str(value["rate"]))
            printExcangeRateDetails(value)

def main():
    # open a URL connection 
    #http://httpstat.us/500
    #https://www.python.org/
    url = "http://www.floatrates.com/daily/usd.json"
    request = Request(url)
    try:
        response = urlopen(request)
        # read HTML Data
        htmldata = response.read()
        print (htmldata)
        
        # response code 
        responseCode = response.getcode()
        print ("response code: ", responseCode)
        if (responseCode == 200):
            jsonStringData = htmldata.decode("utf-8")
            processResults(jsonStringData)
    except URLError as e:
        #print('Reason: ', e.reason)
        #print(dir(e))
        if hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
            print('Reason: ', e.reason)
        elif hasattr(e, 'reason'):
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
 
if __name__ == "__main__":
    main()
