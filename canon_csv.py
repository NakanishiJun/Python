# -*- coding:utf-8 -*-
import glob, re, sys
import pandas as pd

common_list = []

csv_2018_all = pd.read_csv('./2018_all.csv', encoding="ms932").tail(1297)
csv_2017_now = pd.read_csv('./2017_now2.csv', encoding = "ms932").head(69)

list_2017 = csv_2017_now.values.tolist()
list_2018 = csv_2018_all.values.tolist()

for i in list_2017:
    for n in list_2018:
    	if i[0] == n[0]:
    		common_list.append(n)

df = pd.DataFrame(common_list)
 
# CSV ファイル (employee.csv) として出力
df.to_csv("common.csv", encoding='SJIS')
