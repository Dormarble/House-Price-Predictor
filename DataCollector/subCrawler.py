import requests
import random 
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
import os
from os.path import dirname
import time
from pathlib import Path

rawCsvFileDiv = dirname(dirname(os.path.realpath(__file__))) + '/dataCSV/rawCSV/'
targetFileDiv = dirname(dirname(os.path.realpath(__file__))) + '/dataCSV/addtionalCSV/'

csvFiles = [
    '중랑구.csv',
    '중구.csv',
    '종로구.csv',
    '은평구.csv',
    '용산구.csv',
    '영등포구.csv',
    '양천구.csv',
    '송파구.csv'
]

MIN_SLEEP_TIME = 5
MAX_SLEEP_TIME = 12

LAST_TASK_FILE = dirname(os.path.realpath(__file__)) + '/lastTask.txt'

baseURL = f"https://m.land.naver.com/article/info/"

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


# extract info of property (공급면적, 전용면적, 방향, 해당층, 총층, 방수, 욕실수, 총주차대수, 총세대수, 준공년월)
def extractInfos(id):
    result = requests.get(baseURL + str(int(id)),headers=HEAD)
    soup = BeautifulSoup(result.text,"html.parser")

    if soup.select_one('.heading_place') == None:
        return {
            '공급/전용면적': [None], 
            '방향': [None], 
            '해당층/총층': [None], 
            '방수/욕실수': [None], 
            '총주차대수': [None], 
            '총세대수': [None], 
            '준공년월': [None]
            }

    titleContent = {}
    title = soup.select_one('.heading_place').text
    title = ' '.join(title.replace('\\xa0', ' ').split())
    titleContent['매물명'] = [title]
    titleContent['분류'] = [soup.select_one('.label_detail--category').text]
    titleContent['매물번호'] = [id]

    spec = ['공급/전용면적', '방향', '해당층/총층', '방수/욕실수', '총주차대수', '총세대수', '준공년월']
    infos = soup.select('.col_half')
    for info in infos:
        title = info.find('span', {'class': 'tit'}).text
        content = info.find('span', {'class': 'data'}).text

        if title in spec:
            splitTitle = title.split('/')
            splitContent = re.sub('층|개|대|세대', '', content).split('/')
            if len(splitTitle) == 1:
                content = re.sub('세대|대', '', content)
                titleContent[title] = [content]
            elif len(splitTitle) == 2:
                titleContent[splitTitle[0]] = [splitContent[0]]
                titleContent[splitTitle[1]] = [splitContent[1]]

    return titleContent


def loadAdditionalInfo(csvFile, fileIdx, idIdx):
    targetFileName = csvFile.split('/')[-1]


    idDF = pd.read_csv(csvFile)
    idList = idDF['atclNo'].values.tolist()

    if 0<=idIdx and idIdx<len(idList):
        idList = idList[idIdx:]
    else:
        os.remove(targetFileDiv + targetFileName)

    timeRemaining = len(idList) * (MAX_SLEEP_TIME+MIN_SLEEP_TIME)/2

    print('{0:s} 크롤링 시작... ({1:.1f}초 남음)'.format(csvFiles[fileIdx], timeRemaining))

    for i, id in enumerate(idList):
        waitingTime = random.randint(MIN_SLEEP_TIME, MAX_SLEEP_TIME)
        time.sleep(waitingTime)
        timeRemaining -= waitingTime

        itemDF = pd.DataFrame.from_dict(extractInfos(id))
        print('{0:3f}%... ({1:.1f}초 남음)'.format((i+1)/len(idList), timeRemaining))

        if idIdx+i == 0:
            h = True
            print('csv파일 헤더 생성 (새파일이 아닐때 이 메시지가 뜨는 경우 csv파일을 확인바람)')
        else:
            h = False

        itemDF.to_csv(targetFileDiv + targetFileName, header = h,index=False, mode='a')

        f = open(LAST_TASK_FILE, 'w')
        f.write(str(fileIdx) + ' ' + str(i + idIdx))
        f.close()

def mergeInfos(csvFile):
    propertyDF = pd.read_csv(csvFile)
    propertyDF = propertyDF[['atclNo', 'rletTpCd', 'tradTpCd', 'prc', 'lat', 'lng', 'tagList']]
    propertyDF = propertyDF.rename(columns={'atclNo':'매물번호', 'rletTpCd':'매물형태', 'tradTpCd':'거래방식', 'prc':'가격', 'lat':'위도', 'lng':'경도', 'tagList':'태그'})


fileIdx = 0
idIdx = 0

if Path(LAST_TASK_FILE).exists():
    f = open(LAST_TASK_FILE, 'r')
    lastTask = f.readline().split()
    f.close()

    if len(lastTask) == 2:
        fileIdx = int(lastTask[0])
        idIdx = int(lastTask[1])+1

#csvFiles = csvFiles[fileIdx:]

for i in range(fileIdx, len(csvFiles)):
    file = rawCsvFileDiv + csvFiles[i]
    loadAdditionalInfo(file, i, idIdx)  # 새로운 구로 넘어가면 새로운 구 번호를 넘겨준다.
    idIdx = 0 # 한 구가 종료되었으면 idIdx는 초기화