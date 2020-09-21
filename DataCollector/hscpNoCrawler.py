import requests
import json
import time
import random

baseURL = 'https://m.land.naver.com/complex/ajax/complexListByCortarNo?cortarNo='
HEAD = {
        'User-Agent': "PostmanRuntime/7.20.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "adbba748-cb85-4fb4-8f6a-4be441f19cc3",
        'Host': "m.land.naver.com",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

def getCortarNums():
    f = open('../dataCSV/rawCSV/cortarNum.txt', 'r')
    cortarNums = f.read()
    cortarNums = cortarNums.split('\n')
    f.close()
    return cortarNums

def getJson(cortarNo):
    url = baseURL + cortarNo
    result = requests.request("GET", url, headers=HEAD)
    info = json.loads(result.text)
    return info

def writeHscps(f, hscps):
    for hscp in hscps:
        f.write(hscp['hscpNo'] + '\n')

if __name__ == '__main__':
    cortarNums = getCortarNums()
    sum = 0

    for idx, cortarNo in enumerate(cortarNums):
        f = open('../dataCSV/rawCSV/hscpNo1.txt', 'a+')

        info = getJson(cortarNo)
        hscps = info['result']

        sum += len(hscps)
        writeHscps(f, hscps)
        f.close()

        print(f'진행률: {idx+1}/{len(cortarNums)} 누적 단지 수: {sum}')
        time.sleep(random.randint(5, 12))
