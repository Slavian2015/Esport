from bs4 import BeautifulSoup
import requests as req
import pandas as pd
import requests

import os
import pandas as pd
main_path_data = os.path.abspath("./data")
import time



l = ['@Valqui / 외로운 본질', 'D1smar', 'Argius', 'Panda']

print(len(l))


if len(l) < 5:
    l.append("")

print(l)
#
#
# resp = req.get('https://ru.dltv.org/matches/370571', headers={'User-Agent': 'Mozilla'})
# # print (response.encoding)
#
# soup = BeautifulSoup(resp.content, 'lxml')
#
# # print(soup.prettify())
#
# gdp_table = soup.find("table", attrs={"class": "table player-stat"})
# gdp_table_data = gdp_table.tbody.find_all("tr")
# T2data = []
# for td in gdp_table_data[7].find_all("a"):
#     T2data.append(td.text.replace('\n', '').strip())
#
# print(T2data)
#
#
# P21 = []
# P22 = []
# P23 = []
# P24 = []
# P25 = []
#
# P21.append(T2data[0])
# P22.append(T2data[1])
# P23.append(T2data[2])
# P24.append(T2data[3])
# P25.append(T2data[4])
#
#
#
# print(P21, P22, P23, P24, P25)



