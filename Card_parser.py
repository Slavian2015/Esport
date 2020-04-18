from bs4 import BeautifulSoup
import requests as req
import pandas as pd
import os


# ##################################   SHOW ALL ROWS & COLS   ####################################
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# pd.set_option('display.expand_frame_repr', False)
# # pd.set_option('max_colwidth', -1)

main_path_data = os.path.abspath("./data")

def newCard(link, mid):
# def newCard(link, '/332456'):

    print(link)

    resp = req.get(link, headers={'User-Agent': 'Mozilla'})
    soup = BeautifulSoup(resp.content, 'lxml')

    # print(soup.prettify())

    # with open("Match_card.html", "r", encoding='utf-8') as f:
    #     contents = f.read()
    #     soup = BeautifulSoup(contents, 'lxml')

    Mid = mid

    T1name = []
    T2name = []
    T1logo = []
    T2logo = []

    Mtime = []
    Mdate = []
    Mtour = []
    Mtypes = []
    Mstatus = []

    WR = []
    FB = []
    F10 = []

    WR2 = []
    FB2 = []
    F102 = []

    T1score = []
    T2score = []

    P11 = []
    P12 = []
    P13 = []
    P14 = []
    P15 = []

    P21 = []
    P22 = []
    P23 = []
    P24 = []
    P25 = []

    P11_photo = []
    P12_photo = []
    P13_photo = []
    P14_photo = []
    P15_photo = []

    P21_photo = []
    P22_photo = []
    P23_photo = []
    P24_photo = []
    P25_photo = []

    P11_score = []
    P12_score = []
    P13_score = []
    P14_score = []
    P15_score = []

    P21_score = []
    P22_score = []
    P23_score = []
    P24_score = []
    P25_score = []







##############################   FIRST  TEAM   ##################################################

    for rows in soup.find_all("div", attrs={"class": "personal-team-block personal-team__left"}):
        for id in rows.find_all('img'):
            T1logo.append(id.get('src').replace('Nan', '').strip())
            # print(id.get('src'))

        for id in rows.find_all("div", attrs={"class": "name"}):
            T1name.append(id.text.replace('\n', '').strip())
            # print(id.text.replace('\n', '').strip())

        for id in rows.find_all("div", attrs={"inf"}):

            data = []
            for i in id.find_all("div", attrs={"class": "percent"}):
                data.append(i.text.replace('\n', '').strip())
            WR.append(data[0])
            FB.append(data[1])
            F10.append(data[2])

        for id in rows.find_all("div", attrs={"score"}):
            T1score.append(id.text.replace('\n', '').strip())
            # print(id.text.replace('\n', '').strip())



##############################   SECOND  TEAM   ##################################################

    for rows in soup.find_all("div", attrs={"class": "personal-team-block personal-team__right"}):
        for id in rows.find_all('img'):
            T2logo.append(id.get('src').replace('Nan', '').strip())
            # print(id.get('src'))

        for id in rows.find_all("div", attrs={"class": "name"}):
            T2name.append(id.text.replace('\n', '').strip())
            # print(id.text.replace('\n', '').strip())

        for id in rows.find_all("div", attrs={"inf"}):

            data = []
            for i in id.find_all("div", attrs={"class": "percent"}):
                data.append(i.text.replace('\n', '').strip())
            WR2.append(data[0])
            FB2.append(data[1])
            F102.append(data[2])

        for id in rows.find_all("div", attrs={"score"}):
            T2score.append(id.text.replace('\n', '').strip())
            # print(id.text.replace('\n', '').strip())

##############################   STATUS  MATCH   ##################################################
    data222 = []
    for rows in soup.find_all("div", attrs={"class": "personal-team__info"}):

        for id in rows.find_all("div", attrs={"class": "personal-team__best mb-1"}):
            Mtypes.append(id.text.replace('\n', '').strip())
            # print(id.text.replace('\n', '').strip())



        for id in rows.find_all("div", attrs={"class": "mb-1"}):
            data222.append(id.text.replace('\n', '').strip())


        for id in rows.find_all("div", attrs={"class": "head"}):
            t = id.text.replace('\n', '').strip()
            t = t.split(' ')
            Mdate.append(t[0])
            Mtime.append(t[1])

    Mstatus.append(data222[1])

##############################   TOUR  MATCH   ##################################################

    for rows in soup.find_all("div", attrs={"class": "personal-match-head"}):
        Mtour.append(rows.text.replace('\n', '').strip())


##############################   PHOTOS of  TEAMS   ##################################################

    def check(list):
        if len(list) < 5:
            list.append("")
            if len(list) < 5:
                list.append("")
                if len(list) < 5:
                    list.append("")
                    if len(list) < 5:
                        list.append("")
                        if len(list) < 5:
                            list.append("")
        return

    gdp_table = soup.find("table", attrs={"class": "table player-stat"})
    gdp_table_data = gdp_table.tbody.find_all("tr")

    T1data = []
    for td in gdp_table_data[2].find_all("a"):
        T1data.append(td.text.replace('\n', '').strip())

    check(T1data)

    L1data = []
    for td in gdp_table_data[1].find_all("img"):
        L1data.append(td.get('src'))
    check(L1data)

    B1data = []
    for td in gdp_table_data[3].find_all("td"):
        B1data.append(td.text.replace('\n', '').strip())

    check(B1data)

    P11.append(T1data[0])
    P12.append(T1data[1])
    P13.append(T1data[2])
    P14.append(T1data[3])
    P15.append(T1data[4])

    P11_photo.append(L1data[0])
    P12_photo.append(L1data[1])
    P13_photo.append(L1data[2])
    P14_photo.append(L1data[3])
    P15_photo.append(L1data[4])

    P11_score.append(B1data[0])
    P12_score.append(B1data[1])
    P13_score.append(B1data[2])
    P14_score.append(B1data[3])
    P15_score.append(B1data[4])



    T2data = []
    for td in gdp_table_data[7].find_all("a"):
        T2data.append(td.text.replace('\n', '').strip())

    print(T2data)
    check(T2data)

    print(T2data)
    L2data = []
    for td in gdp_table_data[6].find_all("img"):
        L2data.append(td.get('src'))
    check(L2data)

    B2data = []
    for td in gdp_table_data[8].find_all("td"):
        B2data.append(td.text.replace('\n', '').strip())
    check(B2data)

    P21.append(T2data[0])
    P22.append(T2data[1])
    P23.append(T2data[2])
    P24.append(T2data[3])
    P25.append(T2data[4])

    print(P21, P22, P23, P24, P25)

    P21_photo.append(L2data[0])
    P22_photo.append(L2data[1])
    P23_photo.append(L2data[2])
    P24_photo.append(L2data[3])
    P25_photo.append(L2data[4])

    P21_score.append(B2data[0])
    P22_score.append(B2data[1])
    P23_score.append(B2data[2])
    P24_score.append(B2data[3])
    P25_score.append(B2data[4])




##############################   STAT of  TEAMS   ##################################################
    T1_last_time = []
    T1_last_date = []
    T1_last_name = []
    T1_last_logo = []
    T1_last_total_main = []
    T1_last_total_vs = []

    T2_last_time = []
    T2_last_date = []
    T2_last_name = []
    T2_last_logo = []
    T2_last_total_main = []
    T2_last_total_vs = []


    for rows in soup.find_all("div", attrs={"class": "container pastMatches"}):
        Tstat = rows.find_all("div", attrs={"class": "col-md-6"})

        for id in Tstat[0].find_all("div", attrs={"class": "event-box-inner"}):
            for i in id.find_all("div", attrs={"class": "past-matches-cup"}):
                data = i.text.replace('\n', '').strip()
                data = data.split(' ')

                T1_last_date.append(data[0])
                T1_last_time.append(data[1])


            for i in id.find_all("div", attrs={"class": "past-matches-name"}):
                T1_last_name.append(i.text.replace('\n', '').strip())

            for i in id.find_all('img', attrs={"class": "image-logo lazy", "alt":"Logo team"}):
                T1_last_logo.append(i.get('data-src'))

            for i in id.find_all("div", attrs={"class": "past-matches-total"}):
                for ii in i.find_all("a"):
                    h2h2 = ii.text.replace('\n', '').replace(' ', '').strip()
                    t1 = h2h2[:1]
                    t2 = h2h2[-1:]
                    T1_last_total_main.append(t1)
                    T1_last_total_vs.append(t2)




        for id in Tstat[1].find_all("div", attrs={"class": "event-box-inner"}):
            for i in id.find_all("div", attrs={"class": "past-matches-cup"}):
                data = i.text.replace('\n', '').strip()
                data = data.split(' ')

                T2_last_date.append(data[0])
                T2_last_time.append(data[1])

            for i in id.find_all("div", attrs={"class": "past-matches-name"}):
                T2_last_name.append(i.text.replace('\n', '').strip())

            for i in id.find_all('img', attrs={"class": "image-logo lazy", "alt":"Logo team"}):
                T2_last_logo.append(i.get('data-src'))

            for i in id.find_all("div", attrs={"class": "past-matches-total"}):
                for ii in i.find_all("a"):
                    h2h2 = ii.text.replace('\n', '').replace(' ', '').strip()
                    t1 = h2h2[:1]
                    t2 = h2h2[-1:]
                    T2_last_total_main.append(t1)
                    T2_last_total_vs.append(t2)



##############################   HEAD 2  HEAD   ##################################################

    H2H_time = []
    H2H_date = []
    H2H_total_t1 = []
    H2H_total_t2 = []
    for rows in soup.find_all("div", attrs={"class": "event-box-inner headToHead-content"}):
        for id in rows.find_all("div", attrs={"class": "head-matches-cup"}):
            date = id.text.replace('\n', '').strip()
            date2 = date.split(' ')

            H2H_time.append(date2[1])
            H2H_date.append(date2[0])


        for id in rows.find_all("div", attrs={"class": "past-matches-total"}):
            h2h2 = id.text.replace('\n', '').replace(' ', '').strip()
            t1 = h2h2[:1]
            t2 = h2h2[-1:]
            H2H_total_t1.append(t1)
            H2H_total_t2.append(t2)





    dw = {
        'Mid': Mid,
        'T1name': T1name,
          'T2name': T2name,
          'T1logo': T1logo,
          'T2logo': T2logo,

          'Mstatus': Mstatus,
          'T1score': T1score,
          'T2score': T2score,

          'Mdate': Mdate,
          'Mtime': Mtime,
          'Mtour': Mtour,
          'Mtypes': Mtypes,


          'WR': WR,
          'FB': FB,
          'F10': F10,

          'WR2': WR2,
          'FB2': FB2,
          'F102': F102,

          'P11': P11,
          'P12': P12,
          'P13': P13,
          'P14': P14,
          'P15': P15,

          'P21': P21,
          'P22': P22,
          'P23': P23,
          'P24': P24,
          'P25': P25,
          'P11_photo': P11_photo,
          'P12_photo': P12_photo,
          'P13_photo': P13_photo,
          'P14_photo': P14_photo,
          'P15_photo': P15_photo,
          'P21_photo': P21_photo,
          'P22_photo': P22_photo,
          'P23_photo': P23_photo,
          'P24_photo': P24_photo,
          'P25_photo': P25_photo,
          'P11_score': P11_score,
          'P12_score': P12_score,
          'P13_score': P13_score,
          'P14_score': P14_score,
          'P15_score': P15_score,
          'P21_score': P21_score,
          'P22_score': P22_score,
          'P23_score': P23_score,
          'P24_score': P24_score,
          'P25_score': P25_score,

          }
    df = pd.DataFrame(data=dw)
    # print(df)
    # df.to_csv('all_cards.csv', index=False, header=True)


    dwt1 = {
        'Mid': Mid,
        'T1_last_date': T1_last_date,
        'T1_last_time': T1_last_time,
        'T1_last_name': T1_last_name,
        'T1_last_logo': T1_last_logo,
        'T1_last_total_main': T1_last_total_main,
        'T1_last_total_vs': T1_last_total_vs,
        }

    dft1 = pd.DataFrame(data=dwt1)
    # dft1.to_csv('all_t1.csv', index=False, header=True)
    # print(dft1)

    dwt2 = {
        'Mid': str(Mid),
        'T2_last_date': T2_last_date,
        'T2_last_time': T2_last_time,
        'T2_last_name': T2_last_name,
        'T2_last_logo': T2_last_logo,
        'T2_last_total_main': T2_last_total_main,
        'T2_last_total_vs': T2_last_total_vs,
        }

    dft2 = pd.DataFrame(data=dwt2)
    # dft2.to_csv('all_t2.csv', index=False, header=True)
    # print(dft2)

    dwh2h = {
        'Mid': str(Mid),
        'H2H_date': H2H_date,
        'H2H_time': H2H_time,
        'H2H_total_t1': H2H_total_t1,
        'H2H_total_t2': H2H_total_t2,
        }

    dfh2h = pd.DataFrame(data=dwh2h)
    # dfh2h.to_csv('all_h2h.csv', index=False, header=True)
    # print(dfh2h)



    return df, dfh2h, dft1, dft2
