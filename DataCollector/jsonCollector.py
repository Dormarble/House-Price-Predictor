import requests, json
f = open("hscpNo.txt", 'r')
header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)\ AppleWebKit 537.36 (KHTML, like Gecko) Chrome"}
while True:
    complexNo = f.readline()
    if not complexNo:
        break
    complexNo = int(complexNo)
    url = f"https://new.land.naver.com/api/complexes/{complexNo}?sameAddressGroup=false"
    data = requests.get(url, headers=header).json()
    with open("../dataJSON/" + str(complexNo)+".json", 'w') as outfile:
        json.dump(data, outfile)