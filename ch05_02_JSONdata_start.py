#
# Learning in Tamil - Python 
# Example file - JSON
# 

from urllib.request import Request, urlopen
from urllib.error import URLError

def main():
    # open a URL connection 
    #http://httpstat.us/500
    #https://www.python.org/
    url = "http://httpstat.us/500"
    request = Request(url)
    try:
        response = urlopen(request)
        # read HTML Data
        htmldata = response.read()
        print (htmldata)
        
        # response code 
        responseCode = response.getcode()
        print ("response code: ", responseCode)
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
