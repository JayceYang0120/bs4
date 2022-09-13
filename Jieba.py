import urllib.request
import jieba
import jieba.analyse


url = "https://github.com/fxsjy/jieba/raw/master/extra_dict/dict.txt.big"
urllib.request.urlretrieve(url, "dict.big")
jieba.set_dictionary("dict.big")
jieba.load_userdict("nba.dict")

f = open("news.txt", "r", encoding="utf-8")
news = f.read()
f.close()

print("分詞:", list(jieba.cut(news)))

keywords = jieba.analyse.extract_tags(news)
print("重點:", keywords)
