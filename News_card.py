import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
import uuid
import os
from app import dash_app
import pandas as pd
import Live_matches
import Main_page

main_path_data = os.path.abspath("./data")



def news_items():
    newsBD = pd.read_csv(main_path_data + '\\news.csv')
    cards = []


    for ind in newsBD.index:
        ##########################    NEWS CARD   ###################################
        news_item = dbc.ListGroupItem(
            href='/news/{}'.format(newsBD['Mid'][ind]),
            id={'type': 'news-card',
                'index': str(newsBD['Mid'][ind])},
            style={'padding': '0px', 'margin-bottom':"10px",
                   'margin-top':"10px",
                   'border': 'none'},
            children=[ddk.Card(style={'background-color': '#073642',
                                      'max-height': '100px', 'min-height': '100px',
                                      'overflowY': 'hidden', 'text-align': 'center',
                                      'margin': '0', 'padding': '0px'},
                               card_hover=True,
                               children=[ddk.CardHeader(newsBD['name'][ind],
                                                        style={'text-align': 'left', 'font-size': '12px',
                                                               'height': '40px',
                                                               'max-height':'40px', 'overflow-y':'hidden',
                                                               'background-color': 'transparent', }),
                                         html.H6(
                                             newsBD['disc'][ind],
                                             style={'margin': '0', 'padding-bottom': '5px',
                                                    'color':'lightslategrey'})])])

        cards.append(news_item)
    return cards


##########################    ONE MATCH CARD   ##############################
def news_page(id):

    all_cardsBD = pd.read_csv(main_path_data + '\\news.csv')
    # print(" id from NEWS :", id)

    # id = id.replace("news/", "")
    df = all_cardsBD[(all_cardsBD['Mid'].isin([int(id)]))]


    ##############     HEAD CARD of MATCH   ###################################
    news_head = ddk.Card(style={'width': '-webkit-fill-available',
                                 'min-height': '120px',
                                 'margin': '10px',
                                 'padding': '15px',
                                 'background-color': '#f9f9f91c'}, children=[
        ddk.Block(width=100, style={'height': 'fit-content', },
                  children=[html.H2(df.iloc[0]['name'], style={'text-align': 'left',
                                                               'font-size': '30px',
                                                                'text-color': 'azure',
                                                                'margin': '0'})]),
        ddk.Block(width=100, style={'max-height': 'fit-content', 'margin-bottom': '20px',},
                  children=[html.P('{}'.format(df.iloc[0]['date']), style={'text-align': 'left','margin': '0'})]),
        ddk.Block(width=100, style={'max-height': 'fit-content'},
                  children=[html.P('{}'.format(df.iloc[0]['disc']), style={'text-align': 'left', 'margin': '0'})]),

    ])




    match_card = ddk.Block(width=100, style={'height': '93vh',
                             'text-align':'center'}, children=[
                          ddk.Block(width=70,
                                    style={'height':'89vh', 'margin':'0', 'padding':'0',
                                           'color':'azure', 'overflowY': 'scroll', 'overflowX': 'hidden', },
                                    children=[news_head

                                        # ddk.Card(style={'width':'-webkit-fill-available',
                                        #                 'margin':'10px', 'padding':'0',
                                        #                 'background-color': '#f9f9f91c',},
                                        #          children=news_head),


                                    ]),
                          ddk.Block(width=30,
                                    style={'height':'90vh'},
                                    children=[ddk.Card(width=100,
                                                       style={'background-color': 'transparent',
                                                              'max-height':'40vh', 'min-height':'40vh',
                                                              'padding-bottom':'5px',
                                                              'padding':'0','overflowY': 'hidden', 'margin':'10px'},
                                                       children=[
                                                           ddk.CardHeader(title='Live',
                                                                          style={'background-color': 'transparent'}),
                                                           Live_matches.live_list()]),
                                              ddk.Card(width=100,
                                                       id='match_sample_right',
                                                       style={'background-color': 'transparent',
                                                              'max-height':'45vh', 'min-height':'45vh',
                                                              'padding-bottom': '5px',
                                                              'padding':'0','overflowY': 'hidden','margin': '10px'},
                                                       children=[
                                                           ddk.CardHeader(title='Matches',
                                                                          style={'background-color': 'transparent'}),
                                                           Main_page.main_page()])
                                              ])])

    return match_card