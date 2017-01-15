import datetime
import time
import csv
import sys
import re
import urllib.request
import pandas as pd
import matplotlib.pyplot as plot
import matplotlib
import numpy as np
import locale
import seaborn as sns
from bs4 import BeautifulSoup

#開くべきURLを指定
def access_url(code, sy, sm, sd, ey, em, ed):
    url = 'http://info.finance.yahoo.co.jp/history/?code=%d.T&sy=%d&sm=%d&sd=%d&ey=%d&em=%d&ed=%d&tm=d' % (code, sy, sm, sd, ey, em, ed)
    return url 

#リストを取るべきページ数の指定
soup = BeautifulSoup(html, "lxml")
#article = soup.find(class_="boardFin yjSt marB6")
item = soup.find('span', 'stocksHistoryPageing yjS').string
total_items = int(re.findall(r'\d+', item)[2])
page_num  = int(np.ceil(total_items/20))

#各ページから株価を取ってくる
def page_research(code, sy, sm, sd, ey, em, ed, p=1):
    for i in range (1, p):
        read_url = 'http://info.finance.yahoo.co.jp/history/?code=%d.T&sy=%d&sm=%d&sd=%d&ey=%d&em=%d&ed=%d&tm=d&&p=%d' % (code, sy, sm, sd, ey, em, ed, i)
        response = urllib.request.urlopen(read_url)
        html = response.read().decode("utf-8")
        soup = BeautifulSoup(html, "lxml")
        item = soup.find(class_="boardFin yjSt marB6")
        h2_list = item.findAll("tr")
        tds = item.findAll("td")
        print (tds)

##以下は要修正
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
