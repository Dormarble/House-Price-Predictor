import requests
import numpy as np
import time
import json
import pandas as pd
import random
from selenium import webdriver
import os
print(os.getcwd())
#{"gu":"강남구","LAT":37.497113 ,"LON": 127.062318,"DONG":11680}
#{"gu":"강북구","LAT":37.638649 ,"LON": 127.021337,"DONG":11305}
code=[
 {"gu":"강동구","LAT":37.547284 ,"LON": 127.147819,"DONG":11740}
,{"gu":"강서구","LAT":37.557012 ,"LON": 126.823391,"DONG":11500}
,{"gu":"관악구","LAT":37.477748 ,"LON": 126.950788,"DONG":11620}
,{"gu":"광진구","LAT":37.548608 ,"LON": 127.082634,"DONG":11215}
,{"gu":"구로구","LAT":37.493441 ,"LON": 126.851923,"DONG":11530}
,{"gu":"금천구","LAT":37.466765 ,"LON": 126.898586,"DONG":11545}
,{"gu":"노원구","LAT":37.639354 ,"LON": 127.072757,"DONG":11350}
,{"gu":"도봉구","LAT":37.660125 ,"LON": 127.037006,"DONG":11320}
,{"gu":"동대문구","LAT":37.582263 ,"LON": 127.049773 ,"DONG":11230}
,{"gu":"동작구" , "LAT":37.500862 ,"LON": 126.949992 ,"DONG":11590 }
,{"gu":"마포구",  "LAT":37.551057 ,"LON": 126.931071 ,"DONG":11440}
,{"gu":"서대문구","LAT":37.569822 ,"LON": 126.949121 ,"DONG":11410}
,{"gu":"서초구",  "LAT":37.474402 ,"LON": 127.033607 ,"DONG":11650}
,{"gu":"성동구",  "LAT":37.555878 ,"LON": 127.035161 ,"DONG":11200}
,{"gu":"성북구"  ,"LAT":37.591859 ,"LON": 127.020048 ,"DONG":11290}
,{"gu":"송파구"  ,"LAT":37.502988 ,"LON": 127.119120 ,"DONG":11710}
,{"gu":"양천구"  ,"LAT":37.530285 ,"LON": 126.853761 ,"DONG": 11470}
,{"gu":"영등포구","LAT":37.522614 ,"LON": 126.899129 ,"DONG":11560}
,{"gu":" 용산구" ,"LAT":37.536019 ,"LON": 126.972387 ,"DONG":11170}
,{"gu":" 은평구 ","LAT":37.607088 ,"LON": 126.917073 ,"DONG": 11380}
,{"gu":" 종로구 ","LAT":37.577500 ,"LON": 126.982828 ,"DONG":11110}
,{"gu":"  중구  ","LAT":37.563092 ,"LON": 126.988644 ,"DONG": 11140}
,{"gu":" 중랑구 ","LAT":37.599270 ,"LON": 127.087847 ,"DONG": 11260}]

url = "https://m.land.naver.com/cluster/ajax/articleList"
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

def get_soup(DONG,LAT,LON,PAGE):
##행정동 및 위도 경도##변수 입력 
    dong={"cortarNo":DONG}
    lat={"lat":LAT}
    lon={"lon":LON}
    page={"page":PAGE}
  ##고정값
    con1= {"rletTpCd":"DDDGG%3AGM"} ## 검색물건
    con2= {"tradTpCd":"A1"} ##거래방법 A1 : 매매
    con3={"showR0":""}    ## 그외조건 없음
    con4 = {"z":"7"}  ## 축척
  ##검색조건
    space1={"spcMin":"0"} ##40평이상
    space2={"spcMax":"900000000"} ## 무한
    price1={"dprcMin":"10000"} ## 금액 제한
    price2={"dprcMax":"10000000"}
  ##mapping 고정값
    rgt = {"rgt": str(float(lat["lat"])+0.3475542)}
    lft = {"lft": str(float(lat["lat"])-0.3475542)}
    top = {"top": str(float(lon["lon"])+0.0538928)}
    btm = {"btm": str(float(lon["lon"])-0.0538928)}
    qstring={**con1,**con2,**con3,**con4,**space1,**space2,**price1,**price2,**dong,**lat,**lon,**lft,**rgt,**top,**btm,**page}
    result=requests.request("GET",url,headers=HEAD,params=qstring)
    text=json.loads(result.text)
    return text

#강남구
for l, c in enumerate(code):
    DONG=str(code[l]["DONG"]*100000)
    LAT=str(code[l]["LAT"])
    LON=str(code[l]["LON"])
    print(code[l]['gu'])
    datas=pd.DataFrame()

    for i in range(1,1000):
        if get_soup(DONG,LAT,LON,i)["more"]==True:
            data=get_soup(DONG,LAT,LON,i)["body"]
            datas=datas.append(data)
            colname =["atclNo","cortarNo","rletTpCd","tradTpCd","flrInfo","prc","spc1","spc2","direction","lat","lng","atclFetrDesc","tagList","rltrNm"]
            data_fin=datas[colname]
            print(i)
            i += 1
            time.sleep(random.randint(5, 12))
        elif get_soup(DONG,LAT,LON,i)["more"]==False:
            print("no")
            break
    data_fin.to_csv(c['gu'] + ".csv",header = True,index=False)