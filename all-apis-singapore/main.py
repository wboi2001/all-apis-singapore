import time, requests, threading, datetime

webhookurl = 'https://discord.com/api/webhooks/875860965424525322/_JC7fyrmvhxULDyHjL7ACRm15qFzE_oq7Wif__ymdZnZMR47AEChYS8YvN4qt6d3RSOc'
total = []
list="""https://www.binancezh.com
https://www.binancezh.ac
https://www.binancezh.be
https://www.binancezh.cz
https://www.binancezh.in
https://www.binancezh.io
https://www.binancezh.jp
https://www.binancezh.sh
https://www.binance.com
https://www.binance.info"""

listlines = list.split('\n')
end = '/bapi/composite/v1/public/cms/article/catalog/list/query?catalogId=48&pageNo=1&pageSize=1'

def webhook(title, site):
    return requests.post(webhookurl, data={'name': title, 'content': f"`{datetime.datetime.now()} | {title} | {site}`"})

def check(site):

    try:
        x = requests.get(url=site).json()['data']['articles'][0]['title']
        try:
            if x not in total:
                total.append(x)
                threading.Thread(target=webhook, args=(x, site, )).start()
        except:
            pass
    except Exception as owo:
        print(owo, site)

    return

print('Starting')
while True:
    for line in listlines:
        x = threading.Thread(target=check, args=(line+end,)).start()
    time.sleep(2)