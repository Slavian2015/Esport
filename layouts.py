import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
# import uuid
import os
from app import dash_app
import pandas as pd
import Main_page
import Live_matches
import Main_tours_page
import News_card
import Result_page


main_path_data = os.path.abspath("./data")
# global interval
# interval = dcc.Interval(id='interval',
#                         interval=10000,
#                         n_intervals=0)


##################     ALL MATCHES     ####################################
def serve_layout():
    """Creates the layout for each user of the app.
    This function is executed each time a session is created for the app.
    It creates a new session id (a uuid.uuid1 as string) each time.

    This session id will be used in combination with a DashDatabase instance to manage user values.
    It will be fetched via the property data of a dcc.Store component.
    """

    # create a session id
    # session_id = str(uuid.uuid1())
    # # store the session id in a dcc.Store component (invisible component for storing data)
    # store_session_id_div = dcc.Store(id='session_id_div_id',
    #                                  storage_type='session',  # IMPORTANT! see docstring of dcc.Store
    #                                  data=session_id)

    # # create tab to enter a value
    # first_tab = dcc.Tab(label="Enter a value",
    #                     children=[dcc.Input(placeholder="Enter value here", id="input_div"),
    #                               html.Button(children="OK", id="ok_button"),
    #                               dcc.Markdown(id="success_value_saved")])
    #
    # # create tab to retrieve the value entered in the other tab
    # second_tab = dcc.Tab(label="Retrieve the value",
    #                      children=[html.Button(children="Show me the value", id="show_value_button"),
    #                                dcc.Markdown(id="show_value_div")])
    #
    # # assemble tabs in dcc.Tabs object
    # tabs = dcc.Tabs(children=[first_tab, second_tab])

    # create layout

    Card_matches = dbc.ListGroup(flush=True,
                                 children=[
        dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
                                 'height': '50px', 'justify-content': 'center',
                                 'vertical-align': '-webkit-baseline-middle',
                                 'max-height': 'fit-content', 'padding': '0px',
                                 'align-items': 'center'},
                          color="default",
                          action = True,
                          children=[
                              ddk.Row(style={'max-height': 'fit-content',
                                             'height': '100%',
                                             'padding': '0px',
                                             "width": '100%', 'align-items': 'center',
                                             'justify-content': 'center', 'margin': '0',
                                             'vertical-align': '-webkit-baseline-middle',
                                             'textAlign': 'center', 'margin-left': '0',
                                             'margin-right': '0'},
                                      children=[
                                          ddk.Block(width=30,
                                                    style={
                                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '0', 'margin-right': '0'},
                                                  children=[
                                                      ddk.Block(width=50,
                                                                style={
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                              children=ddk.Logo(src='../assets/logo.png',
                                                                                style={
                                                                                     'max-height': '-webkit-fill-available',
                                                                                       'padding': '0px', 'margin': '0',
                                                                                     'vertical-align': '-webkit-baseline-middle'})),
                                                      ddk.Block(width=50,
                                                                style={
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                              children=html.H6('CyberL',
                                                                              style={
                                                                                     'padding': '0px', 'margin': '0',
                                                                        'max-height': '-webkit-fill-available',
                                                                        'vertical-align': '-webkit-baseline-middle'}))]),

                                          ddk.Block(width=10,
                                                    style={'max-width': 'fit-content',
                                                         'max-height': 'fit-content',
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '10px', 'margin-right': '10px'},
                                                  children=html.H6('20:30',
                                                                  style={'height': '100%',
                                                                         'max-height': 'fit-content',
                                                                         'vertical-align': '-webkit-baseline-middle'})),

                                          ddk.Block(width=30,
                                                    style={
                                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '0', 'margin-right': '0'},
                                                    children=[

                                                        ddk.Block(width=50,
                                                                  style={'max-width': 'fit-content',
                                                         'max-height': 'fit-content',
                                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                              children=html.H6('CyberL',
                                                                              style={
                                                                                     'padding': '0px', 'margin': '0',
                                                                                     'max-height': '-webkit-fill-available',
                                                                                     'vertical-align': '-webkit-baseline-middle'})),

                                                        ddk.Block(width=50,
                                                                  style={
                                                                      'padding': '0px',
                                                                      'vertical-align': '-webkit-baseline-middle',
                                                                      'align-items': 'center',
                                                                      'justify-content': 'center',
                                                                      'margin': '0', 'textAlign': 'center'},
                                                              children=ddk.Logo(src='../assets/logo.png',
                                                                                style={
                                                                                       'max-height': '-webkit-fill-available',
                                                                                       'padding': '0px', 'margin': '0',
                                                                                       'vertical-align': '-webkit-baseline-middle'}))]),

                                          ddk.Block(width=30,
                                                    style={'max-width': 'fit-content',
                                                         'max-height': 'fit-content',
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '10px', 'margin-right': '10px'},
                                                    children=html.H6('ESL SA',
                                                                  style={'height': '100%',
                                                                         'max-height': 'fit-content',
                                                                         'vertical-align': '-webkit-baseline-middle'})),


                                      ])]),
        dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
                                 'height': '50px', 'justify-content': 'center',
                                 'vertical-align': '-webkit-baseline-middle',
                                 'max-height': 'fit-content', 'padding': '0px',
                                 'align-items': 'center'},
                          color="default",
                          action = True,
                          children=[
                              ddk.Row(style={'max-height': 'fit-content',
                                             'height': '100%',
                                             'padding': '0px',
                                             "width": '100%', 'align-items': 'center',
                                             'justify-content': 'center', 'margin': '0',
                                             'vertical-align': '-webkit-baseline-middle',
                                             'textAlign': 'center', 'margin-left': '0',
                                             'margin-right': '0'},
                                      children=[
                                          ddk.Block(width=30,
                                                    style={
                                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '0', 'margin-right': '0'},
                                                  children=[
                                                      ddk.Block(width=50,
                                                                style={
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                              children=ddk.Logo(src='../assets/logo.png',
                                                                                style={
                                                                                     'max-height': '-webkit-fill-available',
                                                                                       'padding': '0px', 'margin': '0',
                                                                                     'vertical-align': '-webkit-baseline-middle'})),
                                                      ddk.Block(width=50,
                                                                style={
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                              children=html.H6('CyberL',
                                                                              style={
                                                                                     'padding': '0px', 'margin': '0',
                                                                        'max-height': '-webkit-fill-available',
                                                                        'vertical-align': '-webkit-baseline-middle'}))]),

                                          ddk.Block(width=10,
                                                    style={'max-width': 'fit-content',
                                                         'max-height': 'fit-content',
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '10px', 'margin-right': '10px'},
                                                  children=html.H6('20:30',
                                                                  style={'height': '100%',
                                                                         'max-height': 'fit-content',
                                                                         'vertical-align': '-webkit-baseline-middle'})),

                                          ddk.Block(width=30,
                                                    style={
                                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '0', 'margin-right': '0'},
                                                    children=[

                                                        ddk.Block(width=50,
                                                                  style={'max-width': 'fit-content',
                                                         'max-height': 'fit-content',
                                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                              children=html.H6('CyberL',
                                                                              style={
                                                                                     'padding': '0px', 'margin': '0',
                                                                                     'max-height': '-webkit-fill-available',
                                                                                     'vertical-align': '-webkit-baseline-middle'})),

                                                        ddk.Block(width=50,
                                                                  style={
                                                                      'padding': '0px',
                                                                      'vertical-align': '-webkit-baseline-middle',
                                                                      'align-items': 'center',
                                                                      'justify-content': 'center',
                                                                      'margin': '0', 'textAlign': 'center'},
                                                              children=ddk.Logo(src='../assets/logo.png',
                                                                                style={
                                                                                       'max-height': '-webkit-fill-available',
                                                                                       'padding': '0px', 'margin': '0',
                                                                                       'vertical-align': '-webkit-baseline-middle'}))]),

                                          ddk.Block(width=30,
                                                    style={'max-width': 'fit-content',
                                                         'max-height': 'fit-content',
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '10px', 'margin-right': '10px'},
                                                    children=html.H6('ESL SA',
                                                                  style={'height': '100%',
                                                                         'max-height': 'fit-content',
                                                                         'vertical-align': '-webkit-baseline-middle'})),


                                      ])]),
        dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
                                 'height': '50px', 'justify-content': 'center',
                                 'vertical-align': '-webkit-baseline-middle',
                                 'max-height': 'fit-content', 'padding': '0px',
                                 'align-items': 'center'},
                          color="default",
                          action = True,
                          children=[
                              ddk.Row(style={'max-height': 'fit-content',
                                             'height': '100%',
                                             'padding': '0px',
                                             "width": '100%', 'align-items': 'center',
                                             'justify-content': 'center', 'margin': '0',
                                             'vertical-align': '-webkit-baseline-middle',
                                             'textAlign': 'center', 'margin-left': '0',
                                             'margin-right': '0'},
                                      children=[
                                          ddk.Block(width=30,
                                                    style={
                                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '0', 'margin-right': '0'},
                                                  children=[
                                                      ddk.Block(width=50,
                                                                style={
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                              children=ddk.Logo(src='../assets/logo.png',
                                                                                style={
                                                                                     'max-height': '-webkit-fill-available',
                                                                                       'padding': '0px', 'margin': '0',
                                                                                     'vertical-align': '-webkit-baseline-middle'})),
                                                      ddk.Block(width=50,
                                                                style={
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                              children=html.H6('CyberL',
                                                                              style={
                                                                                     'padding': '0px', 'margin': '0',
                                                                        'max-height': '-webkit-fill-available',
                                                                        'vertical-align': '-webkit-baseline-middle'}))]),

                                          ddk.Block(width=10,
                                                    style={'max-width': 'fit-content',
                                                         'max-height': 'fit-content',
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '10px', 'margin-right': '10px'},
                                                  children=html.H6('20:30',
                                                                  style={'height': '100%',
                                                                         'max-height': 'fit-content',
                                                                         'vertical-align': '-webkit-baseline-middle'})),

                                          ddk.Block(width=30,
                                                    style={
                                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '0', 'margin-right': '0'},
                                                    children=[

                                                        ddk.Block(width=50,
                                                                  style={'max-width': 'fit-content',
                                                         'max-height': 'fit-content',
                                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                              children=html.H6('CyberL',
                                                                              style={
                                                                                     'padding': '0px', 'margin': '0',
                                                                                     'max-height': '-webkit-fill-available',
                                                                                     'vertical-align': '-webkit-baseline-middle'})),

                                                        ddk.Block(width=50,
                                                                  style={
                                                                      'padding': '0px',
                                                                      'vertical-align': '-webkit-baseline-middle',
                                                                      'align-items': 'center',
                                                                      'justify-content': 'center',
                                                                      'margin': '0', 'textAlign': 'center'},
                                                              children=ddk.Logo(src='../assets/logo.png',
                                                                                style={
                                                                                       'max-height': '-webkit-fill-available',
                                                                                       'padding': '0px', 'margin': '0',
                                                                                       'vertical-align': '-webkit-baseline-middle'}))]),

                                          ddk.Block(width=30,
                                                    style={'max-width': 'fit-content',
                                                         'max-height': 'fit-content',
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '10px', 'margin-right': '10px'},
                                                    children=html.H6('ESL SA',
                                                                  style={'height': '100%',
                                                                         'max-height': 'fit-content',
                                                                         'vertical-align': '-webkit-baseline-middle'})),


                                      ])]),
        dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
                                 'height': '50px', 'justify-content': 'center',
                                 'vertical-align': '-webkit-baseline-middle',
                                 'max-height': 'fit-content', 'padding': '0px',
                                 'align-items': 'center'},
                          color="default",
                          action = True,
                          children=[
                              ddk.Row(style={'max-height': 'fit-content',
                                             'height': '100%',
                                             'padding': '0px',
                                             "width": '100%', 'align-items': 'center',
                                             'justify-content': 'center', 'margin': '0',
                                             'vertical-align': '-webkit-baseline-middle',
                                             'textAlign': 'center', 'margin-left': '0',
                                             'margin-right': '0'},
                                      children=[
                                          ddk.Block(width=30,
                                                    style={
                                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '0', 'margin-right': '0'},
                                                  children=[
                                                      ddk.Block(width=50,
                                                                style={
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                              children=ddk.Logo(src='../assets/logo.png',
                                                                                style={
                                                                                     'max-height': '-webkit-fill-available',
                                                                                       'padding': '0px', 'margin': '0',
                                                                                     'vertical-align': '-webkit-baseline-middle'})),
                                                      ddk.Block(width=50,
                                                                style={
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                              children=html.H6('CyberL',
                                                                              style={
                                                                                     'padding': '0px', 'margin': '0',
                                                                        'max-height': '-webkit-fill-available',
                                                                        'vertical-align': '-webkit-baseline-middle'}))]),

                                          ddk.Block(width=10,
                                                    style={'max-width': 'fit-content',
                                                         'max-height': 'fit-content',
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '10px', 'margin-right': '10px'},
                                                  children=html.H6('20:30',
                                                                  style={'height': '100%',
                                                                         'max-height': 'fit-content',
                                                                         'vertical-align': '-webkit-baseline-middle'})),

                                          ddk.Block(width=30,
                                                    style={
                                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '0', 'margin-right': '0'},
                                                    children=[

                                                        ddk.Block(width=50,
                                                                  style={'max-width': 'fit-content',
                                                         'max-height': 'fit-content',
                                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                              children=html.H6('CyberL',
                                                                              style={
                                                                                     'padding': '0px', 'margin': '0',
                                                                                     'max-height': '-webkit-fill-available',
                                                                                     'vertical-align': '-webkit-baseline-middle'})),

                                                        ddk.Block(width=50,
                                                                  style={
                                                                      'padding': '0px',
                                                                      'vertical-align': '-webkit-baseline-middle',
                                                                      'align-items': 'center',
                                                                      'justify-content': 'center',
                                                                      'margin': '0', 'textAlign': 'center'},
                                                              children=ddk.Logo(src='../assets/logo.png',
                                                                                style={
                                                                                       'max-height': '-webkit-fill-available',
                                                                                       'padding': '0px', 'margin': '0',
                                                                                       'vertical-align': '-webkit-baseline-middle'}))]),

                                          ddk.Block(width=30,
                                                    style={'max-width': 'fit-content',
                                                         'max-height': 'fit-content',
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '10px', 'margin-right': '10px'},
                                                    children=html.H6('ESL SA',
                                                                  style={'height': '100%',
                                                                         'max-height': 'fit-content',
                                                                         'vertical-align': '-webkit-baseline-middle'})),


                                      ])]),
        dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
                                 'height': '50px', 'justify-content': 'center',
                                 'vertical-align': '-webkit-baseline-middle',
                                 'max-height': 'fit-content', 'padding': '0px',
                                 'align-items': 'center'},
                          color="default",
                          action = True,
                          children=[
                              ddk.Row(style={'max-height': 'fit-content',
                                             'height': '100%',
                                             'padding': '0px',
                                             "width": '100%', 'align-items': 'center',
                                             'justify-content': 'center', 'margin': '0',
                                             'vertical-align': '-webkit-baseline-middle',
                                             'textAlign': 'center', 'margin-left': '0',
                                             'margin-right': '0'},
                                      children=[
                                          ddk.Block(width=30,
                                                    style={
                                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '0', 'margin-right': '0'},
                                                  children=[
                                                      ddk.Block(width=50,
                                                                style={
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                              children=ddk.Logo(src='../assets/logo.png',
                                                                                style={
                                                                                     'max-height': '-webkit-fill-available',
                                                                                       'padding': '0px', 'margin': '0',
                                                                                     'vertical-align': '-webkit-baseline-middle'})),
                                                      ddk.Block(width=50,
                                                                style={
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                              children=html.H6('CyberL',
                                                                              style={
                                                                                     'padding': '0px', 'margin': '0',
                                                                        'max-height': '-webkit-fill-available',
                                                                        'vertical-align': '-webkit-baseline-middle'}))]),

                                          ddk.Block(width=10,
                                                    style={'max-width': 'fit-content',
                                                         'max-height': 'fit-content',
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '10px', 'margin-right': '10px'},
                                                  children=html.H6('20:30',
                                                                  style={'height': '100%',
                                                                         'max-height': 'fit-content',
                                                                         'vertical-align': '-webkit-baseline-middle'})),

                                          ddk.Block(width=30,
                                                    style={
                                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '0', 'margin-right': '0'},
                                                    children=[

                                                        ddk.Block(width=50,
                                                                  style={'max-width': 'fit-content',
                                                         'max-height': 'fit-content',
                                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                              children=html.H6('CyberL',
                                                                              style={
                                                                                     'padding': '0px', 'margin': '0',
                                                                                     'max-height': '-webkit-fill-available',
                                                                                     'vertical-align': '-webkit-baseline-middle'})),

                                                        ddk.Block(width=50,
                                                                  style={
                                                                      'padding': '0px',
                                                                      'vertical-align': '-webkit-baseline-middle',
                                                                      'align-items': 'center',
                                                                      'justify-content': 'center',
                                                                      'margin': '0', 'textAlign': 'center'},
                                                              children=ddk.Logo(src='../assets/logo.png',
                                                                                style={
                                                                                       'max-height': '-webkit-fill-available',
                                                                                       'padding': '0px', 'margin': '0',
                                                                                       'vertical-align': '-webkit-baseline-middle'}))]),

                                          ddk.Block(width=30,
                                                    style={'max-width': 'fit-content',
                                                         'max-height': 'fit-content',
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '10px', 'margin-right': '10px'},
                                                    children=html.H6('ESL SA',
                                                                  style={'height': '100%',
                                                                         'max-height': 'fit-content',
                                                                         'vertical-align': '-webkit-baseline-middle'})),


                                      ])]),
        dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
                                 'height': '50px', 'justify-content': 'center',
                                 'vertical-align': '-webkit-baseline-middle',
                                 'max-height': 'fit-content', 'padding': '0px',
                                 'align-items': 'center'},
                          color="default",
                          action = True,
                          children=[
                              ddk.Row(style={'max-height': 'fit-content',
                                             'height': '100%',
                                             'padding': '0px',
                                             "width": '100%', 'align-items': 'center',
                                             'justify-content': 'center', 'margin': '0',
                                             'vertical-align': '-webkit-baseline-middle',
                                             'textAlign': 'center', 'margin-left': '0',
                                             'margin-right': '0'},
                                      children=[
                                          ddk.Block(width=30,
                                                    style={
                                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '0', 'margin-right': '0'},
                                                  children=[
                                                      ddk.Block(width=50,
                                                                style={
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                              children=ddk.Logo(src='../assets/logo.png',
                                                                                style={
                                                                                     'max-height': '-webkit-fill-available',
                                                                                       'padding': '0px', 'margin': '0',
                                                                                     'vertical-align': '-webkit-baseline-middle'})),
                                                      ddk.Block(width=50,
                                                                style={
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                              children=html.H6('CyberL',
                                                                              style={
                                                                                     'padding': '0px', 'margin': '0',
                                                                        'max-height': '-webkit-fill-available',
                                                                        'vertical-align': '-webkit-baseline-middle'}))]),

                                          ddk.Block(width=10,
                                                    style={'max-width': 'fit-content',
                                                         'max-height': 'fit-content',
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '10px', 'margin-right': '10px'},
                                                  children=html.H6('20:30',
                                                                  style={'height': '100%',
                                                                         'max-height': 'fit-content',
                                                                         'vertical-align': '-webkit-baseline-middle'})),

                                          ddk.Block(width=30,
                                                    style={
                                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '0', 'margin-right': '0'},
                                                    children=[

                                                        ddk.Block(width=50,
                                                                  style={'max-width': 'fit-content',
                                                         'max-height': 'fit-content',
                                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                              children=html.H6('CyberL',
                                                                              style={
                                                                                     'padding': '0px', 'margin': '0',
                                                                                     'max-height': '-webkit-fill-available',
                                                                                     'vertical-align': '-webkit-baseline-middle'})),

                                                        ddk.Block(width=50,
                                                                  style={
                                                                      'padding': '0px',
                                                                      'vertical-align': '-webkit-baseline-middle',
                                                                      'align-items': 'center',
                                                                      'justify-content': 'center',
                                                                      'margin': '0', 'textAlign': 'center'},
                                                              children=ddk.Logo(src='../assets/logo.png',
                                                                                style={
                                                                                       'max-height': '-webkit-fill-available',
                                                                                       'padding': '0px', 'margin': '0',
                                                                                       'vertical-align': '-webkit-baseline-middle'}))]),

                                          ddk.Block(width=30,
                                                    style={'max-width': 'fit-content',
                                                         'max-height': 'fit-content',
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '10px', 'margin-right': '10px'},
                                                    children=html.H6('ESL SA',
                                                                  style={'height': '100%',
                                                                         'max-height': 'fit-content',
                                                                         'vertical-align': '-webkit-baseline-middle'})),


                                      ])]),
        dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
                                 'height': '50px', 'justify-content': 'center',
                                 'vertical-align': '-webkit-baseline-middle',
                                 'max-height': 'fit-content', 'padding': '0px',
                                 'align-items': 'center'},
                          color="default",
                          action = True,
                          children=[
                              ddk.Row(style={'max-height': 'fit-content',
                                             'height': '100%',
                                             'padding': '0px',
                                             "width": '100%', 'align-items': 'center',
                                             'justify-content': 'center', 'margin': '0',
                                             'vertical-align': '-webkit-baseline-middle',
                                             'textAlign': 'center', 'margin-left': '0',
                                             'margin-right': '0'},
                                      children=[
                                          ddk.Block(width=30,
                                                    style={
                                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '0', 'margin-right': '0'},
                                                  children=[
                                                      ddk.Block(width=50,
                                                                style={
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                              children=ddk.Logo(src='../assets/logo.png',
                                                                                style={
                                                                                     'max-height': '-webkit-fill-available',
                                                                                       'padding': '0px', 'margin': '0',
                                                                                     'vertical-align': '-webkit-baseline-middle'})),
                                                      ddk.Block(width=50,
                                                                style={
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                              children=html.H6('CyberL',
                                                                              style={
                                                                                     'padding': '0px', 'margin': '0',
                                                                        'max-height': '-webkit-fill-available',
                                                                        'vertical-align': '-webkit-baseline-middle'}))]),

                                          ddk.Block(width=10,
                                                    style={'max-width': 'fit-content',
                                                         'max-height': 'fit-content',
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '10px', 'margin-right': '10px'},
                                                  children=html.H6('20:30',
                                                                  style={'height': '100%',
                                                                         'max-height': 'fit-content',
                                                                         'vertical-align': '-webkit-baseline-middle'})),

                                          ddk.Block(width=30,
                                                    style={
                                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '0', 'margin-right': '0'},
                                                    children=[

                                                        ddk.Block(width=50,
                                                                  style={'max-width': 'fit-content',
                                                         'max-height': 'fit-content',
                                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                              children=html.H6('CyberL',
                                                                              style={
                                                                                     'padding': '0px', 'margin': '0',
                                                                                     'max-height': '-webkit-fill-available',
                                                                                     'vertical-align': '-webkit-baseline-middle'})),

                                                        ddk.Block(width=50,
                                                                  style={
                                                                      'padding': '0px',
                                                                      'vertical-align': '-webkit-baseline-middle',
                                                                      'align-items': 'center',
                                                                      'justify-content': 'center',
                                                                      'margin': '0', 'textAlign': 'center'},
                                                              children=ddk.Logo(src='../assets/logo.png',
                                                                                style={
                                                                                       'max-height': '-webkit-fill-available',
                                                                                       'padding': '0px', 'margin': '0',
                                                                                       'vertical-align': '-webkit-baseline-middle'}))]),

                                          ddk.Block(width=30,
                                                    style={'max-width': 'fit-content',
                                                         'max-height': 'fit-content',
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '10px', 'margin-right': '10px'},
                                                    children=html.H6('ESL SA',
                                                                  style={'height': '100%',
                                                                         'max-height': 'fit-content',
                                                                         'vertical-align': '-webkit-baseline-middle'})),


                                      ])]),
        dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
                                 'height': '50px', 'justify-content': 'center',
                                 'vertical-align': '-webkit-baseline-middle',
                                 'max-height': 'fit-content', 'padding': '0px',
                                 'align-items': 'center'},
                          color="default",
                          action = True,
                          children=[
                              ddk.Row(style={'max-height': 'fit-content',
                                             'height': '100%',
                                             'padding': '0px',
                                             "width": '100%', 'align-items': 'center',
                                             'justify-content': 'center', 'margin': '0',
                                             'vertical-align': '-webkit-baseline-middle',
                                             'textAlign': 'center', 'margin-left': '0',
                                             'margin-right': '0'},
                                      children=[
                                          ddk.Block(width=30,
                                                    style={
                                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '0', 'margin-right': '0'},
                                                  children=[
                                                      ddk.Block(width=50,
                                                                style={
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                              children=ddk.Logo(src='../assets/logo.png',
                                                                                style={
                                                                                     'max-height': '-webkit-fill-available',
                                                                                       'padding': '0px', 'margin': '0',
                                                                                     'vertical-align': '-webkit-baseline-middle'})),
                                                      ddk.Block(width=50,
                                                                style={
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                              children=html.H6('CyberL',
                                                                              style={
                                                                                     'padding': '0px', 'margin': '0',
                                                                        'max-height': '-webkit-fill-available',
                                                                        'vertical-align': '-webkit-baseline-middle'}))]),

                                          ddk.Block(width=10,
                                                    style={'max-width': 'fit-content',
                                                         'max-height': 'fit-content',
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '10px', 'margin-right': '10px'},
                                                  children=html.H6('20:30',
                                                                  style={'height': '100%',
                                                                         'max-height': 'fit-content',
                                                                         'vertical-align': '-webkit-baseline-middle'})),

                                          ddk.Block(width=30,
                                                    style={
                                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '0', 'margin-right': '0'},
                                                    children=[

                                                        ddk.Block(width=50,
                                                                  style={'max-width': 'fit-content',
                                                         'max-height': 'fit-content',
                                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                              children=html.H6('CyberL',
                                                                              style={
                                                                                     'padding': '0px', 'margin': '0',
                                                                                     'max-height': '-webkit-fill-available',
                                                                                     'vertical-align': '-webkit-baseline-middle'})),

                                                        ddk.Block(width=50,
                                                                  style={
                                                                      'padding': '0px',
                                                                      'vertical-align': '-webkit-baseline-middle',
                                                                      'align-items': 'center',
                                                                      'justify-content': 'center',
                                                                      'margin': '0', 'textAlign': 'center'},
                                                              children=ddk.Logo(src='../assets/logo.png',
                                                                                style={
                                                                                       'max-height': '-webkit-fill-available',
                                                                                       'padding': '0px', 'margin': '0',
                                                                                       'vertical-align': '-webkit-baseline-middle'}))]),

                                          ddk.Block(width=30,
                                                    style={'max-width': 'fit-content',
                                                         'max-height': 'fit-content',
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '10px', 'margin-right': '10px'},
                                                    children=html.H6('ESL SA',
                                                                  style={'height': '100%',
                                                                         'max-height': 'fit-content',
                                                                         'vertical-align': '-webkit-baseline-middle'})),


                                      ])]),
        dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
                                 'height': '50px', 'justify-content': 'center',
                                 'vertical-align': '-webkit-baseline-middle',
                                 'max-height': 'fit-content', 'padding': '0px',
                                 'align-items': 'center'},
                          color="default",
                          action = True,
                          children=[
                              ddk.Row(style={'max-height': 'fit-content',
                                             'height': '100%',
                                             'padding': '0px',
                                             "width": '100%', 'align-items': 'center',
                                             'justify-content': 'center', 'margin': '0',
                                             'vertical-align': '-webkit-baseline-middle',
                                             'textAlign': 'center', 'margin-left': '0',
                                             'margin-right': '0'},
                                      children=[
                                          ddk.Block(width=30,
                                                    style={
                                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '0', 'margin-right': '0'},
                                                  children=[
                                                      ddk.Block(width=50,
                                                                style={
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                              children=ddk.Logo(src='../assets/logo.png',
                                                                                style={
                                                                                     'max-height': '-webkit-fill-available',
                                                                                       'padding': '0px', 'margin': '0',
                                                                                     'vertical-align': '-webkit-baseline-middle'})),
                                                      ddk.Block(width=50,
                                                                style={
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                              children=html.H6('CyberL',
                                                                              style={
                                                                                     'padding': '0px', 'margin': '0',
                                                                        'max-height': '-webkit-fill-available',
                                                                        'vertical-align': '-webkit-baseline-middle'}))]),

                                          ddk.Block(width=10,
                                                    style={'max-width': 'fit-content',
                                                         'max-height': 'fit-content',
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '10px', 'margin-right': '10px'},
                                                  children=html.H6('20:30',
                                                                  style={'height': '100%',
                                                                         'max-height': 'fit-content',
                                                                         'vertical-align': '-webkit-baseline-middle'})),

                                          ddk.Block(width=30,
                                                    style={
                                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '0', 'margin-right': '0'},
                                                    children=[

                                                        ddk.Block(width=50,
                                                                  style={'max-width': 'fit-content',
                                                         'max-height': 'fit-content',
                                                         'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center'},
                                                              children=html.H6('CyberL',
                                                                              style={
                                                                                     'padding': '0px', 'margin': '0',
                                                                                     'max-height': '-webkit-fill-available',
                                                                                     'vertical-align': '-webkit-baseline-middle'})),

                                                        ddk.Block(width=50,
                                                                  style={
                                                                      'padding': '0px',
                                                                      'vertical-align': '-webkit-baseline-middle',
                                                                      'align-items': 'center',
                                                                      'justify-content': 'center',
                                                                      'margin': '0', 'textAlign': 'center'},
                                                              children=ddk.Logo(src='../assets/logo.png',
                                                                                style={
                                                                                       'max-height': '-webkit-fill-available',
                                                                                       'padding': '0px', 'margin': '0',
                                                                                       'vertical-align': '-webkit-baseline-middle'}))]),

                                          ddk.Block(width=30,
                                                    style={'max-width': 'fit-content',
                                                         'max-height': 'fit-content',
                                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                         'align-items': 'center', 'justify-content': 'center',
                                                         'margin': '0', 'textAlign': 'center',
                                                         'margin-left': '10px', 'margin-right': '10px'},
                                                    children=html.H6('ESL SA',
                                                                  style={'height': '100%',
                                                                         'max-height': 'fit-content',
                                                                         'vertical-align': '-webkit-baseline-middle'})),


                                      ])]),


                                 ])


    layout = ddk.Block(width=100,
                  style={'height': '90vh', 'text-align':'center', 'overflowY':'scroll'},
                  children=[
                      ddk.Block(width=33,
                                # style={'margin': '10px'},
                                children=[ddk.Card(width=100,
                                                   style={'background-color': 'transparent', 'margin': '10px'},
                                                   children=[
                                                       ddk.CardHeader(title='Live',style={'background-color': 'transparent', 'margin': '10px'},),
                                                       html.Div(Card_matches)
                          ])]),
                      ddk.Block(width=33,
                                # style={'margin': '10px'},
                                children=[ddk.Card(width=100,
                                                   style={'background-color': 'transparent', 'margin': '10px'},
                                                   children=[
                                                       ddk.CardHeader(title='Matches',style={'background-color': 'transparent', 'margin': '10px'},),
                                                       html.Div(Card_matches)
                                                   ])]),
                      dcc.Interval(id='interval', interval=10000, n_intervals=0),
                      ddk.Block(width=33,
                                # style={'margin': '10px'},
                                children=[ddk.Card(width=100,
                                                   style={'background-color': 'transparent', 'margin': '10px'},
                                                   children=[
                                                       ddk.CardHeader(title='Results',style={'background-color': 'transparent', 'margin': '10px'},),
                                                       html.Div(Card_matches)
                                                   ])])])
    return layout
all_matches = serve_layout()


##########################    NEWS CARD   ###################################
news_item = dbc.ListGroupItem(style={'padding':'0px', 'border':'none'},
                              children=[ddk.Card(style={'background-color': '#073642',
                                                        'max-height':'100px', 'min-height':'100px',

                                                        'overflowY': 'hidden', 'text-align': 'center',
                                                        'margin':'0', 'padding':'0px'},
                                                 card_hover=True,
                                                 children=[ddk.CardHeader('Alliance прощаются с Fata и 33',
                                                                          style={'text-align': 'left', 'font-size':'12px','background-color': 'transparent',}),
                                                           html.H6("Команда Alliance опубликовала на своей странице сообщение об изменениях в текущем составе. Команду ...", style={'margin':'0', 'padding-bottom':'5px'})])])

##########################        MAIN PAGE      ##############################
def layout_main():

    # session_id = str(uuid.uuid1())
    # # store the session id in a dcc.Store component (invisible component for storing data)
    # store_session_id_div = dcc.Store(id='session_id_div_id',
    #                                  storage_type='session',  # IMPORTANT! see docstring of dcc.Store
    #                                  data=session_id)
    interval = dcc.Interval(id='interval', interval=20000, n_intervals=0)

    layout_main2 = ddk.Block(width=100,
                            style={'height': '93vh',
                             'text-align':'center',
                                   'background-image': 'url(/assets/png/eltv_fon2.png)',
                                   'background-repeat': 'no-repeat',
                                   'background-position': 'center',
                                   # 'background-size': 'auto 90%',
                                   'background-size': 'cover',
                                   },
                            children=[
                                ddk.Block(width=80,
                                          style={'height':'90vh', 'margin':'0',
                                                    'margin-top':"10px",
                                                   'padding':'0', 'color':'azure',
                                                   'overflowY': 'scroll', 'overflowX': 'hidden',
                                                   'justify':'center' },
                                          children=[
                                                # ddk.Block(width=30,
                                                #           children=dbc.ListGroup(flush=True,
                                                #                                  style={'margin': '0', 'border':'0'},
                                                #                                  children=[i for i in News_card.news_items()])),
                                                ddk.Block(width=70,
                                                          children=[ddk.Block(width=100,
                                                                              id='main_matches_live',
                                                                              style={'padding': '0',
                                                                                     'margin': '0',},
                                                                              children=[i for i in Live_matches.live()]),

                                                                    ddk.Block(width=100,
                                                                              children=[ddk.Card(width=50,
                                                                                                 id='main_matches',
                                                                                                 style={#073642
                                                                                                     'background-color': '#163d47',
                                                                                                     "opacity":"1",
                                                                                                     # 'background-color': '#07364275',
                                                                                                     'max-height': '50vh',
                                                                                                     'min-height': '50vh',
                                                                                                     'overflowY': 'hidden',
                                                                                                     'margin': '10px',
                                                                                                 'padding':'0'},
                                                                                                 children=[
                                                                                                     ddk.CardHeader(title='Матчи',
                                                                                                                    style={'background-color': '#1c424c',
                                                                                                                           'margin': '0px',
                                                                                                                           'padding': '15px',
                                                                                                                           'display':'block',
                                                                                                                           'font-size': '20px'}),
                                                                                                     Main_page.main_page()
                                                                                                 ]),
                                                                                        ddk.Card(width=50,
                                                                                                 id='main_results',
                                                                                                 style={#073642
                                                                                                     'background-color': '#163d47',
                                                                                                     "opacity":"1",
                                                                                                     # 'background-color': '#07364275',
                                                                                                     'max-height': '50vh',
                                                                                                     'min-height': '50vh',
                                                                                                     'overflowY': 'hidden',
                                                                                                     'margin': '10px',
                                                                                                 'padding':'0'},
                                                                                                 children=[
                                                                                                     ddk.CardHeader(title='Результаты',
                                                                                                                    style={'background-color': '#1c424c',
                                                                                                                           'margin': '0px',
                                                                                                                           'padding': '15px',
                                                                                                                           'display':'block',
                                                                                                                           'font-size': '20px'}),
                                                                                                     Result_page.result_page()
                                                                                                 ])]),


                                                                    ddk.Block(width=100,
                                                                              children=[ddk.Card(width=100,
                                                                                                 style={
                                                                                                     'background-color': '#163d47',
                                                                                                     'max-height': '50vh',
                                                                                                     "opacity":"1",
                                                                                                     'min-height': '50vh',
                                                                                                     'overflowY': 'hidden',
                                                                                                     'margin': '10px'},
                                                                                                 children=[
                                                                                                     ddk.CardHeader(title='Турниры',
                                                                                                                    style={'background-color': '#1c424c',
                                                                                                                           'margin': '0px',
                                                                                                                           'padding': '15px',
                                                                                                                           'display':'block',
                                                                                                                           'font-size': '20px'}),
                                                                                                     Main_tours_page.tour_page()])]),
                                                                    ddk.Block(width=100,
                                                                              children=[ddk.Card(width=100,
                                     rounded=10,
                                     card_hover=True,
                                     style={'max-height': 'fit-content',
                                            'height': '70px',
                                            'padding': '0px',
                                            'display': 'inline-block',
                                            # "width": '100%',
                                            'background-color': '#163d47',
                                            "opacity":"0.8",
                                            'align-items': 'center',
                                            # 'justify-content': 'flex-start',
                                            'justify-content': 'center',
                                            'margin': '5px',
                                            'vertical-align': '-webkit-baseline-middle',
                                            'textAlign': 'center',
                                            'color':"azure"
                                            # 'margin-left': '0',
                                            # 'margin-right': '0'
                                            },
                                     children=[html.P("© eltv.online 2020. Копирование материалов с сайта запрещена. Все права защищены.")])])]),


                    ]),
                                # dcc.Interval(id='interval',
                                #              interval=10000,
                                #              n_intervals=0)
    ])

    layout_main3 = html.Div(children=[layout_main2,
                                     # store_session_id_div,
                                     interval
                                     ])


    return layout_main3

layout_main = layout_main()
