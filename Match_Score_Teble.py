import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
import os
import pandas as pd




main_path_data = os.path.abspath("./data")


def new_table(Mid,Team1,Team2):
    live_scoreBD = pd.read_csv(main_path_data + '\\live_score.csv')
    filterBD = live_scoreBD[live_scoreBD["Mid"].isin([Mid])]

    Team1BD = filterBD.head(n=5)
    Team2BD = filterBD.tail(n=5)

    def team(TeamBD):

        score_table_item2 = []
        score_table_item2.append(dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
                                                                               'height': '40px', 'justify-content': 'center',
                                                                               'vertical-align': '-webkit-baseline-middle',
                                                                               'max-height': 'fit-content', 'padding': '0px',
                                                                               'background-color':'#0e4e70',
                                                                               'list-style': 'none','max-width':'100%',
                       'min-width':'700px',
                       #                                    'min-width':'1000px',
                       # 'overflowX':'scroll',
                                                                               'align-items': 'center'},
                                                   children=[
                                                       dbc.Row(
                                                           # width=100,
                                                                 style={'justify-content': 'center','margin': '0',
                                                                      'vertical-align': '-webkit-baseline-middle',
                                                                      'height': '40px'},
                                                                 children=[dbc.Col(
                                                                     # width=15,
                                                                                                             style={'min-width':'fit-content','vertical-align': '-webkit-baseline-middle','width':'15%','word-wrap': 'normal',},
                                                                                                             children=html.H2('PLAYER',style={'margin': '0',
                                                                                                                                           'text-align': 'center',
                                                                                                                                           'justify': 'center'})),
                                                                                                   dbc.Col(
                                                                                                       # width=15,
                                                                                                             style={'min-width':'fit-content','vertical-align': '-webkit-baseline-middle','width':'15%',},
                                                                                                             children=html.H2('HERO',style={'margin': '0',
                                                                                                                                           'text-align': 'center',
                                                                                                                                           'justify': 'center'})),
                                                                                                   dbc.Col(
                                                                                                       # width=10,
                                                                                                             style={'min-width':'fit-content','vertical-align': '-webkit-baseline-middle','width':'10%',},
                                                                                                             children=html.H2('KDA',style={'margin': '0',
                                                                                                                                           'text-align': 'center',
                                                                                                                                           'justify': 'center'})),
                                                                                                   dbc.Col(
                                                                                                       # width=20,
                                                                                                             style={'min-width':'fit-content','vertical-align': '-webkit-baseline-middle','width':'20%',},
                                                                                                             children=html.H2('ITEMS',style={'margin': '0',
                                                                                                                                           'text-align': 'center',
                                                                                                                                           'justify': 'center'})),
                                                                                                   dbc.Col(
                                                                                                       # width=10,
                                                                                                             style={'min-width':'fit-content','vertical-align': '-webkit-baseline-middle','width':'10%',},
                                                                                                             children=html.H2('GOLD',style={'margin': '0',
                                                                                                                                           'text-align': 'center',
                                                                                                                                           'justify': 'center'})),
                                                                                                   dbc.Col(
                                                                                                       # width=10,
                                                                                                             style={'min-width':'fit-content','vertical-align': '-webkit-baseline-middle','width':'10%',},
                                                                                                             children=html.H2('LH/DN',
                                                                                                                 style={
                                                                                                                     'margin': '0',
                                                                                                                     'text-align': 'center',
                                                                                                                     'justify': 'center'})),
                                                                                                   dbc.Col(
                                                                                                       # width=10,
                                                                                                             style={'min-width':'fit-content','vertical-align': '-webkit-baseline-middle','width':'10%',},
                                                                                                             children=html.H2('GPM/XPM',style={'margin': '0',
                                                                                                                                            'text-align': 'center',
                                                                                                                                            'justify': 'center'})),
                                                                                                   dbc.Col(
                                                                                                       # width=10,
                                                                                                             style={'min-width':'fit-content','vertical-align': '-webkit-baseline-middle','width':'10%',},
                                                                                                             children=html.H2('NW',style={'margin': '0',
                                                                                                                                           'text-align': 'center',
                                                                                                                                           'justify': 'center'}))])]))

        for ind in TeamBD.index:
            hero_items = []
            data = TeamBD['Hero_items'][ind].replace('"', '').replace("'", "")
            res = data.strip('][').split(', ')
            # print("#########     hero_items    ##############", "\n", hero_items)
            for i in res:
                # print("#########     i  SCORE TEBLE    ##############", "\n", i)
                hitem = dbc.Col(
                    # width=16,
                    style={  'padding': '0',
                            'margin': '0',
                        'max-width': '16%',
                        'max-height': '16px',
                        'height': '16px',
                        'width': 'fit-content'},
                    children=[ddk.Logo(
                        src=i,
                        style={
                            'text-align': 'center',
                            'max-height': '16px',
                            'padding': '0',
                            'margin': '0',
                            'vertical-align': '-webkit-baseline-middle'})])
                hero_items.append(hitem)

        ##############     LIVE SCORE TABLES    ###################################
            score_table_item = dbc.ListGroupItem(
                style={'line-height': '1',
                       'margin': '0',
                       'margin-right': '0',
                       'height': '70px', 'justify-content': 'center',
                       'vertical-align': '-webkit-baseline-middle',
                       'max-height': '30px', 'padding': '0px',
                       'list-style': 'none',
                       'min-width':'700px',
                       'align-items': 'center'},
                children=[
                    dbc.Row(
                        # width=100,
                              style={'justify-content': 'center'},
                              children=[dbc.Col(
                                  # width=15,
                                                 style={'vertical-align': '-webkit-baseline-middle','max-width':'15%','width':'15%', 'word-wrap': 'normal','overflow-x':'hidden'},
                                                 children=html.H6(TeamBD['Players'][ind],style={'margin': '0',

                                                                               'text-align': 'center',
                                                                               'justify': 'center'})),
                                       dbc.Col(
                                           # width=15,
                                                 style={'min-width':'fit-content','vertical-align': '-webkit-baseline-middle','width':'15%'},
                                                 children=dbc.Col(
                                                     # width=80,
                                                     style={
                                             'max-height': '20px',
                                             'height': '20px',
                                             'width': 'fit-content',
                                                     'max-width': '80%',},
                                                     children=[ddk.Logo(
                                             src=TeamBD['Hero_pic'][ind],
                                             style={
                                                 'text-align': 'center',
                                                 'max-height': '20px',
                                                 'padding': '0',
                                                 'margin': '0',
                                                 'vertical-align': '-webkit-baseline-middle'})])),
                                       dbc.Col(
                                           # width=10,
                                                 style={'min-width':'fit-content','vertical-align': '-webkit-baseline-middle','width':'10%'},
                                                 children=html.H6(TeamBD['KDA'][ind],
                                                                  style={'margin': '0',
                                                                       'text-align': 'center',
                                                                       'justify': 'center'})),

                                       dbc.Col(
                                           # width=20,
                                                 style={'min-width':'fit-content','vertical-align': '-webkit-baseline-middle','width':'20%'},
                                                 children=dbc.Row([i for i in hero_items])
                                                 ),
                                       dbc.Col(
                                        # width=10,
                                                 style={'min-width':'fit-content','vertical-align': '-webkit-baseline-middle','width':'10%'},
                                                 children=html.H6(TeamBD['Hero_gold'][ind],
                                                                  style={'margin': '0',
                                                                       'text-align': 'center',
                                                                       'justify': 'center'})),
                                       dbc.Col(
                                           # width=10,
                                                 style={'min-width':'fit-content','vertical-align': '-webkit-baseline-middle','width':'10%'},
                                                 children=html.H6(TeamBD['LH_DN'][ind],
                                                     style={
                                                         'margin': '0',
                                                         'text-align': 'center',
                                                         'justify': 'center'})),
                                       dbc.Col(
                                           # width=10,
                                                 style={'min-width':'fit-content','vertical-align': '-webkit-baseline-middle','width':'10%'},
                                                 children=html.H6(TeamBD['GPM_XPM'][ind],
                                                                  style={'margin': '0',
                                                                        'text-align': 'center',
                                                                        'justify': 'center'})),
                                       dbc.Col(
                                           # width=10,
                                                 style={'min-width':'fit-content','vertical-align': '-webkit-baseline-middle','width':'10%'},
                                                 children=html.H6(TeamBD['NW'][ind],style={'margin': '0',
                                                                               'text-align': 'center',
                                                                               'justify': 'center'}))])])

            score_table_item2.append(score_table_item)


        score_table = ddk.Card(style={'width':'-webkit-fill-available',
                                      'margin':'10px',
                                      # 'min-width':'fit-content',
                                      'overflowX':'scroll',
                                      'padding':'0',
                                      'background-color': '#f9f9f91c',},
                               children=[dbc.ListGroup(flush=True,
                                                       children= [i for i in score_table_item2])])

        return score_table


    full_table = ddk.Block(children=[
    ddk.Block(width=100,
              children=html.H2(Team1, style={'margin': '0px','min-width':'fit-content',
                                             # 'max-width':'100%',
                                      'overflow-x':'scroll'})),
    team(Team1BD),
    ddk.Block(width=100,
              children=html.H2(Team2, style={'margin': '0px','min-width':'fit-content',
                                             # 'max-width':'100%',
                                      'overflow-x':'scroll'})),
    team(Team2BD)
    ])

    return full_table
# new_table('371312','MMMTeam1','MMMTeam2')