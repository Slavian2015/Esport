import pandas as pd
import numpy as np
import Card_parser



##################################   SHOW ALL ROWS & COLS   ####################################
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)
# pd.set_option('max_colwidth', -1)


refreshBD = pd.read_csv('refresh.csv')
serverBD = pd.read_csv('server.csv')
all_cardsBD = pd.read_csv('all_cards.csv')
all_h2hBD = pd.read_csv('all_h2h.csv')
all_t1BD = pd.read_csv('all_t1.csv')
all_t2BD = pd.read_csv('all_t2.csv')



#######################   BD CHANGES   #####################################

df_new_items = refreshBD.loc[~refreshBD['match_id'].isin(serverBD['match_id'])]
# print(df_new_items)
df_old_items = serverBD.loc[~serverBD['match_id'].isin(refreshBD['match_id'])]

if df_old_items.shape[0] > 0:
    serverBD = serverBD.set_index("match_id")
    serverBD = serverBD.drop(df_old_items['match_id'], axis=0)
    serverBD = serverBD.reset_index()
    serverBD.to_csv('all_cards.csv', index=False, header=True)
else:
    pass

#############   Create Mcard and add to All_Cards  ##########################

if df_new_items.shape[0] > 0:
    for i in df_new_items['Mlinks']:
        dt = df_new_items[(df_new_items['Mlinks'].isin([i]))]

        result = Card_parser.newCard(i, dt.iloc[0]['match_id'])

        all_cardsBD = all_cardsBD.append(result[0], ignore_index=True, sort=False)
        all_h2hBD = all_h2hBD.append(result[1], ignore_index=True, sort=False)
        all_t1BD = all_t1BD.append(result[2], ignore_index=True, sort=False)
        all_t2BD = all_t2BD.append(result[3], ignore_index=True, sort=False)

    all_cardsBD.to_csv('all_cards.csv', index=False, header=True)
    all_h2hBD.to_csv('all_h2h.csv', index=False, header=True)
    all_t1BD.to_csv('all_t1.csv', index=False, header=True)
    all_t2BD.to_csv('all_t2.csv', index=False, header=True)

else:
    pass