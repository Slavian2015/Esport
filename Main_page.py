import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
import os
import pandas as pd
main_path_data = os.path.abspath("./data")

##################################   SHOW ALL ROWS & COLS   ####################################
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None)


def main_page():
    def cards_items():
        serverBD1 = pd.read_csv(main_path_data + '\\live.csv')
        serverBD = pd.read_csv(main_path_data + '\\server.csv')
        cards = []

        # print('serverBD1', serverBD1)
        for ind in serverBD1.index:

            if serverBD1['T1gold'][ind] == "r" or serverBD1['T1gold'][ind] == 'd':
                T1gold = dbc.Row(style={'margin':'0','justify-content': 'center',
                                        # 'width': 'fit-content',
                                        'padding':'0'},
                                 children=[
                    dbc.Col(width=80,
                       style={'margin': '0', 'padding': '0', 'width': '80%',},
                       children=html.H6("",
                                    style={'color': '#ff0000',
                                            'font-weight': '900',
                                            # 'width': 'fit-content',
                                            'padding': '0px', 'margin': '0',
                                            'max-height': '-webkit-fill-available',
                                            'vertical-align': '-webkit-baseline-middle'})),
                    dbc.Col(width=20,
                                     style={'margin': '0', 'padding': '0','width': '20%',
                                            'max-height': '20px',
                                            'height': '20px'},
                                     children=[])])
            else:
                T1gold = dbc.Row(style={'margin':'0','justify-content': 'center',
                                        # 'width': 'fit-content',
                                        'padding':'0'},
                                 children=[
                    dbc.Col(width=80,
                       style={'margin': '0', 'padding': '0','width': '80%',},
                       children=html.H6(serverBD1['T1gold'][ind], style={'color': '#ff0000',
                                            'font-weight': '900',
                                            # 'width': 'fit-content',
                                            'padding': '0px', 'margin': '0',
                                            'max-height': '-webkit-fill-available',
                                            'vertical-align': '-webkit-baseline-middle'})),
                    dbc.Col(width=20,
                                     style={'margin': '0', 'padding': '0','width': '20%',
                                            'max-height': '20px',
                                            'height': '20px'},
                                     children=ddk.Logo(
                                         src='../assets/png/gold.png',
                                         style={'text-align': 'center',
                                               'max-height': '-webkit-fill-available',
                                               'padding': '0px', 'margin': '0',
                                             'vertical-align': '-webkit-baseline-middle'}))])

            if serverBD1['T2gold'][ind] == "r" or serverBD1['T2gold'][ind] == 'd':
                T2gold = dbc.Row(style={'margin':'0','justify-content': 'center',
                                        # 'width': 'fit-content',
                                        'padding':'0'},
                                 children=[
                                     dbc.Col(width=20,
                                     style={'margin': '0', 'padding': '0',
                                            'max-height': '20px','width': '20%',
                                            'height': '20px'},
                                     children=[]),
                                     dbc.Col(width=80,
                                              style={'margin': '0', 'padding': '0', 'width': '80%',},
                                              children=html.H6("",
                                               style={'color': '#ff0000',
                                                      'font-weight': '900',
                                                      # 'width': 'fit-content',
                                                      'padding': '0px', 'margin': '0',
                                                      'max-height': '-webkit-fill-available',
                                                      'vertical-align': '-webkit-baseline-middle'})),
                       ])
            else:
                T2gold = dbc.Row(style={'margin':'0','justify-content': 'center',
                                        'width': '100%',
                                        'padding':'0'},
                                 children=[
                    dbc.Col(width=20,
                                     style={'margin': '0', 'padding': '0',
                                            'max-height': '20px','width': '20%',
                                            'height': '20px'},
                                     children=ddk.Logo(
                                         src='../assets/png/gold.png',
                                         style={'text-align': 'center',
                                                'max-height': '-webkit-fill-available',
                                                'padding': '0px', 'margin': '0',
                                                'vertical-align': '-webkit-baseline-middle'})),
                    dbc.Col(width=80,
                                    style={'margin': '0', 'padding': '0', 'width': '80%',},
                                    children=html.H6(serverBD1['T2gold'][ind],
                                                     style={'color': '#ff0000',
                                                            'font-weight': '900',
                                                            # 'width': 'fit-content',
                                                            'padding': '0px', 'margin': '0',
                                                            'max-height': '-webkit-fill-available',
                                                            'vertical-align': '-webkit-baseline-middle'})),
                       ])

            T1 = dbc.Col(style={'margin':'0','justify-content': 'center',
                                # 'width': '100%',
                                'padding':'0'},
                                 children=[
                                     dbc.Row(
                                         # width=100,
                                             style={'margin':'0','justify-content': 'center',
                                                    # 'width': '100%',
                                                    'padding':'0'},
                                             children=html.H6(serverBD1['T1names_live'][ind],
                                                              style={'color': 'azure',
                                                            # 'width': 'fit-content',
                                                            'padding': '0px', 'margin': '0',
                                                            'max-height': '-webkit-fill-available',
                                                            'vertical-align': '-webkit-baseline-middle'})),

                                     T1gold
                                     # dbc.Row(
                                     #     # width=100,
                                     #       style={'margin': '0', 'width': '100%','padding': '0'},
                                     #       children=T1gold)
                                           ])

            T2 = dbc.Col(style={'margin':'0','justify-content': 'center',
                                # 'width': 'fit-content',
                                'padding':'0'},
                                 children=[
                                     dbc.Row(
                                         # width=100,
                                             style={'margin': '0',
                                                    'width': '100%','justify-content': 'center',
                                                    'padding': '0'},
                                             children=html.H6(serverBD1['T2names_live'][ind],
                                                              style={'color': 'azure',
                                                  'padding': '0px', 'margin': '0',
                                                  'max-height': '-webkit-fill-available',
                                                  'vertical-align': '-webkit-baseline-middle'})),
                                     T2gold
                                     # dbc.Row(
                                     #     # width=100,
                                     #        style={'margin': '0',
                                     #               'width': '100%',
                                     #               'padding': '0'},
                                     #        children=T2gold),
             ])



            cards_items1=dbc.ListGroupItem(
                id={'type': 'live-cards-item',
                    'index': str(serverBD1['match_id_live'][ind])},
                href='/{}'.format(str(serverBD1['match_id_live'][ind])),
                style={'line-height': '1', 'margin': '0', 'margin-right': '0',
                                     'height': 'fit-content', 'justify-content': 'center',
                                     'vertical-align': '-webkit-baseline-middle',
                                     'max-height': '60px', 'padding': '0px',
                                     'align-items': 'center'},
                color="default",
                className='live_list',
                action=True,
                children=[
                    dbc.Row(style={'max-height': '60px',
                                   "flex-direction": "row",
                                     # 'overflow-y': 'hidden',
                                 'height': '100%',
                                 'padding': '0px',
                                 # "width": 'fit-content',
                                   'align-items': 'center',
                                 # 'justify-content': 'flex-start',
                                   'justify-content': 'center',
                                   # 'margin': '0',
                                 'vertical-align': '-webkit-baseline-middle',
                                 'textAlign': 'center',
                                 #   'margin-left': '0',
                                 # 'margin-right': '0'
                                   },
                            children=[
                                dbc.Col(width=30,
                                          style={'width': '30%',
                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                         'align-items': 'center', 'justify-content': 'center',
                                         'margin': '0', 'textAlign': 'center',
                                         'margin-left': '0', 'margin-right': '0'},
                                          children=dbc.Row(
                                              [
                                              dbc.Col(width=40,
                                                        style={
                                                        'max-height': '40px',
                                                        'height': '40px',
                                                            # 'background-image': 'url(/assets/png/fon2.png)',
                                                            # 'background-repeat': 'no-repeat',
                                                            # 'background-position': 'center',
                                                            # 'background-size': 'auto 90%',
                                                        'width': '40%',
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                        children=ddk.Logo(
                                                            src=serverBD1['T1logos_live'][ind],
                                                            style={'text-align': 'center',
                                                                   'max-height': '-webkit-fill-available',
                                                                   'padding': '0px', 'margin': '0',
                                                                 'vertical-align': '-webkit-baseline-middle'})),
                                              dbc.Col(width=60,
                                                        style={
                                                            'width': '60%',
                                                 'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                 'align-items': 'center', 'justify-content': 'center',
                                                 'margin': '0', 'textAlign': 'center'},
                                                      children=T1)])),
                                dbc.Col(width=20,
                                          style={'min-width': 'fit-content',
                                                 'width': '20%',
                                             'max-height': 'fit-content',
                                             'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                             'align-items': 'center', 'justify-content': 'center',
                                             'margin': '0', 'textAlign': 'center',
                                             'margin-left': '10px', 'margin-right': '10px'},
                                          children=[html.H1("{} : {}".format(serverBD1['T1_live_score1'][ind],
                                                                              serverBD1['T2_live_score1'][ind]),
                                                                      style={'height': '100%',
                                                                             'margin-top': '10px',
                                                                             # 'margin': '0',
                                                                             'margin-bottom': '0px',
                                                                             'color': '#3dea04', 'padding':'0',
                                                                             'max-height': 'fit-content',
                                                                             'width':'100%',
                                                                             'vertical-align': '-webkit-baseline-middle'}),
                                                    html.P("{} - {}".format(serverBD1['T1_live_score2'][ind],
                                                                             serverBD1['T2_live_score2'][ind]),
                                                            style={'height': '100%',
                                                                   'color': 'gold', 'padding': '0',
                                                                   'max-height': 'fit-content',
                                                                   'margin-bottom': '10px',
                                                                   'margin-top': '0px',
                                                                   'width': '100%','font-size': '10px',
                                                                   'vertical-align': '-webkit-baseline-middle'})
                                                    ]),
                                dbc.Col(width=30,
                                          style={
                                              'width': '30%',
                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                         'align-items': 'center', 'justify-content': 'center',
                                         'margin': '0', 'textAlign': 'center',
                                              # 'width':'fit-content',
                                         'margin-left': '0', 'margin-right': '0'},
                                          children=dbc.Row(
                                              [
                                            dbc.Col(width=60,
                                                      style={'width': '60%',
                                                            # 'overflowX': 'hidden',
                                                 'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                 'align-items': 'center', 'justify-content': 'center',
                                                 'margin': '0', 'textAlign': 'center'},
                                                      children=T2),
                                            dbc.Col(width=40,
                                                      style={
                                                        'max-height': '40px',
                                                        'height': '40px',
                                                        'width': '40%',
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                      children=ddk.Logo(src=serverBD1['T2logos_live'][ind],
                                                                        style={'text-align': 'center',
                                                            #                    'background-image': 'url(/assets/png/fon2.png)',
                                                            # 'background-repeat': 'no-repeat',
                                                            # 'background-position': 'center',
                                                            # 'background-size': 'auto 90%',
                                                                   'max-height': '-webkit-fill-available',
                                                                   'padding': '0px', 'margin': '0',
                                                                 'vertical-align': '-webkit-baseline-middle'}))])),

                                # ])
                                          ])])
            cards.append(cards_items1)

        for ind in serverBD.index:
            cards_items=dbc.ListGroupItem(
                id={'type': 'dynamic-cards-item',
                    'index': str(serverBD['match_id'][ind])},
                href='/{}'.format(str(serverBD['match_id'][ind])),
                style={'line-height': '1', 'margin': '0', 'margin-right': '0',
                                     'height': 'fit-content', 'justify-content': 'center',
                                     'vertical-align': '-webkit-baseline-middle',
                                     'max-height': 'fit-content', 'padding': '0px',
                                     'align-items': 'center'},
                color="default",
                action=True,
                children=[
                    dbc.Row(style={'max-height': '50px',
                                     'overflow-y':'hidden',
                                 'height': '100%',
                                 'padding': '0px',
                                 # "width": '100%',
                                   'align-items': 'center',
                                 # 'justify-content': 'flex-start',
                                   'justify-content': 'center',
                                   'margin': '0',
                                 'vertical-align': '-webkit-baseline-middle',
                                 'textAlign': 'center', 'margin-left': '0',
                                 'margin-right': '0'},
                            children=[
                                dbc.Col(width=30,
                                          style={
                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                         'align-items': 'center', 'justify-content': 'center',
                                         'margin': '0', 'textAlign': 'center',
                                              "width": '30%',
                                         'margin-left': '0', 'margin-right': '0'},
                                          children=dbc.Row([
                                              dbc.Col(width=40,
                                                        style={
                                                        'max-height': '40px',
                                                        'height': '40px',
                                                            # 'background-image': 'url(/assets/png/fon2.png)',
                                                            # 'background-repeat': 'no-repeat',
                                                            # 'background-position': 'center',
                                                            # 'background-size': 'auto 90%',
                                                            # 'background-size': 'cover',
                                                        "width": '40%',
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                        children=ddk.Logo(
                                                            src=serverBD['T1logos'][ind],
                                                            style={'text-align': 'center',
                                                                   'max-height': '-webkit-fill-available',
                                                                   'padding': '0px', 'margin': '0',
                                                                 'vertical-align': '-webkit-baseline-middle'})),
                                              dbc.Col(width=60,
                                                        style={"width": '60%',
                                                            # 'overflowX': 'hidden',
                                                 'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                 'align-items': 'center', 'justify-content': 'center',
                                                 'margin': '0', 'textAlign': 'center'},
                                                      children=html.H6(serverBD['T1names'][ind],
                                                                      style={'color':'azure',
                                                                             # 'width': 'fit-content',
                                                                             'padding': '0px', 'margin': '0',
                                                                'max-height': '-webkit-fill-available',
                                                                'vertical-align': '-webkit-baseline-middle'}))])),
                                dbc.Col(width=20,
                                          style={'min-width': 'fit-content',
                                                 "width": '20%',
                                             'max-height': 'fit-content',
                                             'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                             'align-items': 'center', 'justify-content': 'center',
                                             'margin': '0', 'textAlign': 'center',
                                             'margin-left': '10px', 'margin-right': '10px'},
                                          children=[html.H6(serverBD['Mtime'][ind][:-3],
                                                                      style={'height': '100%',
                                                                             'color': 'azure', 'padding':'0',
                                                                             'max-height': 'fit-content',
                                                                             'vertical-align': '-webkit-baseline-middle'})]),
                                dbc.Col(width=30,
                                          style={
                                              "width": '30%',
                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                         'align-items': 'center', 'justify-content': 'center',
                                         'margin': '0', 'textAlign': 'center',
                                              # 'width':'fit-content',
                                         'margin-left': '0', 'margin-right': '0'},
                                          children=dbc.Row([
                                            dbc.Col(width=60,
                                                      style={"width": '60%',
                                                            # 'overflowX': 'hidden',
                                                 'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                 'align-items': 'center', 'justify-content': 'center',
                                                 'margin': '0', 'textAlign': 'center'},
                                                      children=html.H6(serverBD['T2names'][ind],
                                                                                   style={'color':'azure',
                                                                             # 'width': 'fit-content',
                                                                             'padding': '0px', 'margin': '0',
                                                                'max-height': '-webkit-fill-available',
                                                                'vertical-align': '-webkit-baseline-middle'})),
                                            dbc.Col(width=40,
                                                      style={"width": '40%',
                                                        'max-height': '40px',
                                                        'height': '40px',
                                                        # 'width': 'fit-content',
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                      children=ddk.Logo(src=serverBD['T2logos'][ind],
                                                                        style={'text-align': 'center',
                                                            #                    'background-image': 'url(/assets/png/fon2.png)',
                                                            # 'background-repeat': 'no-repeat',
                                                            # 'background-position': 'center',
                                                            # 'background-size': 'auto 90%',
                                                                   'max-height': '-webkit-fill-available',
                                                                   'padding': '0px', 'margin': '0',
                                                                 'vertical-align': '-webkit-baseline-middle'}))])),
                                # dbc.Col(
                                #     # width=50,
                                #           style={'max-width': '200px',
                                #              'max-height': 'fit-content',
                                #              'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                #              'align-items': 'center', 'justify-content': 'center',
                                #              'margin': '0', 'textAlign': 'center',
                                #              # 'margin-left': '10px', 'margin-right': '10px'
                                #                  },
                                #           children=html.H6(serverBD['Mtour'][ind],
                                #                       style={'height': '100%','color':'azure',
                                #                              'max-height': 'fit-content',
                                #                              'max-width': '200px',
                                #                              'overflow-x':'hidden',
                                #                              'margin': '0',
                                #                              'vertical-align': '-webkit-baseline-middle'})),


                                          ])])
            cards.append(cards_items)
        empty_card=dbc.ListGroupItem(
                style={'line-height': '1', 'margin': '0', 'margin-right': '0',
                                     'height': 'fit-content', 'justify-content': 'center',
                                     'vertical-align': '-webkit-baseline-middle',
                                     'max-height': '50px', 'padding': '0px',
                                     'align-items': 'center'},
                color="default",
                action=True,
                children=[
                    ddk.Block(style={'max-height': '50px',
                                     'overflow-y':'hidden',
                                 'height': '50px',
                                 'padding': '0px',
                                 "width": '100%',
                                   'align-items': 'center',
                                 # 'justify-content': 'flex-start',
                                   'justify-content': 'center',
                                   'margin': '0',
                                 'vertical-align': '-webkit-baseline-middle',
                                 'textAlign': 'center', 'margin-left': '0',
                                 'margin-right': '0'},
                            children=[
                                dbc.Col(width=30,
                                          style={
                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                         'align-items': 'center', 'justify-content': 'center',
                                         'margin': '0', 'textAlign': 'center',
                                              'height': '40px',
                                              # 'width':'fit-content',
                                         'margin-left': '0', 'margin-right': '0'},
                                          children=[
                                              dbc.Col(width=40,
                                                        style={
                                                        'max-height': '40px',
                                                        'height': '40px',
                                                            # 'background-image': 'url(/assets/png/fon2.png)',
                                                            # 'background-repeat': 'no-repeat',
                                                            # 'background-position': 'center',
                                                            # 'background-size': 'auto 90%',
                                                            # 'background-size': 'cover',
                                                        # 'width': 'fit-content',
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                        children=ddk.Logo(
                                                            src='',
                                                            style={'text-align': 'center',
                                                                   'max-height': '-webkit-fill-available',
                                                                   'padding': '0px', 'margin': '0',
                                                                 'vertical-align': '-webkit-baseline-middle'})),
                                              dbc.Col(width=60,
                                                        style={'height': '40px',
                                                            # 'overflowX': 'hidden',
                                                 'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                 'align-items': 'center', 'justify-content': 'center',
                                                 'margin': '0', 'textAlign': 'center'},
                                                      children=html.H6('',
                                                                       style={'color':'azure',
                                                                             # 'width': 'fit-content',
                                                                             'padding': '0px', 'margin': '0',
                                                                'max-height': '-webkit-fill-available',
                                                                'vertical-align': '-webkit-baseline-middle'}))]),
                                dbc.Col(width=20,
                                          style={'max-width': 'fit-content',
                                             'max-height': '50px', 'height': '50px',
                                             'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                             'align-items': 'center', 'justify-content': 'center',
                                             'margin': '0', 'textAlign': 'center',
                                             'margin-left': '10px', 'margin-right': '10px'},
                                          children=[html.H6('',
                                                                      style={'height': '100%',
                                                                             'color': 'azure', 'padding':'0',
                                                                             'max-height': 'fit-content',
                                                                             'vertical-align': '-webkit-baseline-middle'})]),
                                dbc.Col(width=30,
                                          style={

                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                         'align-items': 'center', 'justify-content': 'center',
                                         'margin': '0', 'textAlign': 'center',
                                              # 'width':'fit-content',
                                         'margin-left': '0', 'margin-right': '0'},
                                          children=[
                                            dbc.Col(width=60,
                                                      style={
                                                            # 'overflowX': 'hidden',
                                                          'height': '50px',
                                                 'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                 'align-items': 'center', 'justify-content': 'center',
                                                 'margin': '0', 'textAlign': 'center'},
                                                      children=html.H6('',
                                                                                   style={'color':'azure',
                                                                             # 'width': 'fit-content',
                                                                             'padding': '0px', 'margin': '0',
                                                                'max-height': '-webkit-fill-available',
                                                                'vertical-align': '-webkit-baseline-middle'})),
                                            dbc.Col(width=40,
                                                      style={
                                                        'max-height': '50px',
                                                        'height': '50px',
                                                        # 'width': 'fit-content',
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                      children=ddk.Logo(src='',
                                                                        style={'text-align': 'center',
                                                            #                    'background-image': 'url(/assets/png/fon2.png)',
                                                            # 'background-repeat': 'no-repeat',
                                                            # 'background-position': 'center',
                                                            # 'background-size': 'auto 90%',
                                                                   'max-height': '-webkit-fill-available',
                                                                   'padding': '0px', 'margin': '0',
                                                                 'vertical-align': '-webkit-baseline-middle'}))]),
                                dbc.Col(
                                    # width=50,
                                          style={'max-width': '200px',
                                             'max-height': '50px',
                                             'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                             'align-items': 'center', 'justify-content': 'center',
                                             'margin': '0', 'textAlign': 'center',
                                             # 'margin-left': '10px', 'margin-right': '10px'
                                                 },
                                          children=html.H6('',
                                                      style={'height': '50px','color':'azure',
                                                             'max-height': '50px',
                                                             'max-width': '200px',
                                                             'overflow-x':'hidden',
                                                             'margin': '0',
                                                             'vertical-align': '-webkit-baseline-middle'})),


                                          ])])
        cards.append(empty_card)
        return cards

    Card_matches = dbc.ListGroup(flush=True,
                                 style={'min-height': '100%',
                                     'max-height':'-webkit-fill-available',
                                        '-webkit-tap-highlight-color':  '#268bd2',
                                        'overflow-y':'scroll'
                                        },
                                 children=[i for i in cards_items()])


    return Card_matches

