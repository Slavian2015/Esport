from bs4 import BeautifulSoup
import requests as req
import pandas as pd
import numpy as np
import os
import Structure



main_path_data = os.path.abspath("./data")

##################################   SHOW ALL ROWS & COLS   ####################################
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None)


def new_live_refresh():
    # resp = req.get('https://ru.dltv.org/matches')
    # soup = BeautifulSoup(resp.text, 'lxml')
    # print(soup.prettify())

    with open(main_path_data + "\\live_matches.html", "r", encoding='utf-8') as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')

        #######################   LIVE   MATCHES   ##########################################

        Mtour_live = []
        match_id_live = []
        Mlinks_live = []

        Mmap_live = []
        Mtime_live = []
        Mtypes_live = []


        T1_live_score1 = []
        T1_live_score2 = []


        T2_live_score1 = []
        T2_live_score2 = []


        teams = []
        logos = []





        for rows in soup.find_all("div", attrs={"class": "event-box live-matches scrolling-inner-big jsLiveMatches"}):
            for item in rows.find_all("div", attrs={"class": "live-matches-row"}):
                id = item["data-serie-id"]
                # print(id)                                                                   #shows:  ALL MATCHES ids
                match_id_live.append(id)
                for na in item.find_all("a", attrs={"class": "abs-link"}):
                    Mlinks_live.append(na.get('href'))
                    # print(na.get('href'))                                                   #shows:  ALL MATCHES LINKS




                for na in item.find_all("table", attrs={"class": "table"}):
                    for rep in na.find_all("td", attrs={"class": "mobile-none border-left"}):
                        for nas in rep.find_all("a"):
                            Mtour_live.append(nas.text.replace('\n', '').replace(' ', '').strip())  #shows:  ALL TOURS Names

                    for rep in na.find_all("td", attrs={"class": "mobile-none border-right"}):
                        for nas in rep.find_all("p"):
                            Mtypes_live.append(nas.text.replace('\n', '').replace(' ', '').strip())  #shows:  ALL MATCHES TYPE

                    for rep in na.find_all("td", attrs={"class": "border-left border-right"}):
                        for nas2 in rep.find_all("div", attrs={"class": "map-time"}):
                            data4 = nas2.text.replace('\n', '').replace(' ', '').strip()
                            Mtime_live.append(data4[4:])
                            # print(data4[4:])

                            for nas3 in nas2.find_all("span", attrs={"class": "jsMatchMapNumber"}):
                                Mmap_live.append(nas3.text.replace('\n', '').strip())             #shows:  ALL MATCHES MAP #

                    for rep in na.find_all("td", attrs={"class": "border-left"}):
                        for ids in rep.find_all('div', attrs={"teams-date__left"}):
                            teams.append(ids.text.replace('\n', '').replace(' ', '').strip())    #shows:  ALL MATCHES teams

                        for ids in rep.find_all('img'):
                            # T1logos.append(id.get('src').replace('Nan', '').strip())
                            logos.append(ids.get('src'))                                          #shows:  ALL MATCHES logos


                        for ids in rep.find_all('div', attrs={"team-score"}):
                            # print(ids.text.replace('\n', '').replace(' ', '').strip())    #shows:  ALL MATCHES SCORE

                            for ids2 in ids.find_all('div', attrs={"diff-score__left mobile-none"}):
                                T1_live_score2.append(ids.text.replace('\n', '').replace(' ', '').strip())  # shows:  ALL MATCHES SCORE


                            for ids2 in ids.find_all('div', attrs={"diff-score__right"}):
                                # print(ids.text.replace('\n', '').replace(' ', '').strip())
                                T2_live_score2.append(ids.text.replace('\n', '').replace(' ', '').strip())  # shows:  ALL MATCHES SCORE

                    for ids in na.find_all('td', attrs={"border-left jsFirstTeamScore"}):
                        # print(ids.text.replace('\n', '').replace(' ', '').strip())
                        T1_live_score1.append(
                            ids.text.replace('\n', '').replace(' ', '').strip())  # shows:  ALL MATCHES SCORE

                    for ids in na.find_all('td', attrs={"border-left jsSecondTeamScore"}):
                        T2_live_score1.append(
                            ids.text.replace('\n', '').replace(' ', '').strip())  # shows:  ALL MATCHES SCORE



        logos2 = logos[1:]
        teams2 = teams[1:]

        T1names_live = teams[::2]
        T2names_live = teams2[::2]

        T1logos_live = logos[::2]
        T2logos_live = logos2[::2]



        dw_live = {
            'Mtour_live': Mtour_live,
                   'match_id_live': match_id_live,
                   'Mlinks_live': Mlinks_live,
                   'Mmap_live': Mmap_live,
                   'Mtime_live': Mtime_live,
                   'Mtypes_live': Mtypes_live,
                   'T1_live_score1': T1_live_score1,
                   'T1_live_score2': T1_live_score2,
                   'T2_live_score1': T2_live_score1,
                   'T2_live_score2': T2_live_score2,
                   'T1names_live': T1names_live,
                   'T2names_live': T2names_live,
                   'T1logos_live': T1logos_live,
                   'T2logos_live': T2logos_live
                   }


        df_live = pd.DataFrame(data=dw_live)


        print(df_live)

new_live_refresh()