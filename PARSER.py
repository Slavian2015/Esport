from bs4 import BeautifulSoup
import requests
import requests as req
import pandas as pd
import numpy as np



##################################   SHOW ALL ROWS & COLS   ####################################
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)
# pd.set_option('max_colwidth', -1)


# resp = req.get('https://dltv.org/matches')
# soup = BeautifulSoup(resp.text, 'lxml')


with open("Matches.html", "r", encoding='utf-8') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')


    match_id =[]
    Mlinks = []
    T1names = []
    T2names = []
    T1logos = []
    T2logos = []
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
                        Mtime.append(i.text.replace('Nan', '').strip())
                        # print(i.text)                                               #shows:  Time
                    for i in na.find_all("div", attrs={"class": "teams-date__right"}):
                        T2names.append(i.text.replace('Nan', '').strip())
                        # print(i.text)                                               #shows:  Team 2
                        for id in i.find_all('img'):
                            T2logos.append(id.get('src').replace('Nan', '').strip())
                            # print(id.get('src'))


#######################   LIVE   MATCHES   ##########################################

    match_id_live = []
    Mlinks_live = []
    T1names_live = []
    T2names_live = []
    T1logos_live = []
    T2logos_live = []
    Mtime_live = []
    Mtour_live = []
    Mtypes_live = []
    T1names_live_score = []
    T2names_live_score = []


    for rows in soup.find_all("div", attrs={"class": "event-box live-matches scrolling-inner-big jsLiveMatches"}):
        for item in rows.find_all("div", attrs={"class": "live-matches-row"}):
            id = item["data-serie-id"]
            match_id_live.append(id)
            for na in item.find_all("a", attrs={"class": "abs-link"}):
                Mlinks_live.append(na.get('href'))
                # print(na.get('href'))                                           #shows:  ALL MATCHES LINKS


            for na in item.find_all("td", attrs={"class": "mobile-none border-left"}):
                    for i in na.find_all("a"):
                        Mtour_live.append(i.text.replace('Nan', '').strip())
                        # print(i.text)                                             #shows:  ALL TOURNAMENTS NAMES
                    for i in na.find_all("div"):
                        Mtypes_live.append(i.text.replace(str(np.nan), '').strip())
                        # print(i.text)                                             #shows:  ALL TYPES NAMES




    # gdp_table = soup.find("table", attrs={"class": "table"})
    # gdp_table_data = gdp_table.tbody.find_all("tr")
    #
    #
    # for td in gdp_table_data[0].find_all("div", attrs={"class": "teams-date__left"}):
    #
    #     # remove any newlines and extra spaces from left and right
    #     T1logos_live.append(td.text)
    #     print(td.text)
    #     for id in td.find_all('img'):
    #         T1logos_live.append(id.get('src').replace('Nan', '').strip())
    #
    #     for id in td.find_all('td', attrs={"class": "border-left jsFirstTeamScore"}):
    #         T1names_live_score.append(id.text)
    #         print(id.text)













    # dw_live = {'match_id': match_id_live, 'Mlinks': Mlinks_live, 'T1names': T1names_live, 'T2names': T2names_live, 'T1logos': T1logos_live, 'T2logos': T2logos_live, 'Mtime': Mtime_live, 'Mtour': Mtour_live, 'Mtypes': Mtypes_live}
    # df_live = pd.DataFrame(data=dw_live)
    # print(df_live.info())



    dw = {'match_id': match_id, 'Mlinks': Mlinks, 'T1names': T1names, 'T2names': T2names, 'T1logos': T1logos, 'T2logos': T2logos, 'Mtime': Mtime, 'Mtour': Mtour, 'Mtypes': Mtypes}
    df = pd.DataFrame(data=dw)
    # print(df.info())


    # print(len(match_id_live))
    # print(len(Mlinks_live))
    # print(len(T1names_live))
    # print(len(T2names_live))
    # print(len(T1logos_live))
    # print(len(T2logos_live))
    # print(len(Mtime_live))
    # print(len(Mtour_live))
    # print(len(Mtypes_live))

    # print(len(match_id_live))
    # print(len(match_id))
    # print(len(Mlinks))
    # print(len(T1names))
    # print(len(T2names))
    # print(len(T1logos))
    # print(len(T2logos))
    # print(len(Mtime))
    # print(len(Mtour))
    # print(len(Mtypes))
