import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

page = 55

df = {
    "Eng":[], 
    "Ja":[], 
    "Rating":[],
    "Area":[],
    "Blog":[]
}

while True:
    url = "https://tabelog.com/tw/kyoto/rstLst/" + str(page) + "/?SrtT=rt"
    print("目前頁數: ", page)
    page = page + 1
    try:
        response = urlopen(url)
    except HTTPError:
        print("Last Page")
        TabelogF = pd.DataFrame(df)
        TabelogF.to_csv("Tabelog.csv", encoding = "utf-8", index = False)
        break
    html = BeautifulSoup(response)

    rs = html.find_all("li", class_ = "list-rst")
    for r in rs:
        en = r.find("a", class_ = "list-rst__name-main")
        ja = r.find("small", class_ = "list-rst__name-ja")
        area = r.find("li", class_ = "list-rst__area")
        opinion = r.find("b", class_ = "c-rating__val")
        price = r.find_all("span", class_ = "c-rating__val")

        print("Name_Eng: ", en.text)
        print("Name_Ja: ", ja.text)
        print("Area: ", area.text.strip())
        print("Opinion: ", opinion.text)
        print("Dinner: ", price[0].text)
        print("Launch: ", price[1].text)
        print("Blog: ", en["href"])
        print()
        print("*" * 30)

        df["Eng"].append(en.text)
        df["Ja"].append(ja.text)
        df["Rating"].append(opinion.text)
        df["Area"].append(area.text)
        df["Blog"].append(en["href"])
