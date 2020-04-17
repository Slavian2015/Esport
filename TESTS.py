import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
import uuid
import os
from app import dash_app
from Structure import serverBD
import pandas as pd

# all_cardsBD = pd.read_csv('all_cards.csv')
#
tt = "/370614"
id = tt.replace("/", "")
#
# df = all_cardsBD[(all_cardsBD['Mid'].isin([id]))]
#
# print(df)
#
# print(df.iloc[0]['Mtour'])


# all_h2hBD = pd.read_csv('all_h2h.csv')
# h2hdf = all_h2hBD[(all_h2hBD['Mid'].isin(['370614']))]
#
# print(h2hdf)
#
# # print(h2hdf.groupby('H2H_total_t1').count())
#
#
# www = h2hdf['H2H_total_t1'].value_counts()
# www2 = h2hdf['H2H_total_t2'].value_counts()
#
# tt = [www,www2]
#
# print("www[2]  :",tt[0][2])


all_t1BD = pd.read_csv('all_t1.csv')
t1bd = all_t1BD[(all_t1BD['Mid'].isin([id]))]

all_t2BD = pd.read_csv('all_t2.csv')
t2bd = all_t2BD[(all_t2BD['Mid'].isin([id]))]


df = pd.concat([t1bd, t2bd.reindex(t1bd.index)], axis=1)

print(df)


