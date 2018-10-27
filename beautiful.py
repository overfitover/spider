import requests
from bs4 import BeautifulSoup

url = "http://python123.io/ws/demo.html"

try:
    r = requests.get(url)
    r.raise_for_status()
    demo = r.text
    soup = BeautifulSoup(demo, 'html.parser')
    print(soup.prettify())
except:
    print("失败")