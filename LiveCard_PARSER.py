from bs4 import BeautifulSoup
import requests as req
import pandas as pd
import requests
import re
import os
import pandas as pd
from pandas._libs.tslibs.timestamps import Timestamp

main_path_data = os.path.abspath("./data")
import time



##################################   SHOW ALL ROWS & COLS   ####################################
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None)

# resp = req.get('https://ru.dltv.org/matches/371307', headers={'User-Agent': 'Mozilla'})
# soup = BeautifulSoup(resp.content, 'lxml')
# print(soup.prettify())

def newCard(link, Mid):

    print("#######  LINK   :", link)
    print("#######  Mid   :", Mid)

    resp = req.get(link, headers={'User-Agent': 'Mozilla'})
    soup = BeautifulSoup(resp.content, 'lxml')

# with open(main_path_data + "\\live_matches.html", "r", encoding='utf-8') as f:
#     contents = f.read()
#     soup = BeautifulSoup(contents, 'lxml')

    #######################   LIVE   MATCHES   ##########################################

    Teams = []
    #
    # Team1 = Teams[0]
    # Team2 = Teams[1]

    Players = []


    Hero_pic = []
    Level_hero = []
    KDA = []
    Hero_items = []
    Hero_gold = []
    LH_DN = []
    GPM_XPM = []
    NW = []
    T1score = []


    regex = re.compile('[/]')



    for rows in soup.find_all("div", attrs={"class": "personal-team renewed"}):
        for item3 in rows.find_all("div", attrs={"class": "rig"}):
            for item in item3.find_all("div", attrs={"class": "score"}):
                T1score.append(item.text.replace('\n', '').replace(' ', '').strip())          #shows:  Teams names






    for rows in soup.find_all("div", attrs={"class": "live-statistics-info"}):
        for item3 in rows.find_all("div", attrs={"class": "event-box-top"}):
            Teams.append(item3.text.replace('\n', '').replace(' ', '').strip())          #shows:  Teams names


        for item3 in rows.find_all("div", attrs={"class": "radient-content-row"}):
            for item in item3.find_all("div", attrs={"class": "player-cell"}):
                Players.append(item.text.replace('\n', '').replace(' ', '').strip())       #shows:  ALL MATCHES Players


            for item in item3.find_all("div", attrs={"class": "players_stats_cell type-cell active"}):
                for item11 in item.find_all("img"):
                    Hero_pic.append(item11.get('src'))                                    #shows:  ALL Active Heroes

            for item in item3.find("div", attrs={"class": "players_stats_cell type-cell", "data-type": "2"}):
                Level_hero.append(item.replace('\n', '').replace(' ', '').strip())             # shows:  ALL Active LEVEL

            for item in item3.find("div", attrs={"class": "players_stats_cell kda-cell active"}):
                KDA.append(item.replace('\n', '').replace(' ', '').strip())             # shows:  ALL Active LEVEL


            for item in item3.find_all("div", attrs={"class": "players_stats_cell type-cell", "data-type": "2"}):
                if (regex.search(item.text) == None):
                    pass
                else:
                    LH_DN.append(item.text.replace('\n', '').replace(' ', '').strip())         # shows:  LH/DN


            for item in item3.find_all("div", attrs={"class": "players_stats_cell gmp-cell"}):
                GPM_XPM.append(item.text.replace('\n', '').replace(' ', '').strip())             # shows:  GPM/XPM


            for item in item3.find_all("div", attrs={"class": "players_stats_cell type-cell active", "data-type": "1"}):
                Hero_gold.append(item.text.replace('\n', '').replace(' ', '').strip())          #shows:  ALL Active GOLD


            for item in item3.find_all("div", attrs={"class": "players_stats_cell type-cell active", "data-type":"1"}):
                NW.append(item.text.replace('\n', '').replace(' ', '').strip())          #shows:  NW


            for item in item3.find_all("div", attrs={"class": "players_stats_cell items-cell", "data-type":"3"}):
                pics = []
                for item2 in item.find_all("a"):
                    for item22 in item2.find_all("img"):
                        pics.append(item22.get('src'))
                # print(pics[0], pics[1], pics[5])
                Hero_items.append(pics)#shows:  ITEMS


    status = []

    for rows in soup.find_all("div", attrs={"class": "personal-team__info"}):
        for id in rows.find_all("div", attrs={"class": "mb-1"}):
            status.append(id.text.replace('\n', '').strip())

    if len(status)>1:
        status = status[1]
    else:
        status = status[0]                                                       #shows:  MATCH STATUS


    print("########   T1score :", T1score)
    print("########   MID :", Mid)
    print("########   Players :", Players)
    print("########   Hero_pic :", Hero_pic)
    print("########   Level_hero :", Level_hero)
    print("########   KDA :", KDA)
    print("########   Hero_items :", Hero_items)
    print("########   Hero_gold :", Hero_gold)
    print("########   LH_DN :", LH_DN)
    print("########   GPM_XPM :", GPM_XPM)
    print("########   NW :", NW)
    print("########   status :", status)



    dw_live = {

        'Mid': Mid,
        'Players': Players,
        'Hero_pic': Hero_pic,
        'Level_hero': Level_hero,
        'KDA': KDA,
        'Hero_items': Hero_items,
        'Hero_gold': Hero_gold,
        'LH_DN': LH_DN,
        'GPM_XPM': GPM_XPM,
        'NW': NW,
        'status': status,
        'T1score': T1score[0],
        'T2score': T1score[1],
    }

    df_live = pd.DataFrame(data=dw_live)

    # print(df_live)

    live_scoreBD = pd.read_csv(main_path_data + '\\live_score.csv')
    filterBD = live_scoreBD[live_scoreBD["Mid"].isin([Mid])]

    if filterBD.shape[0] > 0:
        print("БОЛЬШЕ")
        live_scoreBD = live_scoreBD.set_index("Mid")
        live_scoreBD = live_scoreBD.drop(filterBD['Mid'], axis=0)
        live_scoreBD = live_scoreBD.reset_index()
        live_scoreBD = live_scoreBD.append(df_live)
        live_scoreBD.to_csv(main_path_data + "\\live_score.csv", index=False, header=True)
    else:
        print("МЕНЬШЕ")
        live_scoreBD = live_scoreBD.append(df_live)
        live_scoreBD.to_csv(main_path_data + "\\live_score.csv", index=False, header=True)


    allBD = pd.read_csv(main_path_data + '\\all_cards.csv')
    filter = allBD[(allBD['Mid'].isin([Mid]))].index
    allBD.loc[filter, "Mstatus"] = status
    allBD.loc[filter, "T1score"] = T1score[0]
    allBD.loc[filter, "T2score"] = T1score[1]

    allBD.to_csv(main_path_data + "\\all_cards.csv", index=False, header=True)


    # print(df_live.head(n=5))
    # print(df_live.tail(n=5))

    return

# newCard('https://ru.dltv.org/matches/371408', '371408')