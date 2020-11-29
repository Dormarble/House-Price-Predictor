import requests
import json

f = open("hscpNo.txt", 'r')
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)\ AppleWebKit 537.36 (KHTML, like Gecko) Chrome"}
complexNo_list = f.readlines()

for complexNo in complexNo_list:
    complexNo = complexNo.rstrip()
    url = f"https://new.land.naver.com/api/complexes/{complexNo}?sameAddressGroup=false"
    res = requests.get(url, headers=header).json()
    with open(f'{complexNo}.json', "w") as f:
        json.dump(res, f)