import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
import os
import pandas as pd
main_path_data = os.path.abspath("./data")


def result_page():
    def cards_items():
        serverBD = pd.read_csv(main_path_data + '\\all_cards.csv')
        serverBD = serverBD.drop_duplicates(subset='Mid', keep="last")
        serverBD = serverBD[serverBD["Mstatus"] == 'Finished']
        serverBD = serverBD.sort_values(by='TIME', ascending=False)
        serverBD = serverBD.head(n=10)

        cards = []
        for ind in serverBD.index:
            cards_items=dbc.ListGroupItem(
                id={'type': 'dynamic-cards-item',
                    'index': str(serverBD['Mid'][ind])},
                href='/{}'.format(str(serverBD['Mid'][ind])),
                style={'line-height': '0', 'margin': '0',
                                     'height': 'fit-content', 'justify-content': 'center',
                                     'vertical-align': '-webkit-baseline-middle',
                                     'max-height': 'fit-content', 'padding': '0px',
                                     'align-items': 'center'},
                color="default",
                action=True,
                children=[
                    dbc.Row(style={'max-height': '50px',
                                     'overflow-y':'hidden',
                                     'line-height': '1',
                                 'height': '50px',
                                 'padding': '0px',
                                 "width": '100%',
                                   'align-items': 'center',
                                 # 'justify-content': 'flex-start',
                                   'justify-content': 'center',
                                   'margin': '0',
                                 'vertical-align': '-webkit-baseline-middle',
                                 'textAlign': 'center',
                                 #     'margin-left': '0',
                                 # 'margin-right': '0'
                                     },
                            children=[
                                dbc.Col(width=32,
                                          style={'width': '32%',
                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                         'align-items': 'center', 'justify-content': 'center',
                                         'margin': '0', 'textAlign': 'center',
                                              # 'width':'fit-content',
                                         'margin-left': '0', 'margin-right': '0'},
                                          children=dbc.Row([
                                              dbc.Col(width=35,
                                                        style={
                                                            'width': '35%',
                                                        'max-height': '40px',
                                                        'height': '40px',
                                                            'background-image': 'url(/assets/png/fon2.png)',
                                                            'background-repeat': 'no-repeat',
                                                            'background-position': 'center',
                                                            'background-size': 'auto 90%',
                                                            # 'background-size': 'cover',
                                                        # 'width': 'fit-content',
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                        children=ddk.Logo(
                                                            src=serverBD['T1logo'][ind],
                                                            style={'text-align': 'center',
                                                                   'max-height': '-webkit-fill-available',
                                                                   'padding': '0px', 'margin': '0',
                                                                 'vertical-align': '-webkit-baseline-middle'})),
                                              dbc.Col(width=65,
                                                        style={'width': '65%',
                                                            # 'overflowX': 'hidden',
                                                 'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                 'align-items': 'center', 'justify-content': 'center',
                                                 'margin': '0', 'textAlign': 'center'},
                                                      children=html.H6(serverBD['T1name'][ind],
                                                                      style={'color':'azure',
                                                                             # 'width': 'fit-content',
                                                                             'padding': '0px', 'margin': '0',
                                                                'max-height': '-webkit-fill-available',
                                                                'vertical-align': '-webkit-baseline-middle'}))])),
                                dbc.Col(width=16,
                                          style={'min-width': 'fit-content',
                                                 'width': '16%',
                                             'max-height': 'fit-content',
                                             'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                             'align-items': 'center', 'justify-content': 'center',
                                             'margin': '0', 'textAlign': 'center',
                                             'margin-left': '10px', 'margin-right': '10px'},
                                          children=[html.H1("{} : {}".format(serverBD['T1score'][ind],
                                                                              serverBD['T2score'][ind]),
                                                                      style={'height': '100%','margin': '0',
                                                                             'color': 'azure', 'padding':'0',
                                                                             'max-height': 'fit-content',
                                                                             'vertical-align': '-webkit-baseline-middle'})]),
                                dbc.Col(width=32,
                                          style={
                                              'width': '32%',
                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                         'align-items': 'center', 'justify-content': 'center',
                                         'margin': '0', 'textAlign': 'center',
                                              # 'width':'fit-content',
                                         'margin-left': '0', 'margin-right': '0'},
                                          children=dbc.Row([
                                            dbc.Col(width=65,
                                                      style={'width': '65%',
                                                            # 'overflowX': 'hidden',
                                                 'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                 'align-items': 'center', 'justify-content': 'center',
                                                 'margin': '0', 'textAlign': 'center'},
                                                      children=html.H6(serverBD['T2name'][ind],
                                                                                   style={'color':'azure',
                                                                             # 'width': 'fit-content',
                                                                             'padding': '0px', 'margin': '0',
                                                                'max-height': '-webkit-fill-available',
                                                                'vertical-align': '-webkit-baseline-middle'})),
                                            dbc.Col(width=35,
                                                      style={
                                                        'max-height': '40px',
                                                        'height': '40px',
                                                        'width': '35%',
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                      children=ddk.Logo(src=serverBD['T2logo'][ind],
                                                                        style={'text-align': 'center',
                                                                               'background-image': 'url(/assets/png/fon2.png)',
                                                            'background-repeat': 'no-repeat',
                                                            'background-position': 'center',
                                                            'background-size': 'auto 90%',
                                                                   'max-height': '-webkit-fill-available',
                                                                   'padding': '0px', 'margin': '0',
                                                                 'vertical-align': '-webkit-baseline-middle'}))])),
                                # ddk.Block(
                                #     # width=50,
                                #           style={'max-width': '200px',
                                #              'max-height': 'fit-content',
                                #              'padding': '0px', 'vertical-align': '-webkit-baseline--webkit-baseline-middle',
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
                                #                              'vertical-align': '-webkit-baseline--webkit-baseline-middle'})),


                                          ])])
            cards.append(cards_items)
        return cards



    Card_matches = dbc.ListGroup(flush=True,
                                 style={'min-height': '100%',
                                     'max-height':'-webkit-fill-available',
                                        '-webkit-tap-highlight-color':  '#268bd2',
                                        'overflow-y':'scroll'
                                        },
                                 children=[i for i in cards_items()])


    return Card_matches