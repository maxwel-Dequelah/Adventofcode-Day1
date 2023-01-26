from bs4 import BeautifulSoup
import lxml.html
import requests
import json

cookies = {
    '_ga': 'GA1.2.1853744814.1674655232',
    '_gid': 'GA1.2.238997403.1674655232',
    'ru': '53616c7465645f5f0b866c04502f1eb0e21aadf2a722987b95b135aefcd2cc89',
    'session': '53616c7465645f5fe416c5549c458aeddd0e765e2df014dde3a5519c4a5c7693977355cb2ac83be471987faa85d4b2ac8324ae4c70dbb7e8a2260a86c96cd9bf',
    'arp_scroll_position': '18304',
}

headers = {
    'authority': 'adventofcode.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': '_ga=GA1.2.1853744814.1674655232; _gid=GA1.2.238997403.1674655232; ru=53616c7465645f5f0b866c04502f1eb0e21aadf2a722987b95b135aefcd2cc89; session=53616c7465645f5fe416c5549c458aeddd0e765e2df014dde3a5519c4a5c7693977355cb2ac83be471987faa85d4b2ac8324ae4c70dbb7e8a2260a86c96cd9bf; arp_scroll_position=18304',
    'referer': 'https://adventofcode.com/2022/day/1',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36',
}

response = requests.get('https://adventofcode.com/2022/day/1/input', cookies=cookies, headers=headers)
value2=BeautifulSoup(response.text,'lxml')

numbers=value2.text

numbers=numbers.split("\n\n")
newNumbers=[]
for i in numbers:
    i=i.replace('\n',',')
    newNumbers.append(i)

finalArray=[]

for values in newNumbers:
    sum=0
    values=values.split(',')
    for i in values:
        if i !='':
            sum=sum+int(i)
        else:
            pass
    finalArray.append(sum)

with open("file.json", "w") as jsonfile: 
    json.dump(finalArray, jsonfile)

print(max(finalArray))
