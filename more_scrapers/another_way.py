#using soup to dig deeper into html structure
import pandas as pd
import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.basketball-reference.com/players/j/jamesle01.html")

soup = BeautifulSoup(res.content,'lxml')

table = soup.find_all('table')[0]

row = table.find_all('tr')[1]
# print(row)

s1_stats = []

for data in row.find_all('td'):
    s1_stats.append(data.text)

print(s1_stats)