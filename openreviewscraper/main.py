import math
import pandas as pd
import requests


def run():

    url = "https://api.openreview.net/notes?content.venue=NeurIPS+2022+Accept&details=replyCount&offset=0&limit=1&invitation=NeurIPS.cc%2F2022%2FConference%2F-%2FBlind_Submission"

    payload={}
    headers = {
    'authority': 'api.openreview.net',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'access-control-allow-origin': '*',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'dnt': '1',
    'origin': 'https://openreview.net',
    'referer': 'https://openreview.net/',
    'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    d=response.json()
    count=d['count']


    start=1
    end=math.ceil(count/1000)
    data=[]

    for i in range(start,end+1):
        print(i)
        url = f"https://api.openreview.net/notes?content.venue=NeurIPS+2022+Accept&details=replyCount&offset={(i-1)*1000}&limit={1000}&invitation=NeurIPS.cc%2F2022%2FConference%2F-%2FBlind_Submission"
        payload={}
        headers = {
            'authority': 'api.openreview.net',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            'access-control-allow-origin': '*',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'dnt': '1',
            'origin': 'https://openreview.net',
            'referer': 'https://openreview.net/',
            'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        d=response.json()
        data.append(d)

    n=[]
    for i in data:
        n.extend(i['notes'])


    df=pd.json_normalize(n)

    df['content.pdf']='https://openreview.net'+df['content.pdf']
    df.to_csv('open_review_data.csv', index=False)
