import requests, json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib.request
from urllib.request import urlopen
from urllib.request import urlretrieve

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

listID = input("Enter List ID: ")

webInfo = {

    'Id': listID,
    'x-imdb-parent-id': '????',
    'Referer': 'https://www.imdb.com/list/' + listID + '/edit?inProgress=true',
    'Cookie': '?????',
    'Data': '????=????'
}

def addItemByTitleYear(title, year, itemType):

    if itemType == "movies:

        itemType = "feature"

    elif itemType == "tvSeries":

        itemType = "TV series"

    year = year.replace("(","").replace(")","")

    searchTitle = title.replace(" ","_") 

    url = 'https://v2.sg.media-imdb.com/suggestion/titles/' + searchTitle[0].lower() + '/' + searchTitle + '.json'

    r = requests.get(url, verify=False)

    results = []

    try:

        for movie in r.json()['d']:

            try:

                results.append([movie['l'],str(movie['y'])])

                if (movie['l'].lower() == title.lower()) and (movie['q'].lower() == itemType.lower()) and ((str(movie['y']) == str(year)) or (str(movie['y']) == str(int(year)-1))):
                    
                    headers = {

                        'Host': 'www.imdb.com',
                        'Connection': 'keep-alive',
                        'Content-Length': '10',
                        'Origin': 'https://www.imdb.com',
                        'x-imdb-parent-id': webInfo['x-imdb-parent-id'],
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Accept': '*/*',
                        'Sec-Fetch-Site': 'same-origin',
                        'Sec-Fetch-Mode': 'cors',
                        'Referer': webInfo['Referer'],
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'en-US,en;q=0.9',
                        'Cookie': webInfo['Cookie']
                        }

                    r = requests.post('https://www.imdb.com/list/' + webInfo['Id'] + '/' + movie['id'] + '/add', headers=headers, data=webInfo['Data'], verify=False)

                    print("Added:",title," - ",year)

                    return

            except:
                pass

        print("Missing: ",title," - ",year)

    except:
        print("Missing: ",title," - ",year)


def addItemByID(itemID):

    try:
            
        headers = {

            'Host': 'www.imdb.com',
            'Connection': 'keep-alive',
            'Content-Length': '10',
            'Origin': 'https://www.imdb.com',
            'x-imdb-parent-id': webInfo['x-imdb-parent-id'],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Referer': webInfo['Referer'],
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cookie': webInfo['Cookie']
            }

        r = requests.post('https://www.imdb.com/list/' + webInfo['Id'] + '/' + itemID + '/add', headers=headers, data=webInfo['Data'], verify=False)

        if r.status_code == 200:
            print("Added:",itemID)
        else:
            print("Failed: ",itemID)

        return

    except:
        print("Failed: ",itemID)
        pass

def getLocalListWithIDs(file):
    
    itemList = []

    f = open(file,"r", encoding="utf-8")

    data = f.readlines()

    for line in data:

        line = line.replace('\n',"")

        line = line.strip()

        itemList.append(line)

    return itemList

def getLocalListWithTitleYears(file,itemType):
    
    itemList = []

    f = open(file,"r", encoding="utf-8")

    data = f.readlines()

    for line in data:

        line = line.replace('\n',"")

        tmpLine = line.split()

        tmpYear = tmpLine[len(tmpLine)-1]

        line = line.replace(tmpYear,"")

        line = line.strip()

        itemList.append([line, tmpYear,itemType])

    return itemList

def addListByIDs(listData):

    for item in listData:

        try:

            addItemByID(item)

        except:
            pass

def addListByTitleYear(listData):

    for item in listData:

        try:

            addItemByTitleYear(item[0], item[1], item[2])

        except:
            pass


addListByIDs(getLocalListWithIDs("list.txt"))

t = input("")
