import datetime
import time
import csv
import sys
import urllib.request
import pandas as pd
import matplotlib.pyplot as plot
import matplotlib
import numpy as np
import locale
import seaborn as sns

#一旦適当な株のページを参照（あとで複数指定できるようにする）
URL = 'http://info.finance.yahoo.co.jp/history/?code=6050.T'

response = urllib.request.urlopen(URL)

html = response.read().decode("utf-8")

#beautiful soupでスクレイピング
#lxmlは超高速らしいので使う
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "lxml")
article = soup.find(class_="boardFin yjSt marB6")
h2_list = article.findAll("tr")
tds = article.findAll("td")

def get_price(lists, idx =1):
	elm = lists[idx]
	tds = elm.findAll("td")
	data = [td.text for td in tds]
	return data
get_price(h2_list, 2)

price_sets = []
for i in range(1,20):
    data = get_price(h2_list, i)
    price_sets.append(data)

data = pd.DataFrame(price_sets)

data.columns = ['日付','始値','高値','安値','終値','出来高','調整後終値']

data = data.sort_index(ascending=False)
data.reset_index(drop=True)

data['始値']  = data['始値'].str.replace(u',','')
data['高値']  = data['高値'].str.replace(u',','')
data['安値']  = data['安値'].str.replace(u',','')
data['終値']  = data['終値'].str.replace(u',','')
data['出来高']  = data['出来高'].str.replace(u',','')
data['調整後終値']  = data['調整後終値'].str.replace(u',','')

data['始値'] = data['始値'].astype(float)
data['高値']  = data['高値'].astype(float)
data['安値']  = data['安値'].astype(float)
data['終値']  = data['終値'].astype(float)
data['出来高']  = data['出来高'].astype(float)
data['調整後終値']  = data['調整後終値'].astype(float)
data.dtypes

data.plot(x = '日付', y = ['終値', '出来高'], figsize=(20,10))