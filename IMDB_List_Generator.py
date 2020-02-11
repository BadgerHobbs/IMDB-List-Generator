import requests, json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib.request
from urllib.request import urlopen
from urllib.request import urlretrieve

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

listID = input("Enter List ID: ")

webInfo = {

    'Id': listID,
    'x-imdb-parent-id': 'VCG3P7ECZDJ8FM43NXZC',
    'Referer': 'https://www.imdb.com/list/' + listID + '/edit?inProgress=true',
    'Cookie': 'session-id=146-9994463-1300849; ubid-main=132-5393080-8888646; adblk=adblk_yes; x-main="i2qE6E@EK4A3OCx1RGzbNw5OQHEJ2Zsmn?6kotECDlfEQuzOzNG33np8le1pqcvb"; at-main=Atza|IwEBIMyaDc_2mKxpe6I_4nHl-hpbsE3B-7UypCcCww_TKXTsORs5Bduso4-lJ7ZUy6qgFdEEshmS2Cm7kOqoI7qA3jg2HIEXp8wL0szmrQ7QrLxgFyamSI513a0fIUippjFbo-Uvf_yJpByZFgjMa_cpdHP19DlTb7bwfc7OzwOk3fbgkZL3RQI2WYTAldH3QDKWa0-qJRsJEyiMzfb0RmdXh4sWbH2VG4iITOC4lA0XOaimS56Sizqmab_cgOw3LNxvXWfRooQB5mQY8t_hFcLAStyVYz6uonCtNIqSyDF5sKGL34BvNLxTbhN7MDxIjcQh6Qozyr9uEKBcDIjcAPLz14FvALVlkLV9iwL9R6XwX3j8kPfaXk3YG9H1X4HOeEdj8sx1_MSH0_T8aXT1lfUwzdwC; sess-at-main="ksn3tObY6xcfarA5wMelfTYunHVlheCPDjRuZWaES0I="; id=BCYkxOLtp_sPENF26QSKyVeRYibvi4h7SQBx3zHlCAijYDOOvh9pRaIIW3_CfRLEVzHpGBLdiy8_%0D%0AWUud1bS-GA8gIXgtq7nzv8p2rs7vGl1T2fko1iR6FP8KwIHNw4jzXhmcaYZs3aJ-l5KecZNGbFiv%0D%0A7g%0D%0A; uu=BCYvWpz6s5_lDtDVvP0x5V8XRDjzpe4e8XOB_5UMtx7gM2KjFV51JYCtEN_5h-K0rDE7T7ama6if%0D%0ApI-cknUaeTCuKxIHmDK0Cf9K7bZJKFagngdzjBGipmsIYHsfjaJl8jjd9x2QkuubZK6e2ZR5zs2i%0D%0AM9p11JQdqwYpOEOvOttOD_-Bl4DmsMy7R5bR4NNhTvMCBjMUugN9rvKXmAp7M-M89J3zwxzgbBqT%0D%0AVdz1Xzuf80VyurmN_F8tMTxfhMzTSjbOUm6_Zh1BsHUTKB8uFtHD3mIJNiV4Tw2q_ib2TWPvz60%0D%0A; sid=BCYssQZexcWAziphd46uAQs1mV6nFGs_arvCLsKyvAVnfIlk2QabWFfovVcHD4WO2RZ3U6VlGHvn%0D%0Azj0UvrGm4xQILK7zMH3Ky2kG0ENuv-gyZDlMbc6_CT_o3ZJ--gsADOTcvdlRZ5k7fp_uZH7YKlYZ%0D%0Afw%0D%0A; session-id-time=2082787201l; pa=BCYp6BtxqYuzJvutDdA9MsRI9VZvHdg1Z5BU2_muJepjmqEEX4Y9Lm1eyPXMmjq95V-Kea-ZtfPq%0D%0AW6NMyYBlZj4dOr26UBcIegxY7EqZkxDLbCb6alLzVwlds-hZ_VOYWEWC%0D%0A; session-token=PlMQwunKUWaXDq06edtmCrrmx7XCUP96byWEUESh9n9SsLGEYQrhxwtVHEcJnOcJa4FfcHHza08eaizNqTWocMixdNUISDmZORxeGUtVUN2DzCWdyztNZAq3oDY3bvE0sIddNZzORvqeyW3ys2tn57S7fZhWTfUsWOqc4imGeDxPfEZpmCPdJ8ksAb45kdxQ7mtvrWF0CA7cSv29z4RpxSqL0XQIbTUMRrxHe31xD2E=; csm-hit=tb:TW2DFPRY163PD7MYFVMH+s-VCG3P7ECZDJ8FM43NXZC|1581461936325&adb:adblk_yes&t:1581461936325',
    'Data': '49e6c=e3c2'
}

def addItemByTitleYear(title, year, itemType):

    if itemType == "movie":

        itemType = "feature"

    elif itemType == "tvSeries":

        itemType = "TV series"

    searchTitle = title.replace(" ","_") 

    url = 'https://v2.sg.media-imdb.com/suggestion/titles/' + searchTitle[0].lower() + '/' + searchTitle + '.json'

    r = requests.get(url, verify=False)

    results = []

    try:

        for movie in r.json()['d']:

            try:

                results.append([movie['l'],str(movie['y'])])

                if (movie['l'] == title) and (movie['q'] == itemType) and ((str(movie['y']) == str(year)) or (str(movie['y']) == str(int(year)-1))):
                    
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

        addItemByID(item)

def addListByTitleYear(listData):

    for item in listData:

        addItemByTitleYear(item[0], item[1], item[2])


addListByIDs(getLocalListWithIDs("list.txt"))

t = input("")