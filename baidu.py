import requests

# url = 'http://www.baidu/com/s'
url = 'http://www.taobao.com/search?q=书包'

try:
    # kv = {'wd': 'python'}
    # r = requests.get(url, params=kv)
    r = requests.get(url)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))

except:
    print("爬取失败")

