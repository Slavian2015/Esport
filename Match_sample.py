import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
import os
import pandas as pd
import Main_page
import Match_Score_Teble


main_path_data = os.path.abspath("./data")


##############     CHART SCORE TABLES    ###################################
chart_table = ddk.Card(style={'width':'-webkit-fill-available',
                              'margin':'10px', 'padding':'0',
                              'background-color': '#f9f9f91c'},
                       children=ddk.Block(width=100,
                                          style={'justify-content': 'center',
                                               'vertical-align': '-webkit-baseline-middle',
                                               'height': '250px',
                                               'width': '100%'}, children=[ddk.Logo(src='\\assets\\png\\charts.png',
                                                        style={
                                                             'max-height': '-webkit-fill-available',
                                                             'height': '-webkit-fill-available',
                                                             'width': '100%',
                                                            'text-align': 'left',
                                                             'padding': '0px', 'margin': '0',
                                                             'vertical-align': '-webkit-baseline-middle'})]))


##########################    ONE MATCH CARD   ##############################
def match_card(id):

    all_cardsBD = pd.read_csv(main_path_data + '\\all_cards.csv')
    id = id.replace("/", "")
    df = all_cardsBD[(all_cardsBD['Mid'].isin([id]))]

    time = df.iloc[0]['Mtime']

    ##############     HEAD CARD of MATCH   ###################################
    match_head = ddk.Card(style={'width': '-webkit-fill-available',
                                 'min-height': '120px',
                                 'margin': '10px',
                                 'padding': '10px',
                                 'background-color': '#f9f9f91c',
                                 'text-align': '-webkit-center'}, children=[
        dbc.Row(
            # width=100,
            style={'height': 'fit-content', 'justify-content': 'center'},
                  children=[html.H2(df.iloc[0]['Mtour'], style={'text-align': 'center',
                                                                'text-color': 'azure',
                                                                'margin': '0'})]),
        dbc.Row(
            # width=100,
            style={'max-height': 'fit-content', 'justify-content': 'center','padding': '5px',},
                  children=[html.H6('{} {}'.format(df.iloc[0]['Mdate'], time[0:5]),
                                    style={'text-align': 'center', 'margin': '0'})]),

        dbc.Row(style={'text-align': 'center',
                       'margin': '0',
                       'padding': '0',
                       'width':'100%',
                       'justify-content': 'center'},
                children=[
        dbc.Col(
            # width=40,
                style={'width': '40%',
                       'max-height': 'fit-content',
                       'padding': '0',
                       # 'min-width':'fit-content',
                       'max-width':'fit-content'
                       },
                children=dbc.Row(
                    style={'width': '100%',
                           'margin': '0',
                           # 'padding': '0',
                           # 'text-align': 'center',
                           'justify-content': 'center'
                           },
                children=[
                          dbc.Col(
                              # width=70,
                                  style={'width': '70%',
                                         'justify-content': 'center',
                                         'padding': '0',
                                         # 'min-width':'fit-content'
                                         },
                                    children=[
                              dbc.Row(style={'margin': '0',
                                             'padding': '0',
                                             'justify-content': 'right'},
                                  # width=100,
                                        children=html.H2(df.iloc[0]['T1name'],
                                                         style={
                                                             'text-align': 'right', 'margin': '0'})),
                              dbc.Row(style={'margin': '0',
                                             # 'padding': '0',
                                             'justify-content': 'right'},
                                  # width=100,
                                        children=html.H6('{}, {}, {}, {}, {}'.format(df.iloc[0]['P11'],
                                                                                     df.iloc[0]['P12'],
                                                                                     df.iloc[0]['P13'],
                                                                                     df.iloc[0]['P14'],
                                                                                     df.iloc[0]['P15']),
                                                         style={
                                                             'text-align': 'right', 'margin': '0'}))]),
                          dbc.Col(
                              # width=30,
                                    style={'width': '30%',
                                           'max-height': '40px',
                                           'padding': '0',
                                           # 'max-width': '40px',
                                           # 'margin-left': '15px',
                                           # 'min-width':'fit-content'
                                           },
                                    children=[
                                        ddk.Logo(src=df.iloc[0]['T1logo'],
                                                 style={
                                                     'max-height': '40px',
                                                     'height': '40px',
                                                     # 'width': '40px',
                                                     'text-align': 'center',
                                                     'padding': '0px', 'margin': '0',
                                                     'vertical-align': '-webkit-baseline-middle'})
                                    ])])),




        dbc.Col(
            # width=20,
                style={'width': '20%',
                       'max-height': 'fit-content',
                       'padding': '0',
                       'min-width':'fit-content',
                       'max-width':'fit-content'
                       },
                children=[dbc.Row(
                    # width=100,
                                    style={'margin': '0', 'padding': '0', 'justify-content': 'center' },
                                    children=[html.H1('{} : {}'.format(df.iloc[0]['T1score'], df.iloc[0]['T2score']),
                                                        style={'text-align': 'center', 'font-size': '40px',
                                                               'margin': '0'})]),
                          dbc.Row(
                              # width=100,
                                    style={'margin': '0', 'padding': '0',
                                                     'text-align': 'center',
                                             'max-height': '50px', 'justify-content': 'center',
                                             'height': '50px'},
                                    children=html.A(
                                        style={'text-align': 'center', 'justify-content': 'center'},
                                          id={'type': 'video_btn',
                                              'index': id},
                                          # n_clicks=0,
                                          children=[ddk.Logo(
                                          src='../assets/png/play.png',
                                          style={'text-align': 'center', 'justify-content': 'center',
                                                 'max-height': '-webkit-fill-available',
                                                 'padding': '0px', 'margin': '0',
                                                 'vertical-align': '-webkit-baseline-middle'})]))

                            ]),





        dbc.Col(
            # width=40,
                style={'width': '40%',
                       'max-height': 'fit-content',
                       'padding': '0',
                       # 'min-width':'fit-content',
                       'max-width':'fit-content'
                       },
                children=dbc.Row(
                    style={'width': '100%',
                           'margin': '0',
                        # 'margin': '0', 'padding': '0',
                           'justify-content': 'center', },

                    children=[
                          dbc.Col(
                              # width=30,
                                    style={'max-height': '40px','width': '30%',
                                           # 'margin': '0',
                                           'padding': '0',
                                           # 'max-width': '40px', 'margin-right': '15px',
                                           # 'min-width':'fit-content',
                                           'justify-content': 'left'},
                                    children=[
                                        ddk.Logo(src=df.iloc[0]['T2logo'],
                                                 style={
                                                     'max-height': '40px',
                                                     'text-align': 'center',
                                                     'height': '40px',
                                                     # 'width': '40px',
                                                     'padding': '0px', 'margin': '0',
                                                     'vertical-align': '-webkit-baseline-middle'})
                                    ]),
                          dbc.Col(
                              # width=70,
                                  style={'width': '70%',
                                         'margin': '0',
                                         # 'padding': '0',
                                         },
                                  children=[
                              dbc.Row(style={'margin': '0', 'padding': '0', 'justify-content': 'left'},
                                  # width=100,
                                  children=html.H2(df.iloc[0]['T2name'],
                                                                    style={'text-align': 'left', 'margin': '0'})),
                              dbc.Row(style={'margin': '0', 'padding': '0', 'justify-content': 'left'},
                                  # width=100,
                                      children=html.H6('{}, {}, {}, {}, {}'.format(df.iloc[0]['P21'],
                                                                                                df.iloc[0]['P22'],
                                                                                                df.iloc[0]['P23'],
                                                                                                df.iloc[0]['P24'],
                                                                                                df.iloc[0]['P25']),
                                                                    style={'text-align': 'left', 'margin': '0'})),

                          ]),

        ]))])
    ])





    ###################  TEAMS CARD of MATCH  #################################
    live_teams = ddk.Card(style={'width': '-webkit-fill-available',
                                 'margin': '10px',
                                 'padding': '0',
                                 'background-color': '#f9f9f91c'}, children=[
        ddk.Block(width=100,
                  style={'height': 'fit-content', 'vertical-align': '-webkit-baseline-middle'},
                  children=[ddk.Block(width=40,
                                      style={'height': 'fit-content'},
                                      children=[ddk.Block(width=20, style={
                                          'height': 'fit-content'}, children=[
                                          ddk.Block(width=100,
                                                    style={
                                                        'max-height': '50px',
                                                        'height': '50px',
                                                        'width': 'fit-content'},
                                                    children=[ddk.Logo(
                                                        src=df.iloc[0]['P11_photo'],
                                                        style={
                                                            'text-align': 'center',
                                                            'max-height': '50px',
                                                            'padding': '0px',
                                                            'margin': '0',
                                                            'vertical-align': '-webkit-baseline-middle'})]),
                                          ddk.Block(width=100, style={
                                              'max-width': '100px',
                                              'height': 'fit-content'},
                                                    children=[
                                                        html.H6(df.iloc[0]['P11'],
                                                                style={
                                                                    'text-align': 'center',
                                                                    'margin': '0'})]),
                                          ddk.Block(width=100, style={
                                              'max-width': '100px',
                                              'height': 'fit-content'},
                                                    children=[html.P(df.iloc[0]['P11_score'],
                                                                     style={
                                                                         'text-align': 'center',
                                                                         'margin': '0'})])]),
                                                ddk.Block(width=20, style={
                                                    'height': 'fit-content'},
                                                          children=[ddk.Block(
                                                              width=100,
                                                              style={
                                                                  'max-height': '50px',
                                                                  'height': '50px',
                                                                  'width': 'fit-content'},
                                                              children=[
                                                                  ddk.Logo(
                                                                      src=df.iloc[0]['P12_photo'],
                                                                      style={
                                                                          'text-align': 'center',
                                                                          'max-height': '50px',
                                                                          'padding': '0px',
                                                                          'margin': '0',
                                                                          'vertical-align': '-webkit-baseline-middle'})]),
                                                              ddk.Block(
                                                                  width=100,
                                                                  style={
                                                                      'max-width': '100px',
                                                                      'height': 'fit-content'},
                                                                  children=[
                                                                      html.H6(
                                                                          df.iloc[0]['P12'],
                                                                          style={
                                                                              'text-align': 'center',
                                                                              'margin': '0'})]),
                                                              ddk.Block(
                                                                  width=100,
                                                                  style={
                                                                      'max-width': '100px',
                                                                      'height': 'fit-content'},
                                                                  children=[
                                                                      html.P(
                                                                          df.iloc[0]['P12_score'],
                                                                          style={
                                                                              'text-align': 'center',
                                                                              'margin': '0'})])]),
                                                ddk.Block(width=20, style={
                                                    'height': 'fit-content'},
                                                          children=[ddk.Block(
                                                              width=100,
                                                              style={
                                                                  'max-height': '50px',
                                                                  'height': '50px',
                                                                  'width': 'fit-content'},
                                                              children=[
                                                                  ddk.Logo(
                                                                      src=df.iloc[0]['P13_photo'],
                                                                      style={
                                                                          'text-align': 'center',
                                                                          'max-height': '50px',
                                                                          'padding': '0px',
                                                                          'margin': '0',
                                                                          'vertical-align': '-webkit-baseline-middle'})]),
                                                              ddk.Block(
                                                                  width=100,
                                                                  style={
                                                                      'max-width': '100px',
                                                                      'height': 'fit-content'},
                                                                  children=[
                                                                      html.H6(
                                                                          df.iloc[0]['P13'],
                                                                          style={
                                                                              'text-align': 'center',
                                                                              'margin': '0'})]),
                                                              ddk.Block(
                                                                  width=100,
                                                                  style={
                                                                      'max-width': '100px',
                                                                      'height': 'fit-content'},
                                                                  children=[
                                                                      html.P(
                                                                          df.iloc[0]['P13_score'],
                                                                          style={
                                                                              'text-align': 'center',
                                                                              'margin': '0'})])]),
                                                ddk.Block(width=20, style={
                                                    'height': 'fit-content'},
                                                          children=[ddk.Block(
                                                              width=100,
                                                              style={
                                                                  'max-height': '50px',
                                                                  'height': '50px',
                                                                  'width': 'fit-content'},
                                                              children=[
                                                                  ddk.Logo(
                                                                      src=df.iloc[0]['P14_photo'],
                                                                      style={
                                                                          'text-align': 'center',
                                                                          'max-height': '50px',
                                                                          'padding': '0px',
                                                                          'margin': '0',
                                                                          'vertical-align': '-webkit-baseline-middle'})]),
                                                              ddk.Block(
                                                                  width=100,
                                                                  style={
                                                                      'max-width': '100px',
                                                                      'height': 'fit-content'},
                                                                  children=[
                                                                      html.H6(
                                                                          df.iloc[0]['P14'],
                                                                          style={
                                                                              'text-align': 'center',
                                                                              'margin': '0'})]),
                                                              ddk.Block(
                                                                  width=100,
                                                                  style={
                                                                      'max-width': '100px',
                                                                      'height': 'fit-content'},
                                                                  children=[
                                                                      html.P(
                                                                          df.iloc[0]['P14_score'],
                                                                          style={
                                                                              'text-align': 'center',
                                                                              'margin': '0'})])]),
                                                ddk.Block(width=20, style={
                                                    'height': 'fit-content'},
                                                          children=[ddk.Block(
                                                              width=100,
                                                              style={
                                                                  'max-height': '50px',
                                                                  'height': '50px',
                                                                  'width': 'fit-content'},
                                                              children=[
                                                                  ddk.Logo(
                                                                      src=df.iloc[0]['P15_photo'],
                                                                      style={
                                                                          'text-align': 'center',
                                                                          'max-height': '50px',
                                                                          'padding': '0px',
                                                                          'margin': '0',
                                                                          'vertical-align': '-webkit-baseline-middle'})]),
                                                              ddk.Block(
                                                                  width=100,
                                                                  style={
                                                                      'max-width': '100px',
                                                                      'height': 'fit-content'},
                                                                  children=[
                                                                      html.H6(
                                                                          df.iloc[0]['P15'],
                                                                          style={
                                                                              'text-align': 'center',
                                                                              'margin': '0'})]),
                                                              ddk.Block(
                                                                  width=100,
                                                                  style={
                                                                      'max-width': '100px',
                                                                      'height': 'fit-content'},
                                                                  children=[
                                                                      html.P(
                                                                          df.iloc[0]['P15_score'],
                                                                          style={
                                                                              'text-align': 'center',
                                                                              'margin': '0'})])]), ]),

                            ddk.Block(width=20,
                                      style={'height': '100px', 'vertical-align': '-webkit-baseline-middle',
                                             'padding': '10px'},
                                      children=[ddk.Block(width=100,
                                                          style={'height': '33%'},
                                                          children=[ddk.Block(width=30, style={'height': 'fit-content',
                                                                                               'vertical-align': 'middle'},
                                                                              children=[html.H6('{}'.format(df.iloc[0]['WR']), style={
                                                                                  'text-align': 'center',
                                                                                  'padding': '0px', 'margin': '0'})]),
                                                                    ddk.Block(width=40, style={'height': 'fit-content',
                                                                                               'vertical-align': 'middle'},
                                                                              children=[html.H2('WR', style={
                                                                                  'text-align': 'center',
                                                                                  'padding': '0px', 'margin': '0'})]),
                                                                    ddk.Block(width=30, style={'height': 'fit-content',
                                                                                               'vertical-align': 'middle'},
                                                                              children=[html.H6('{}'.format(df.iloc[0]['WR2']), style={
                                                                                  'text-align': 'center',
                                                                                  'padding': '0px', 'margin': '0'})])]),
                                                ddk.Block(width=100, style={'height': '33%'}, children=[
                                                    ddk.Block(width=30, style={'height': 'fit-content',
                                                                               'vertical-align': 'middle'}, children=[
                                                        html.H6('{}'.format(df.iloc[0]['FB']), style={'text-align': 'center', 'padding': '0px',
                                                                              'margin': '0'})]),
                                                    ddk.Block(width=40, style={'height': 'fit-content',
                                                                               'vertical-align': 'middle'}, children=[
                                                        html.H2('FB', style={'text-align': 'center', 'padding': '0px',
                                                                             'margin': '0'})]),
                                                    ddk.Block(width=30, style={'height': 'fit-content',
                                                                               'vertical-align': 'middle'}, children=[
                                                        html.H6('{}'.format(df.iloc[0]['FB2']), style={'text-align': 'center', 'padding': '0px',
                                                                              'margin': '0'})])]),
                                                ddk.Block(width=100, style={'height': '33%'}, children=[
                                                    ddk.Block(width=30, style={'height': 'fit-content',
                                                                               'vertical-align': 'middle'}, children=[
                                                        html.H6('{}'.format(df.iloc[0]['F10']), style={'text-align': 'center', 'padding': '0px',
                                                                              'margin': '0'})]),
                                                    ddk.Block(width=40, style={'height': 'fit-content',
                                                                               'vertical-align': 'middle'}, children=[
                                                        html.H2('F10', style={'text-align': 'center', 'padding': '0px',
                                                                              'margin': '0'})]),
                                                    ddk.Block(width=30, style={'height': 'fit-content',
                                                                               'vertical-align': 'middle'}, children=[
                                                        html.H6('{}'.format(df.iloc[0]['F102']), style={'text-align': 'center', 'padding': '0px',
                                                                              'margin': '0'})])])]),

                            ddk.Block(width=40,
                                      style={'height': 'fit-content'},
                                      children=[ddk.Block(width=20, style={
                                          'height': 'fit-content'}, children=[
                                          ddk.Block(width=100,
                                                    style={
                                                        'max-height': '50px',
                                                        'height': '50px',
                                                        'width': 'fit-content'},
                                                    children=[ddk.Logo(
                                                        src=df.iloc[0]['P21_photo'],
                                                        style={
                                                            'text-align': 'center',
                                                            'max-height': '50px',
                                                            'padding': '0px',
                                                            'margin': '0',
                                                            'vertical-align': '-webkit-baseline-middle'})]),
                                          ddk.Block(width=100, style={
                                              'max-width': '100px',
                                              'height': 'fit-content'},
                                                    children=[
                                                        html.H6(df.iloc[0]['P21'],
                                                                style={
                                                                    'text-align': 'center',
                                                                    'margin': '0'})]),
                                          ddk.Block(width=100, style={
                                              'max-width': '100px',
                                              'height': 'fit-content'},
                                                    children=[html.P(df.iloc[0]['P21_score'],
                                                                     style={
                                                                         'text-align': 'center',
                                                                         'margin': '0'})])]),
                                                ddk.Block(width=20, style={
                                                    'height': 'fit-content'},
                                                          children=[ddk.Block(
                                                              width=100,
                                                              style={
                                                                  'max-height': '50px',
                                                                  'height': '50px',
                                                                  'width': 'fit-content'},
                                                              children=[
                                                                  ddk.Logo(
                                                                      src=df.iloc[0]['P22_photo'],
                                                                      style={
                                                                          'text-align': 'center',
                                                                          'max-height': '50px',
                                                                          'padding': '0px',
                                                                          'margin': '0',
                                                                          'vertical-align': '-webkit-baseline-middle'})]),
                                                              ddk.Block(
                                                                  width=100,
                                                                  style={
                                                                      'max-width': '100px',
                                                                      'height': 'fit-content'},
                                                                  children=[
                                                                      html.H6(
                                                                          df.iloc[0]['P22'],
                                                                          style={
                                                                              'text-align': 'center',
                                                                              'margin': '0'})]),
                                                              ddk.Block(
                                                                  width=100,
                                                                  style={
                                                                      'max-width': '100px',
                                                                      'height': 'fit-content'},
                                                                  children=[
                                                                      html.P(
                                                                          df.iloc[0]['P22_score'],
                                                                          style={
                                                                              'text-align': 'center',
                                                                              'margin': '0'})])]),
                                                ddk.Block(width=20, style={
                                                    'height': 'fit-content'},
                                                          children=[ddk.Block(
                                                              width=100,
                                                              style={
                                                                  'max-height': '50px',
                                                                  'height': '50px',
                                                                  'width': 'fit-content'},
                                                              children=[
                                                                  ddk.Logo(
                                                                      src=df.iloc[0]['P23_photo'],
                                                                      style={
                                                                          'text-align': 'center',
                                                                          'max-height': '50px',
                                                                          'padding': '0px',
                                                                          'margin': '0',
                                                                          'vertical-align': '-webkit-baseline-middle'})]),
                                                              ddk.Block(
                                                                  width=100,
                                                                  style={
                                                                      'max-width': '100px',
                                                                      'height': 'fit-content'},
                                                                  children=[
                                                                      html.H6(
                                                                          df.iloc[0]['P23'],
                                                                          style={
                                                                              'text-align': 'center',
                                                                              'margin': '0'})]),
                                                              ddk.Block(
                                                                  width=100,
                                                                  style={
                                                                      'max-width': '100px',
                                                                      'height': 'fit-content'},
                                                                  children=[
                                                                      html.P(
                                                                          df.iloc[0]['P23_score'],
                                                                          style={
                                                                              'text-align': 'center',
                                                                              'margin': '0'})])]),
                                                ddk.Block(width=20, style={
                                                    'height': 'fit-content'},
                                                          children=[ddk.Block(
                                                              width=100,
                                                              style={
                                                                  'max-height': '50px',
                                                                  'height': '50px',
                                                                  'width': 'fit-content'},
                                                              children=[
                                                                  ddk.Logo(
                                                                      src=df.iloc[0]['P24_photo'],
                                                                      style={
                                                                          'text-align': 'center',
                                                                          'max-height': '50px',
                                                                          'padding': '0px',
                                                                          'margin': '0',
                                                                          'vertical-align': '-webkit-baseline-middle'})]),
                                                              ddk.Block(
                                                                  width=100,
                                                                  style={
                                                                      'max-width': '100px',
                                                                      'height': 'fit-content'},
                                                                  children=[
                                                                      html.H6(
                                                                          df.iloc[0]['P24'],
                                                                          style={
                                                                              'text-align': 'center',
                                                                              'margin': '0'})]),
                                                              ddk.Block(
                                                                  width=100,
                                                                  style={
                                                                      'max-width': '100px',
                                                                      'height': 'fit-content'},
                                                                  children=[
                                                                      html.P(
                                                                          df.iloc[0]['P24_score'],
                                                                          style={
                                                                              'text-align': 'center',
                                                                              'margin': '0'})])]),
                                                ddk.Block(width=20, style={
                                                    'height': 'fit-content'},
                                                          children=[ddk.Block(
                                                              width=100,
                                                              style={
                                                                  'max-height': '50px',
                                                                  'height': '50px',
                                                                  'width': 'fit-content'},
                                                              children=[
                                                                  ddk.Logo(
                                                                      src=df.iloc[0]['P25_photo'],
                                                                      style={
                                                                          'text-align': 'center',
                                                                          'max-height': '50px',
                                                                          'padding': '0px',
                                                                          'margin': '0',
                                                                          'vertical-align': '-webkit-baseline-middle'})]),
                                                              ddk.Block(
                                                                  width=100,
                                                                  style={
                                                                      'max-width': '100px',
                                                                      'height': 'fit-content'},
                                                                  children=[
                                                                      html.H6(
                                                                          df.iloc[0]['P25'],
                                                                          style={
                                                                              'text-align': 'center',
                                                                              'margin': '0'})]),
                                                              ddk.Block(
                                                                  width=100,
                                                                  style={
                                                                      'max-width': '100px',
                                                                      'height': 'fit-content'},
                                                                  children=[
                                                                      html.P(
                                                                          df.iloc[0]['P24_score'],
                                                                          style={
                                                                              'text-align': 'center',
                                                                              'margin': '0'})])]), ])]),
    ])



    ##############     H 2 H card items    ###################################

    def h2h():
        all_h2hBD = pd.read_csv(main_path_data + '\\all_h2h.csv')
        h2hdf = all_h2hBD[(all_h2hBD['Mid'].isin([id]))]



        shape = h2hdf.shape[0]
        h2h = []

        for ind in h2hdf.index:
            head_list = dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
                                                 'height': '40px', 'justify-content': 'center',
                                                 'vertical-align': '-webkit-baseline-middle',
                                                 'max-height': 'fit-content', 'padding': '0px',
                                                 # 'background-color':'#0e4e70',
                                                 'list-style': 'none',
                                                 'align-items': 'center'},
                                          children=ddk.Block(width=100,
                                                             style={'vertical-align': '-webkit-baseline-middle',
                                                                    'height': '35px'}, children=[
                                                  ddk.Block(width=20,
                                                            style={'vertical-align': '-webkit-baseline-middle'},
                                                            children=[
                                                                html.H2(h2hdf['H2H_total_t1'][ind], style={
                                                                    'vertical-align': '-webkit-baseline-middle',
                                                                    'text-align': 'center', 'margin': '0'})]),
                                                  ddk.Block(width=60,
                                                            style={'vertical-align': '-webkit-baseline-middle'},
                                                            children=[html.H6(h2hdf['H2H_date'][ind], style={
                                                                'vertical-align': '-webkit-baseline-middle',
                                                                'text-align': 'center', 'margin': '0'})]),
                                                  ddk.Block(width=20,
                                                            style={'vertical-align': '-webkit-baseline-middle'},
                                                            children=[
                                                                html.H2(h2hdf['H2H_total_t2'][ind], style={
                                                                    'vertical-align': '-webkit-baseline-middle',
                                                                    'text-align': 'center', 'margin': '0'})])]))

            h2h.append(head_list)


        dfr = h2hdf[(h2hdf['H2H_total_t1'] == 2)]
        dfr2 = h2hdf[(h2hdf['H2H_total_t2'] == 2)]

        if dfr.shape[0] > 0:
            www = h2hdf['H2H_total_t1'].value_counts()
        else:
            www = [[0], [0], [0]]

        if dfr2.shape[0] > 0:
            www2 = h2hdf['H2H_total_t2'].value_counts()
        else:
            www2 = [[0], [0], [0]]








        return h2h, shape, www, www2

    lhitem = h2h()
    head_to_head = ddk.Card(style={'width': '-webkit-fill-available',
                                   'margin': '10px',
                                   'padding': '0',
                                   'background-color': '#f9f9f91c'}, children=[
        ddk.Block(width=100, children=[ddk.Block(width=30, style={'vertical-align': '-webkit-baseline-middle', },
                                                 children=[ddk.Block(width=100, children=[
                                                     html.H6('Побед', style={'text-align': 'center', 'margin': '0'})]),
                                                           ddk.Block(width=100, children=[html.H2(lhitem[2][2], style={
                                                               'text-align': 'center', 'margin': '0'})])]),
                                       ddk.Block(width=40, style={'vertical-align': '-webkit-baseline-middle', },
                                                 children=[ddk.Card(shadow_weight='medium',
                                                                    style={'background-color': 'transparent'},
                                                                    children=[html.H2(lhitem[1],
                                                                                      style={'text-align': 'center',
                                                                                             'margin': '0'})])]),
                                       ddk.Block(width=30, style={'vertical-align': '-webkit-baseline-middle', },
                                                 children=[ddk.Block(width=100, children=[
                                                     html.H6('Побед', style={'text-align': 'center', 'margin': '0'})]),
                                                           ddk.Block(width=100, children=[html.H2(lhitem[3][2], style={
                                                               'text-align': 'center', 'margin': '0'})])])]),
        ddk.Block(width=100, children=dbc.ListGroup(flush=True,
                                                    children=[i for i in lhitem[0]]))])



    ##############     Total games card items    ##############################


    def totals():
        all_t1BD = pd.read_csv(main_path_data + '\\all_t1.csv')
        t1bd = all_t1BD[(all_t1BD['Mid'].isin([id]))]

        all_t2BD = pd.read_csv(main_path_data + '\\all_t2.csv')
        t2bd = all_t2BD[(all_t2BD['Mid'].isin([id]))]


        ttt = []
        total = pd.concat([t1bd, t2bd.reindex(t1bd.index)], axis=1)



        for ind in total.index:

            if total['T1_last_total_main'][ind] > total['T1_last_total_vs'][ind]:
                tr = '\\assets\\png\\w.png'
                pass
            else:
                tr = '\\assets\\png\\l.png'
                pass


            if total['T2_last_total_main'][ind] > total['T2_last_total_vs'][ind]:
                ty = '\\assets\\png\\w.png'
                pass
            else:
                ty = '\\assets\\png\\l.png'
                pass




            stat_list = dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
                                                 'height': '40px', 'justify-content': 'center',
                                                 'vertical-align': '-webkit-baseline-middle',
                                                 'max-height': 'fit-content', 'padding': '0px',
                                                 # 'background-color':'#0e4e70',
                                                 'list-style': 'none',
                                                 'align-items': 'center'}, children=ddk.Block(width=100,
                                       style={'vertical-align': '-webkit-baseline-middle',
                                              'height': '35px'},
                                       children=[
                                           ddk.Block(width=50,
                                                     style={'vertical-align': '-webkit-baseline-middle'},
                                                     children=[
                                                         ddk.Block(
                                                             width=25,
                                                             style={
                                                                 'max-height': '20px',
                                                                 'height': '20px',
                                                                 'width': 'fit-content'},
                                                             children=[ddk.Logo(
                                                                 src=total['T1_last_logo'][ind],
                                                                 style={
                                                                     'text-align': 'center',
                                                                     'max-height': '20px',
                                                                     'padding': '0',
                                                                     'margin': '0',
                                                                     'vertical-align': '-webkit-baseline-middle'})]),
                                                         ddk.Block(
                                                             width=25,
                                                             children=[html.H6('vs',
                                                                               style={'text-align': 'center', 'margin': '0'})]),
                                                         ddk.Block(
                                                             width=25,
                                                             style={
                                                                 'max-height': '20px',
                                                                 'height': '20px',
                                                                 'width': 'fit-content'},
                                                             children=[ddk.Logo(
                                                                 src=df.iloc[0]['T1logo'],
                                                                 style={
                                                                     'text-align': 'center',
                                                                     'max-height': '20px',
                                                                     'padding': '0',
                                                                     'margin': '0',
                                                                     'vertical-align': '-webkit-baseline-middle'})]),
                                                         ddk.Block(
                                                             width=25,
                                                             style={
                                                                 'max-height': '20px',
                                                                 'height': '20px',
                                                                 'width': 'fit-content'},
                                                             children=[ddk.Logo(
                                                                 src=tr,
                                                                 style={
                                                                     'text-align': 'center',
                                                                     'max-height': '20px',
                                                                     'padding': '0',
                                                                     'margin': '0',
                                                                     'margin-left': '10px',
                                                                     'vertical-align': '-webkit-baseline-middle'})])
                                                     ]),
                                           ddk.Block(width=50,
                                                     style={'vertical-align': '-webkit-baseline-middle'},
                                                     children=[
                                                         ddk.Block(
                                                             width=25,
                                                             style={
                                                                 'max-height': '20px',
                                                                 'height': '20px',
                                                                 'width': 'fit-content'},
                                                             children=[ddk.Logo(
                                                                 src=ty,
                                                                 style={
                                                                     'text-align': 'center',
                                                                     'max-height': '20px',
                                                                     'padding': '0',
                                                                     'margin': '0',
                                                                     'margin-right': '10px',
                                                                     'vertical-align': '-webkit-baseline-middle'})]),
                                                         ddk.Block(
                                                             width=25,
                                                             style={
                                                                 'max-height': '20px',
                                                                 'height': '20px',
                                                                 'width': 'fit-content'},
                                                             children=[ddk.Logo(
                                                                 src=df.iloc[0]['T2logo'],
                                                                 style={
                                                                     'text-align': 'center',
                                                                     'max-height': '20px',
                                                                     'padding': '0',
                                                                     'margin': '0',
                                                                     'vertical-align': '-webkit-baseline-middle'})]),
                                                         ddk.Block(
                                                             width=25,
                                                             children=[html.H6('vs',
                                                                               style={'text-align': 'center', 'margin': '0'})]),
                                                         ddk.Block(
                                                             width=25,
                                                             style={
                                                                 'max-height': '20px',
                                                                 'height': '20px',
                                                                 'width': 'fit-content'},
                                                             children=[ddk.Logo(
                                                                 src=total['T2_last_logo'][ind],
                                                                 style={
                                                                     'text-align': 'center',
                                                                     'max-height': '20px',
                                                                     'padding': '0',
                                                                     'margin': '0',
                                                                     'vertical-align': '-webkit-baseline-middle'})]),

                                                     ])]))

            ttt.append(stat_list)


        dfr = total[(total['T1_last_total_main'] == 2)]
        dfr2 = total[(total['T2_last_total_main'] == 2)]

        if dfr.shape[0] > 0:
            rew1 = total['T1_last_total_main'].value_counts()
        else:
            rew1 = [[0], [0], [0]]


        if dfr2.shape[0] > 0:
            rew2 = total['T2_last_total_main'].value_counts()
        else:
            rew2 = [[0], [0],[0]]


        return ttt, rew1, rew2



    rrr = totals()

    stat_teams = ddk.Card(style={'width': '-webkit-fill-available',
                                 'margin': '10px', 'padding': '0',
                                 'background-color': '#f9f9f91c', }, children=[
        ddk.Block(width=100, children=[ddk.Block(width=50, style={'vertical-align': '-webkit-baseline-middle', },
                                                 children=[ddk.Block(width=100, children=[
                                                     html.H6('Побед', style={'text-align': 'center', 'margin': '0'})]),
                                                           ddk.Block(width=100, children=[html.H2("{}".format(rrr[1][2]),
                                                                                                  style={
                                                               'text-align': 'center', 'margin': '0'})])]),

                                       ddk.Block(width=50, style={'vertical-align': '-webkit-baseline-middle', },
                                                 children=[ddk.Block(width=100, children=[
                                                     html.H6('Побед', style={'text-align': 'center', 'margin': '0'})]),
                                                           ddk.Block(width=100, children=[html.H2("{}".format(rrr[2][2]),
                                                                                                  style={
                                                               'text-align': 'center', 'margin': '0'})])])]),
        ddk.Block(width=100, children=dbc.ListGroup(flush=True, children=[i for i in rrr[0]]))

    ])


    #################   Statistics  #############################################
    stat = ddk.Block(width=100, style={'vertical-align': 'top'
                                       }, children=[
        ddk.Block(width=50,
                  style={'vertical-align': 'top'},
                  children=[head_to_head]),
        ddk.Block(width=50,
                  style={'vertical-align': 'top'},
                  children=[stat_teams])])




    ############################     TABS    ###################################
    first_tab = dcc.Tab(label="Live",
                        children=[live_teams,
                                  Match_Score_Teble.new_table(id, df.iloc[0]['T1name'], df.iloc[0]['T2name'])],
                        style={
                            # 'margin': '10px',
                                                                     'border-radius': '10px',
                                                                     'background-color': '#0e4e70', 'color': 'azure',
                                                                     'border': '1px solid rgb(14, 78, 112)'},
                        selected_style={
                            # 'margin': '10px',
                                        'border-radius': '10px',
                                        'background-color': '#0e4e70', 'color': 'azure', 'border': '2px solid #1f78b4'})
    second_tab = dcc.Tab(label="Statistics", children=[stat,
                                                       # chart_table
                                                       ], style={
        # 'margin': '10px',
                                                                            'border-radius': '10px',
                                                                            'background-color': '#0e4e70',
                                                                            'color': 'azure',
                                                                            'border': '1px solid rgb(14, 78, 112)'},
                         selected_style={
                             # 'margin': '10px',
                                         'border-radius': '10px', 'background-color': '#0e4e70', 'color': 'azure',
                                         'border': '2px solid #1f78b4'})
    tabs = dcc.Tabs(style={'width':'100%', 'padding-left':'5px',},children=[first_tab, second_tab])
        # dbc.Row(
        # style={'width':'100%', 'padding-left':'5px', 'padding-right':'5px'}, children=(
        #     dcc.Tabs(children=[first_tab, second_tab])
        # ))






    match_card = [ddk.Block(width=100,
                           style={'height': '90vh',
                             'text-align':'center'},
                           children=[
                          ddk.Block(width=70,
                                    style={'height':'90vh', 'margin':'0', 'padding':'0', 'color':'azure', 'overflowY': 'scroll', 'overflowX': 'hidden', },
                                    children=[
                                        match_head,
                                        ddk.Card(style={'width':'-webkit-fill-available', 'margin':'10px', 'padding':'0', 'background-color': '#f9f9f91c',},
                                                 children=tabs)]),
                          ddk.Block(width=30,
                                    style={'height':'93vh'},
                                    children=[ddk.Card(width=100,
                                                       id='match_sample_right',
                                                       style={'background-color': 'transparent', 'max-height':'89vh', 'min-height':'89vh', 'padding':'0','overflowY': 'hidden','margin': '10px'},
                                                       children=[
                                                           ddk.CardHeader(title='Matches', style={'background-color': 'transparent'}),
                                                           Main_page.main_page()])
                                              ])]),
                  dbc.Toast(
                      # "This toast is placed in the top right",
                      id={'type': 'video_div',
                          'index': id},
                      # header="Positioned toast",
                      is_open=False,
                      # width='640px',
                      # dismissable=True,
                      body_style={'margin':'0', 'padding':'0', 'max-width': '380px', 'overflow': 'hidden','max-height': '240px',
                             'min-width': '380px', 'min-height':'220px',},
                      header_style={'margin': '0', 'padding': '0'},
                        # icon="danger",
                      # top: 66 positions the toast below the navbar
                      style={'margin':'0', 'padding':'0', "position": "fixed", "top": 350, "right": 10,
                             # "width": '640px',
                             "maxWidth": "380px", "maxHeight": "240px",
                             'over-flowX':'hidden','over-flowY':'hidden',
                             'max-width': '380px', 'overflow': 'hidden','max-height': '240px',
                             'min-width': '380px', 'min-height':'220px',},
                      children=[


                            #   dcc.Markdown(f'''
                            # <iframe
                            #     src="https://player.twitch.tv/?channel={df.iloc[0]['Video']}&muted=true"
                            #     height="720"
                            #     width="1280"
                            #     frameborder="0"
                            #     scrolling="no"
                            #     allowfullscreen="true">
                            # </iframe>
                            # ''')


                          html.Iframe(
                              style={'frameborder':'0', 'overflowX':'hidden','overflowY':'hidden','margin':'0', 'padding':'0',
                                     "max-height": '230px', "min-height": '230px', "width": '230px',
                                     "max-width": '410px', "min-width": '410px',"height": '410px','border': '0'
                                     },
                              # src=f"https://player.twitch.tv/?channel={df.iloc[0]['Video']}",
                            # height="720",
                            # width="1280",
                            #   width='640px',
                          srcDoc=f'''
                            <iframe
                                src="https://player.twitch.tv/?channel={df.iloc[0]['Video']}&muted=true"
                                frameborder="0"
                                scrolling="yes"
                                height="200"
                                width="360"
                                allowfullscreen="true">
                            </iframe>
                              '''
                              # frameborder="<frameborder>",
                            #  scrolling=True,
                            #  allowfullscreen=True
                          )

                      ]

                  )]


    # dcc.Interval(id='interval', interval=60000, n_intervals=0)
    # print('id 3', id)
    return match_card

# def match_card(id):
#     ref_match = html.Div(id={'type':'session_match_div', 'index': id},
#                          children=[dcc.Interval(id={'type': 'interval_match', 'index': id}, interval=5000, n_intervals=0),match_card2(id)])
#     return ref_match
