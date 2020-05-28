import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
import os
import pandas as pd

main_path_data = os.path.abspath("./data")


def tour_page():
    def cards_items():
        serverBD = pd.read_csv(main_path_data + '\\tours.csv')
        cards = []

        for ind in serverBD.index:
            cards_items = dbc.ListGroupItem(
                id={'type': 'dynamic_tour_item',
                    'index': ind},
                # href='/tournament/{}'.format(str(ind)),
                style={'line-height': '1', 'margin': '0', 'margin-right': '0',
                       'height': 'fit-content', 'justify-content': 'center',
                       'vertical-align': '-webkit-baseline-middle',
                       'max-height': 'fit-content', 'padding': '0px',
                       "width": '100%',
                       'align-items': 'center'},
                color="default",
                action=True,
                children=[
                    dbc.Row(style={'max-height': 'fit-content',
                                     'height': '100%',
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
                                  dbc.Col(
                                      # width=30,
                                      style={
                                          "width": '30%',
                                          # 'max-width': '200px',
                                             'max-height': 'fit-content',
                                             'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                             'align-items': 'center', 'justify-content': 'center',
                                             'margin': '0', 'textAlign': 'center',
                                             # 'margin-left': '10px', 'margin-right': '10px'
                                             },
                                      children=html.H6(serverBD['TourName'][ind],
                                                                          style={'height': '100%', 'color': 'azure',
                                                                                 'max-height': 'fit-content',
                                                                                 # 'max-width': '200px',
                                                                                 'overflow-x': 'hidden',
                                                                                 'margin': '0',
                                                                                 'font-size': '15px',
                                                                                 'text-align': 'center',
                                                                                 'vertical-align': '-webkit-baseline-middle'})),
                                  dbc.Col(
                                      # width=20,
                                            style={
                                                "width": '20%',
                                                # 'max-width': 'fit-content',
                                                'max-height': 'fit-content',
                                                'min-width': 'fit-content',
                                                'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                'align-items': 'center', 'justify-content': 'center',
                                                'margin': '0', 'textAlign': 'left',
                                                # 'margin-left': '10px', 'margin-right': '10px'
                                            },
                                            children=[html.H2("{}".format(serverBD['TourPrize'][ind]),
                                                                    style={"width": '100%', 'text-align': 'center',
                                                                        'color': 'azure', 'padding': '0',
                                                                        'margin': '0',
                                                                        'max-height': 'fit-content',
                                                                        'vertical-align': '-webkit-baseline-middle'})]),
                                  dbc.Col(
                                      # width=13,
                                            style={
                                                "width": '20%',
                                                'max-height': '60px',
                                                # 'height': '60px',
                                                'min-width': 'fit-content',
                                                'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                'align-items': 'center', 'justify-content': 'center',
                                                'margin': '0', 'textAlign': 'center'},
                                            children=[
                                                dbc.Row(children=html.P("{}".format(serverBD['TourDateFrom'][ind]),
                                                                    style={'color': 'azure','text-align': 'center',
                                                                           'width': '100%',
                                                                           'font-size': '12px',
                                                                           'padding': '0px', 'margin': '0',
                                                                           'max-height': '-webkit-fill-available',
                                                                           'vertical-align': '-webkit-baseline-middle'})),
                                                dbc.Row(children=html.P(
                                                                    "{}".format(serverBD['TourDateTo'][ind]),
                                                                    style={'color': 'azure','text-align': 'center',
                                                                           'width': '100%',
                                                                           'font-size': '12px',
                                                                           'padding': '0px', 'margin': '0',
                                                                           'max-height': '-webkit-fill-available',
                                                                           'vertical-align': '-webkit-baseline-middle'})),
                                                      ]),
                                  dbc.Col(
                                      # width=8,
                                            style={
                                                "width": '15%',
                                                'min-width': 'fit-content',
                                                'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                'align-items': 'center', 'justify-content': 'center',
                                                'margin': '0', 'textAlign': 'center'},
                                            children=[html.H2("{}".format(serverBD['TourTeams'][ind]),
                                                                    style={'color': 'azure',
                                                                           'width': '100%',
                                                                           'padding': '0px', 'margin': '0',
                                                                           'max-height': '-webkit-fill-available',
                                                                           'vertical-align': '-webkit-baseline-middle'})
                                                      ]),
                                  dbc.Col(
                                      # width=13,
                                            style={
                                                "width": '15%',
                                                'max-height': '60px',
                                                'height': '60px',
                                                'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                'align-items': 'center', 'justify-content': 'center',
                                                'min-width': 'fit-content',
                                                'margin-left': '5px',
                                                'margin': '0', 'textAlign': 'center'},
                                            children=ddk.Logo(src=serverBD['TourFlagLink'][ind],
                                                                   style={'text-align': 'center',
                                                                          "width": '100%',
                                                                          'max-height': '50px',
                                                                          'padding': '0px', 'margin': '0',
                                                                          'vertical-align': '-webkit-baseline-middle'})),

                              ])
                ])
            cards.append(cards_items)
        return cards

    Card_matches = dbc.ListGroup(flush=True,
                                 style={'min-height': '100%',
                                        'max-height': '-webkit-fill-available',
                                        '-webkit-tap-highlight-color': '#268bd2',
                                        'overflow-y': 'scroll'
                                        },
                                 children=[i for i in cards_items()])

    return Card_matches