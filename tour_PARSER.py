from bs4 import BeautifulSoup
import requests as req
import pandas as pd
import os



##################################   SHOW ALL ROWS & COLS   ####################################
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)
# pd.set_option('max_colwidth', -1)

main_path_data = os.path.abspath("./data")



def new_refresh():
    resp = req.get('https://ru.dltv.org/events')
    soup = BeautifulSoup(resp.text, 'lxml')


    # with open(main_path_data + "\\events.html", "r", encoding='utf-8') as f:
    #     contents = f.read()
    #     soup = BeautifulSoup(contents, 'lxml')

    TourLink = []
    TourName = []
    TourCountry = []
    TourFlagLink = []
    TourTeams = []
    TourPrize = []
    TourType = []
    TourDateFrom = []
    TourDateTo = []


    for rows in soup.find_all("div", attrs={"class": "event-list-slide"}):
        for na in rows.find_all("a", attrs={"class": "abs-link"}):
            TourLink.append(na.get('href'))                                     #shows:  ALL TOUR LINKS

        for na in rows.find_all("div", attrs={"class": "event-cell"}):

            for i in na.find_all("div", attrs={"class": "wrap"}):
                for x in i.find_all("div", attrs={"class": "top"}):
                    TourName.append(x.text.replace('Nan', '').strip())          #shows:  ALL TOUR NAMES

                for id in i.find_all('img'):
                    TourFlagLink.append(id.get('src'))                          #shows:  ALL TOUR FLAGS

                for id in i.find_all('img'):
                    TourCountry.append(id.get('title'))                          #shows:  ALL TOUR COUNTRY


                for x in i.find_all("div", attrs={"class": "bottom"}):
                    TourType.append(x.text.replace('Nan', '').strip())          #shows:  ALL TOUR TYPE

                for x in i.find_all("div", attrs={"class": "date"}):
                    dates = x.text.replace('\n', '').replace(' ', '').strip()
                    TourDateFrom.append(dates[:10])                             #shows:  ALL TOUR DATES
                    TourDateTo.append(dates[11:])

        for na in rows.find_all("div", attrs={"class": "teams-cell"}):
            for i in na.find_all("div", attrs={"class": "top"}):

                datas = i.text.strip()
                # print(datas)
                if not datas:
                    TourTeams.append("Ended")
                else:
                    TourTeams.append(datas)                                      #shows:  ALL TOUR TEAMS



        for na in rows.find_all("div", attrs={"class": "prize-cell"}):
            for i in na.find_all("div", attrs={"class": "top"}):
                datas = i.text.strip()

                if not datas:
                    pass
                else:
                    # print(datas)
                    TourPrize.append(datas)                                      #shows:  ALL TOUR Prize

    TourTeams.append("Ended")
    # print(len(TourTeams))
    # print(TourTeams)

    dw = {'TourLink': TourLink,
          'TourName': TourName,
          'TourCountry': TourCountry,
          'TourFlagLink': TourFlagLink,
          'TourTeams': TourTeams,
          'TourPrize': TourPrize,
          'TourType': TourType,
          'TourDateFrom': TourDateFrom,
          'TourDateTo': TourDateTo}
    df1 = pd.DataFrame(data=dw)
    # df1 = df.head(n=20)

    # df1['TIME'] = df1['Mdate'].astype(str) + ' ' + df1['Mtime'].astype(str)
    # df1['TIME'] = pd.to_datetime(df1['TIME'])
    # df1['TIME'] = df1['TIME'].dt.tz_localize('UTC').dt.tz_convert('Etc/GMT-3')
    # df1['Mdate'] = [d.date() for d in df1['TIME']]
    # df1['Mtime'] = [d.time() for d in df1['TIME']]

    df1.to_csv(main_path_data + '\\tours.csv', index=False, header=True)
    return df1

print(new_refresh())