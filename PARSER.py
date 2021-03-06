from bs4 import BeautifulSoup
import requests as req
import pandas as pd
import numpy as np
import os
import Structure
import LiveCard_PARSER


main_path_data = os.path.abspath("./data")

# ##################################   SHOW ALL ROWS & COLS   ####################################
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# pd.set_option('display.expand_frame_repr', False)
# # pd.set_option('max_colwidth', -1)

def new_refresh():
    resp = req.get('https://ru.dltv.org/matches')
    soup = BeautifulSoup(resp.text, 'lxml')


    # with open("Matches.html", "r", encoding='utf-8') as f:
    #     contents = f.read()
    #     soup = BeautifulSoup(contents, 'lxml')


    match_id =[]
    Mlinks = []
    T1names = []
    T2names = []
    T1logos = []
    T2logos = []
    Mdate = []
    Mtime = []
    Mtour = []
    Mtypes = []

    for rows in soup.find_all("div", attrs={"class": "matches-tab js-tab-wrap scrolling-inner-big live-matches jsComingMatches"}):
        for item in rows.find_all("div", attrs={"class": "live-matches-row"}):
            id = item["data-serie-id"]
            match_id.append(id)
            for na in item.find_all("a", attrs={"class": "abs-link"}):
                Mlinks.append(na.get('href'))
                # print(na.get('href'))                                           #shows:  ALL MATCHES LINKS

            for na in item.find_all("div", attrs={"class": "event-date"}):
                    for i in na.find_all("a"):
                        Mtour.append(i.text.replace('Nan', '').strip())
                        # print(i.text)                                             #shows:  ALL TOURNAMENTS NAMES

            for na in item.find_all("div", attrs={"class": "type-date mobile-none"}):
                    for i in na.find_all("div"):
                        Mtypes.append(i.text.replace(str(np.nan), '').strip())
                        # print(i.text)                                             #shows:  ALL TYPES NAMES

            for na in item.find_all("div", attrs={"class": "teams-date"}):
                    for i in na.find_all("div", attrs={"class": "teams-date__left"}):
                        T1names.append(i.text.replace('[]', '').strip())
                        # print(i.text)                                               #shows:  Team 1
                        for id in i.find_all('img'):
                            T1logos.append(id.get('src').replace('Nan', '').strip())
                            # print(id.get('src'))
                    for i in na.find_all("div", attrs={"class": "date"}):
                        # Mtime.append(i.text.replace('Nan', '').strip())
                        t = i.text.replace('Nan', '').strip()
                        t = t.split(' ')
                        Mtime.append(t[1])
                        Mdate.append(t[0])
                        # print(i.text)                                               #shows:  Time
                    for i in na.find_all("div", attrs={"class": "teams-date__right"}):
                        T2names.append(i.text.replace('Nan', '').strip())
                        # print(i.text)                                               #shows:  Team 2
                        for id in i.find_all('img'):
                            T2logos.append(id.get('src').replace('Nan', '').strip())
                            # print(id.get('src'))

    dw = {'match_id': match_id, 'Mlinks': Mlinks, 'T1names': T1names, 'T2names': T2names, 'T1logos': T1logos, 'T2logos': T2logos, 'Mtime': Mtime, 'Mdate': Mdate, 'Mtour': Mtour, 'Mtypes': Mtypes}
    df = pd.DataFrame(data=dw)
    df1 = df.head(n=20)

    df1['TIME'] = df1['Mdate'].astype(str) + ' ' + df1['Mtime'].astype(str)
    df1['TIME'] = pd.to_datetime(df1['TIME'])
    df1['TIME'] = df1['TIME'].dt.tz_localize('UTC').dt.tz_convert('Etc/GMT-3')
    df1['Mdate'] = [d.date() for d in df1['TIME']]
    df1['Mtime'] = [d.time() for d in df1['TIME']]

    df1.to_csv(main_path_data + '\\refresh.csv', index=False, header=True)



    def new_live_refresh():
    # resp = req.get('https://ru.dltv.org/matches')
    # soup = BeautifulSoup(resp.text, 'lxml')
    # print(soup.prettify())

    # with open(main_path_data + "\\live_matches.html", "r", encoding='utf-8') as f:
    #     contents = f.read()
    #     soup = BeautifulSoup(contents, 'lxml')

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

        allBD = pd.read_csv(main_path_data + '\\all_cards.csv')

        for ind in df_live.index:
            filter = allBD[(allBD['Mid'] == df_live['match_id_live'][ind])].index
            allBD.loc[filter, "T1score"] = df_live['T1_live_score1'][ind]
            allBD.loc[filter, "T2score"] = df_live['T1_live_score1'][ind]

        allBD.to_csv(main_path_data + "\\all_cards.csv", index=False, header=True)
        df_live.to_csv(main_path_data + '\\live.csv', index=False, header=True)

        for ind in df_live.index:
            LiveCard_PARSER.newCard(df_live['Mlinks_live'][ind], df_live['match_id_live'][ind])



        ##  IF not in live.csv
        # delet from live_score.csv

    new_live_refresh()
    return

new_refresh()
Structure.refresh_BD()


