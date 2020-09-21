import requests
import pandas
import json
import time
import random

baseURL = 'https://m.land.naver.com/complex/ajax/complexListByCortarNo?cortarNo='
HEAD = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) \
        AppleWebKit 537.36 (KHTML, like Gecko) Chrome"
}

def getCortarNums():
    with open('../dataCSV/rawCSV/cortarNum.txt', 'r') as f:
        cortarNums = f.read()
        cortarNums = cortarNums.split('\n')
    return cortarNums

def getJson(cortarNo):
    url = baseURL + cortarNo
    result = requests.request("GET", url, headers=HEAD)
    info = json.loads(result.text)
    return info

def writeHscps(hscps):
    for hscp in hscps:
        hscpType = hscp['hscpTypeNm']
        with open('../dataCSV/rawCSV/hscpNo_' + hscpType + '.txt', 'a+') as f:
            f.write(hscp['hscpNo'] + '\n')

if __name__ == '__main__':
    cortarNums = getCortarNums()
    sum = 0

    for idx, cortarNo in enumerate(cortarNums):


        info = getJson(cortarNo)
        hscps = info['result']

        sum += len(hscps)
        writeHscps(hscps)

        print(f'진행률: {idx+1}/{len(cortarNums)} 누적 단지 수: {sum}')
        time.sleep(random.randint(5, 12))
