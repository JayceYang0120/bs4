import os
import requests
from bs4 import BeautifulSoup
import shutil

url = "https://www.ptt.cc/bbs/Beauty/M.1605506600.A.32A.html"
response = requests.get(url, cookies={"over18":"1"})
html = BeautifulSoup(response.text)

dirname = "ptt/" + url.split("/")[-1]
if not os.path.exists(dirname):
    os.makedirs(dirname)

allowed = ["jpg", "jpeg", "png", "gif"]
links = html.find_all("a")
for a in links:
    href = a["href"]
    sub = href.split(".")[-1]
    if sub.lower() in allowed:
        # SSL certificate fail
        print("下載:", href)
        response = requests.get(href, stream=True, verify=False)
        fname = dirname + "/" + href.split("/")[-1]
        f = open(fname, "wb")
        shutil.copyfileobj(response.raw, f)
        f.close()
