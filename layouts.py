import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
import uuid
import os
from app import dash_app
import pandas as pd
main_path_data = os.path.abspath("./data")

##################     ALL MATCHES     ####################################
def serve_layout():
    """Creates the layout for each user of the app.
    This function is executed each time a session is created for the app.
    It creates a new session id (a uuid.uuid1 as string) each time.

    This session id will be used in combination with a DashDatabase instance to manage user values.
    It will be fetched via the property data of a dcc.Store component.
    """

    # create a session id
    session_id = str(uuid.uuid1())
    # store the session id in a dcc.Store component (invisible component for storing data)
    store_session_id_div = dcc.Store(id='session_id_div_id',
                                     storage_type='session',  # IMPORTANT! see docstring of dcc.Store
                                     data=session_id)

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




###################       EXAMPLE of Table   ##############################
def cards_items():
    serverBD = pd.read_csv(main_path_data + '\\server.csv')
    cards = []
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
                ddk.Row(style={'max-height': 'fit-content',
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
                            ddk.Block(width=30,
                                      style={
                                     'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                     'align-items': 'center', 'justify-content': 'center',
                                     'margin': '0', 'textAlign': 'center',
                                          # 'width':'fit-content',
                                     'margin-left': '0', 'margin-right': '0'},
                                      children=[
                                          ddk.Block(width=40,
                                                    style={
                                                    'max-height': '30px',
                                                    'height': '30px',
                                                        'background-image': 'url(/assets/png/fon2.png)',
                                                        'background-repeat': 'no-repeat',
                                                        'background-position': 'center',
                                                        'background-size': 'auto 130%',
                                                        # 'background-size': 'cover',
                                                    # 'width': 'fit-content',
                                                     'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                     'align-items': 'center', 'justify-content': 'center',
                                                     'margin': '0', 'textAlign': 'center'},
                                                    children=ddk.Logo(
                                                        src=serverBD['T1logos'][ind],
                                                        style={'text-align': 'center',
                                                               'max-height': '-webkit-fill-available',
                                                               'padding': '0px', 'margin': '0',
                                                             'vertical-align': '-webkit-baseline-middle'})),
                                          ddk.Block(width=60,
                                                    style={
                                                        # 'overflowX': 'hidden',
                                             'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                             'align-items': 'center', 'justify-content': 'center',
                                             'margin': '0', 'textAlign': 'center'},
                                                  children=html.H6(serverBD['T1names'][ind],
                                                                  style={'color':'azure',
                                                                         # 'width': 'fit-content',
                                                                         'padding': '0px', 'margin': '0',
                                                            'max-height': '-webkit-fill-available',
                                                            'vertical-align': '-webkit-baseline-middle'}))]),
                            ddk.Block(width=20,
                                      style={'max-width': 'fit-content',
                                         'max-height': 'fit-content',
                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                         'align-items': 'center', 'justify-content': 'center',
                                         'margin': '0', 'textAlign': 'center',
                                         'margin-left': '10px', 'margin-right': '10px'},
                                      children=[html.H6(serverBD['Mtime'][ind],
                                                                  style={'height': '100%',
                                                                         'color': 'azure', 'padding':'0',
                                                                         'max-height': 'fit-content',
                                                                         'vertical-align': '-webkit-baseline-middle'})]),
                            ddk.Block(width=30,
                                      style={

                                     'padding': '0', 'vertical-align': '-webkit-baseline-middle',
                                     'align-items': 'center', 'justify-content': 'center',
                                     'margin': '0', 'textAlign': 'center',
                                          # 'width':'fit-content',
                                     'margin-left': '0', 'margin-right': '0'},
                                      children=[
                                        ddk.Block(width=60,
                                                  style={
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
                                        ddk.Block(width=40,
                                                  style={
                                                    'max-height': '30px',
                                                    'height': '30px',
                                                    # 'width': 'fit-content',
                                                     'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                                     'align-items': 'center', 'justify-content': 'center',
                                                     'margin': '0', 'textAlign': 'center'},
                                                  children=ddk.Logo(src=serverBD['T2logos'][ind],
                                                                    style={'text-align': 'center',
                                                                           'background-image': 'url(/assets/png/fon2.png)',
                                                        'background-repeat': 'no-repeat',
                                                        'background-position': 'center',
                                                        'background-size': 'auto 130%',
                                                               'max-height': '-webkit-fill-available',
                                                               'padding': '0px', 'margin': '0',
                                                             'vertical-align': '-webkit-baseline-middle'}))]),
                            ddk.Block(
                                # width=50,
                                      style={'max-width': '200px',
                                         'max-height': 'fit-content',
                                         'padding': '0px', 'vertical-align': '-webkit-baseline-middle',
                                         'align-items': 'center', 'justify-content': 'center',
                                         'margin': '0', 'textAlign': 'center',
                                         # 'margin-left': '10px', 'margin-right': '10px'
                                             },
                                      children=html.H6(serverBD['Mtour'][ind],
                                                  style={'height': '100%','color':'azure',
                                                         'max-height': 'fit-content',
                                                         'max-width': '200px',
                                                         'overflow-x':'hidden',
                                                         'margin': '0',
                                                         'vertical-align': '-webkit-baseline-middle'})),


                                      ])])
        cards.append(cards_items)
    return cards
Card_matches = dbc.ListGroup(flush=True,style={'max-height':'-webkit-fill-available',
                                               'overflowY':'scroll'},
                             children=[i for i in cards_items()])



##############     LIVE SCORE TABLES    ###################################
score_table_item = dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
                                           'height': '70px', 'justify-content': 'center',
                                           'vertical-align': '-webkit-baseline-middle',
                                           'max-height': 'fit-content', 'padding': '0px',
                                           'list-style': 'none',
                                           'align-items': 'center'},
                                     children=[
                                         ddk.Block(width=100,
                                                   style={'justify-content': 'center'},
                                                   children=[ddk.Block(width=15,
                                                                             style={'vertical-align': '-webkit-baseline-middle'},
                                                                             children=html.H6('PLAYER1',style={'margin': '0',
                                                                                                           'text-align': 'center',
                                                                                                           'justify': 'center'})),
                                                                   ddk.Block(width=15,
                                                                             style={'vertical-align': '-webkit-baseline-middle'},
                                                                             children=ddk.Block(
                                                                                 width=80,
                                                                                 style={
                                                                         'max-height': '20px',
                                                                         'height': '20px',
                                                                         'width': 'fit-content'},
                                                                                 children=[ddk.Logo(
                                                                         src='\\assets\\png\\1.png',
                                                                         style={
                                                                             'text-align': 'center',
                                                                             'max-height': '20px',
                                                                             'padding': '0',
                                                                             'margin': '0',
                                                                             'vertical-align': '-webkit-baseline-middle'})])),
                                                                   ddk.Block(width=10,
                                                                             style={'vertical-align': '-webkit-baseline-middle'},
                                                                             children=html.H6('6/ 2/ 5',style={'margin': '0',
                                                                                                           'text-align': 'center',
                                                                                                           'justify': 'center'})),



                                                                   ddk.Block(width=20,
                                                                             style={'vertical-align': '-webkit-baseline-middle'},
                                                                             children=[
                                                                                 ddk.Block(
                                                                                 width=16,
                                                                                 style={
                                                                         'max-height': '15px',
                                                                         'height': '15px',
                                                                         'width': 'fit-content'},
                                                                                 children=[ddk.Logo(
                                                                         src='\\assets\\png\\1.png',
                                                                         style={
                                                                             'text-align': 'center',
                                                                             'max-height': '15px',
                                                                             'padding': '0',
                                                                             'margin': '0',
                                                                             'vertical-align': '-webkit-baseline-middle'})]),
                                                                                 ddk.Block(
                                                                                 width=16,
                                                                                 style={
                                                                         'max-height': '15px',
                                                                         'height': '15px',
                                                                         'width': 'fit-content'},
                                                                                 children=[ddk.Logo(
                                                                         src='\\assets\\png\\1.png',
                                                                         style={
                                                                             'text-align': 'center',
                                                                             'max-height': '15px',
                                                                             'padding': '0',
                                                                             'margin': '0',
                                                                             'vertical-align': '-webkit-baseline-middle'})]),
                                                                                 ddk.Block(
                                                                                 width=16,
                                                                                 style={
                                                                         'max-height': '15px',
                                                                         'height': '15px',
                                                                         'width': 'fit-content'},
                                                                                 children=[ddk.Logo(
                                                                         src='\\assets\\png\\1.png',
                                                                         style={
                                                                             'text-align': 'center',
                                                                             'max-height': '15px',
                                                                             'padding': '0',
                                                                             'margin': '0',
                                                                             'vertical-align': '-webkit-baseline-middle'})]),
                                                                                 ddk.Block(
                                                                                 width=16,
                                                                                 style={
                                                                         'max-height': '15px',
                                                                         'height': '15px',
                                                                         'width': 'fit-content'},
                                                                                 children=[ddk.Logo(
                                                                         src='\\assets\\png\\1.png',
                                                                         style={
                                                                             'text-align': 'center',
                                                                             'max-height': '15px',
                                                                             'padding': '0',
                                                                             'margin': '0',
                                                                             'vertical-align': '-webkit-baseline-middle'})]),
                                                                                 ddk.Block(
                                                                                 width=16,
                                                                                 style={
                                                                         'max-height': '15px',
                                                                         'height': '15px',
                                                                         'width': 'fit-content'},
                                                                                 children=[ddk.Logo(
                                                                         src='\\assets\\png\\1.png',
                                                                         style={
                                                                             'text-align': 'center',
                                                                             'max-height': '15px',
                                                                             'padding': '0',
                                                                             'margin': '0',
                                                                             'vertical-align': '-webkit-baseline-middle'})]),
                                                                                 ddk.Block(
                                                                                 width=16,
                                                                                 style={
                                                                         'max-height': '15px',
                                                                         'height': '15px',
                                                                         'width': 'fit-content'},
                                                                                 children=[ddk.Logo(
                                                                         src='\\assets\\png\\1.png',
                                                                         style={
                                                                             'text-align': 'center',
                                                                             'max-height': '15px',
                                                                             'padding': '0',
                                                                             'margin': '0',
                                                                             'vertical-align': '-webkit-baseline-middle'})])


                                                                             ]),
                                                                   ddk.Block(width=10,
                                                                             style={'vertical-align': '-webkit-baseline-middle'},
                                                                             children=html.H6('95',style={'margin': '0',
                                                                                                           'text-align': 'center',
                                                                                                           'justify': 'center'})),
                                                                   ddk.Block(width=10,
                                                                             style={'vertical-align': '-webkit-baseline-middle'},
                                                                             children=html.H6('193/11',
                                                                                 style={
                                                                                     'margin': '0',
                                                                                     'text-align': 'center',
                                                                                     'justify': 'center'})),
                                                                   ddk.Block(width=10,
                                                                             style={'vertical-align': '-webkit-baseline-middle'},
                                                                             children=html.H6('620/961',style={'margin': '0',
                                                                                                            'text-align': 'center',
                                                                                                            'justify': 'center'})),
                                                                   ddk.Block(width=10,
                                                                             style={'vertical-align': '-webkit-baseline-middle'},
                                                                             children=html.H6('13352',style={'margin': '0',
                                                                                                           'text-align': 'center',
                                                                                                           'justify': 'center'}))])])
score_table = ddk.Card(style={'width':'-webkit-fill-available',
                              'margin':'10px',
                              'padding':'0',
                              'background-color': '#f9f9f91c',}, children=[dbc.ListGroup(flush=True, children=[
                                            dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
                                                                       'height': '40px', 'justify-content': 'center',
                                                                       'vertical-align': '-webkit-baseline-middle',
                                                                       'max-height': 'fit-content', 'padding': '0px',
                                                                       'background-color':'#0e4e70',
                                                                       'list-style': 'none',
                                                                       'align-items': 'center'},
                                                              children=[ddk.Block(width=100,
                                                                                 style={'justify-content': 'center','vertical-align': '-webkit-baseline-middle','height': '40px',},
                                                                                 children=[ddk.Block(width=15,
                                                                                                     style={'vertical-align': '-webkit-baseline-middle'},
                                                                                                     children=html.H2('PLAYER',style={'margin': '0',
                                                                                                                                   'text-align': 'center',
                                                                                                                                   'justify': 'center'})),
                                                                                           ddk.Block(width=15,
                                                                                                     style={'vertical-align': '-webkit-baseline-middle'},
                                                                                                     children=html.H2('HERO',style={'margin': '0',
                                                                                                                                   'text-align': 'center',
                                                                                                                                   'justify': 'center'})),
                                                                                           ddk.Block(width=10,
                                                                                                     style={'vertical-align': '-webkit-baseline-middle'},
                                                                                                     children=html.H2('KDA',style={'margin': '0',
                                                                                                                                   'text-align': 'center',
                                                                                                                                   'justify': 'center'})),
                                                                                           ddk.Block(width=20,
                                                                                                     style={'vertical-align': '-webkit-baseline-middle'},
                                                                                                     children=html.H2('ITEMS',style={'margin': '0',
                                                                                                                                   'text-align': 'center',
                                                                                                                                   'justify': 'center'})),
                                                                                           ddk.Block(width=10,
                                                                                                     style={'vertical-align': '-webkit-baseline-middle'},
                                                                                                     children=html.H2('GOLD',style={'margin': '0',
                                                                                                                                   'text-align': 'center',
                                                                                                                                   'justify': 'center'})),
                                                                                           ddk.Block(width=10,
                                                                                                     style={'vertical-align': '-webkit-baseline-middle'},
                                                                                                     children=html.H2('LH/DN',
                                                                                                         style={
                                                                                                             'margin': '0',
                                                                                                             'text-align': 'center',
                                                                                                             'justify': 'center'})),
                                                                                           ddk.Block(width=10,
                                                                                                     style={'vertical-align': '-webkit-baseline-middle'},
                                                                                                     children=html.H2('GPM/XPM',style={'margin': '0',
                                                                                                                                    'text-align': 'center',
                                                                                                                                    'justify': 'center'})),
                                                                                           ddk.Block(width=10,
                                                                                                     style={'vertical-align': '-webkit-baseline-middle'},
                                                                                                     children=html.H2('NW',style={'margin': '0',
                                                                                                                                   'text-align': 'center',
                                                                                                                                   'justify': 'center'}))])]),
                                                 score_table_item,
                                                 score_table_item,
                                                 score_table_item,
                                                 score_table_item,
                                                 score_table_item



                                             ])])






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

    # df.iloc[0]['Mtour']



    ##############     HEAD CARD of MATCH   ###################################
    match_head = ddk.Card(style={'width': '-webkit-fill-available',
                                 'min-height': '120px',
                                 'margin': '10px',
                                 'padding': '15px',
                                 'background-color': '#f9f9f91c'}, children=[
        ddk.Block(width=100, style={'height': 'fit-content', },
                  children=[html.H2(df.iloc[0]['Mtour'], style={'text-align': 'center',
                                                                'text-color': 'azure',
                                                                'margin': '0'})]),
        ddk.Block(width=100, style={'max-height': 'fit-content'},
                  children=[html.H6('{} {}'.format(df.iloc[0]['Mdate'], df.iloc[0]['Mtime']), style={'text-align': 'center', 'margin': '0'})]),
        ddk.Block(width=40, style={'max-height': 'fit-content'}, children=[
            ddk.Block(width=100,
                      children=[
                          ddk.Block(width=70, children=[
                              ddk.Block(width=100,
                                        children=html.H2(df.iloc[0]['T1name'],
                                                         style={
                                                             'text-align': 'right', 'margin': '0'})),
                              ddk.Block(width=100,
                                        children=html.H6('{}, {}, {}, {}, {}'.format(df.iloc[0]['P11'],
                                                                                     df.iloc[0]['P12'],
                                                                                     df.iloc[0]['P13'],
                                                                                     df.iloc[0]['P14'],
                                                                                     df.iloc[0]['P15']),
                                                         style={
                                                             'text-align': 'right', 'margin': '0'})),

                          ]),
                          ddk.Block(width=30,
                                    style={'max-height': '40px', 'max-width': '40px', 'margin-left': '15px'},
                                    children=[
                                        ddk.Logo(src=df.iloc[0]['T1logo'],
                                                 style={
                                                     'max-height': '40px',
                                                     'height': '40px',
                                                     'width': '40px',
                                                     'text-align': 'center',
                                                     'padding': '0px', 'margin': '0',
                                                     'vertical-align': '-webkit-baseline-middle'})
                                    ]),
                      ])
        ]),
        ddk.Block(width=20,
                  style={'max-height': 'fit-content'},
                  children=[html.H1('{} : {}'.format(df.iloc[0]['T1score'], df.iloc[0]['T2score']),
                                    style={'text-align': 'center', 'font-size': '40px', 'margin': '0'})]),
        ddk.Block(width=40, style={'max-height': 'fit-content'}, children=[
            ddk.Block(width=100,
                      children=[
                          ddk.Block(width=30,
                                    style={'max-height': '40px', 'max-width': '40px', 'margin-right': '15px'},
                                    children=[
                                        ddk.Logo(src=df.iloc[0]['T2logo'],
                                                 style={
                                                     'max-height': '40px',
                                                     'text-align': 'center',
                                                     'height': '40px',
                                                     'width': '40px',
                                                     'padding': '0px', 'margin': '0',
                                                     'vertical-align': '-webkit-baseline-middle'})
                                    ]),
                          ddk.Block(width=70, children=[
                              ddk.Block(width=100, children=html.H2(df.iloc[0]['T2name'],
                                                                    style={'text-align': 'left', 'margin': '0'})),
                              ddk.Block(width=100, children=html.H6('{}, {}, {}, {}, {}'.format(df.iloc[0]['P21'],
                                                                                     df.iloc[0]['P22'],
                                                                                     df.iloc[0]['P23'],
                                                                                     df.iloc[0]['P24'],
                                                                                     df.iloc[0]['P25']),
                                                                    style={'text-align': 'left', 'margin': '0'})),

                          ]),

                      ])
        ]),
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
        ddk.Block(width=100,
                  children=dbc.ListGroup(flush=True, children=[i for i in rrr[0]]))

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
    first_tab = dcc.Tab(label="Live", children=[live_teams,
                                                ddk.Block(width=100,
                                                          children=html.H2('Team 1', style={'margin': '0px'})),
                                                score_table,
                                                ddk.Block(width=100,
                                                          children=html.H2('Team 2', style={'margin': '0px'})),
                                                score_table], style={'margin': '10px',
                                                                     'border-radius': '10px',
                                                                     'background-color': '#0e4e70', 'color': 'azure',
                                                                     'border': '1px solid rgb(14, 78, 112)'},
                        selected_style={'margin': '10px', 'border-radius': '10px',
                                        'background-color': '#0e4e70', 'color': 'azure', 'border': '2px solid #1f78b4'})
    second_tab = dcc.Tab(label="Statistics", children=[stat,
                                                       chart_table], style={'margin': '10px',
                                                                            'border-radius': '10px',
                                                                            'background-color': '#0e4e70',
                                                                            'color': 'azure',
                                                                            'border': '1px solid rgb(14, 78, 112)'},
                         selected_style={'margin': '10px',
                                         'border-radius': '10px', 'background-color': '#0e4e70', 'color': 'azure',
                                         'border': '2px solid #1f78b4'})
    tabs = dcc.Tabs(children=[first_tab, second_tab])





    match_card = ddk.Block(width=100, style={'height': '90vh',
                             'text-align':'center'}, children=[
                          ddk.Block(width=70,
                                    style={'height':'89vh', 'margin':'0', 'padding':'0', 'color':'azure', 'overflowY': 'scroll', 'overflowX': 'hidden', },
                                    children=[
                                        match_head,
                                        ddk.Card(style={'width':'-webkit-fill-available', 'margin':'10px', 'padding':'0', 'background-color': '#f9f9f91c',},
                                                 children=tabs),


                                    ]),
                          ddk.Block(width=30,
                                    style={'height':'90vh'},
                                    children=[ddk.Card(width=100,
                                                       style={'background-color': 'transparent', 'max-height':'40vh', 'min-height':'40vh', 'overflowY': 'hidden', 'margin':'10px'},
                                                       children=[
                                                           ddk.CardHeader(title='Live', style={'background-color': 'transparent'}),
                                                           Card_matches]),
                                              ddk.Card(width=100,
                                                       style={'background-color': 'transparent', 'max-height':'45vh', 'min-height':'45vh', 'overflowY': 'hidden','margin': '10px'},
                                                       children=[
                                                           ddk.CardHeader(title='Matches', style={'background-color': 'transparent'}),
                                                           Card_matches])
                                              ])])

    return match_card





##########################    NEWS CARD   ###################################
news_item = dbc.ListGroupItem(style={'padding':'0px', 'border':'none'},
                              children=[ddk.Card(style={'background-color': '#f9f9f91c',
                                                        'max-height':'100px', 'min-height':'100px', 'overflowY': 'hidden', 'text-align': 'center','margin':'0', 'padding':'0px'},
                                                 card_hover=True,
                                                 children=[ddk.CardHeader('Alliance прощаются с Fata и 33',
                                                                          style={'text-align': 'left', 'font-size':'12px','background-color': 'transparent',}),
                                                           html.H6("Команда Alliance опубликовала на своей странице сообщение об изменениях в текущем составе. Команду ...", style={'margin':'0', 'padding-bottom':'5px'})])])

##########################    TOP 3 LIVE   ###################################
top3_live = ddk.Card(width=33,
                     card_hover=True,
                     style={'margin':'5px',
                            'background-color': '#f9f9f91c', 'max-height':'fit-content',
                            # 'min-height':'100px'
                            },
                     children=[ddk.Block(width=100,
                                         style={'text-align':'center'},
                                         children=[ddk.Block(width=46,
                                                             style={'max-height': '40px','max-width': '-webkit-fill-available', 'height': '40px','text-align':'center',
                                                                    'vertical-align': '-webkit-baseline-middle'},
                                                             children=[ddk.Logo(
                                                 src='\\assets\\png\\1.png',
                                                 style={
                                                     'text-align': 'center',
                                                     'max-height': '40px',
                                                     'padding': '0',
                                                     'margin': '0',
                                                     'vertical-align': '-webkit-baseline-middle'})]),
                                                   ddk.Block(width=8,
                                                             children=[html.H6('vs', style={'padding':'0px', 'margin':'0', 'vertical-align': '-webkit-baseline-middle'},)]),
                                                   ddk.Block(width=46,
                                                             style={'max-height': '40px','max-width': '-webkit-fill-available','height': '40px','text-align':'center',
                                                                    'vertical-align': '-webkit-baseline-middle'},
                                                             children=[ddk.Logo(
                                                 src='\\assets\\png\\2.png',
                                                 style={
                                                     'text-align': 'center',
                                                     'max-height': '40px',
                                                     'padding': '0',
                                                     'margin': '0',
                                                     'vertical-align': '-webkit-baseline-middle'})])
                               ]),
                               ddk.Block(width=100,
                                         children=[ddk.Block(width=50,
                                                             children=[html.H2('NiP', style={'padding':'0px', 'margin':'0'},)]),
                                                   ddk.Block(width=50,
                                                             children=[html.H2('ChickenF', style={'padding':'0px', 'margin':'0'},)])]),
                               ddk.Block(width=100,
                                         children=[ddk.Block(width=40,
                                                             children=[html.H1('2', style={'padding':'0px', 'margin':'0', 'text-align': 'right'},)]),
                                                   ddk.Block(width=20,
                                                             children=[html.H6('-', style={'padding':'0px', 'margin':'0'},)]),
                                                   ddk.Block(width=40,
                                                             children=[html.H1('1', style={'padding':'0px', 'margin':'0','text-align': 'left'},)])])
                               ])


##########################        MAIN PAGE      ##############################
layout_main = ddk.Block(width=100,
                        style={'height': '90vh',
                         'text-align':'center'},
                        children=[
                      ddk.Block(width=80,
                                style={'height':'90vh', 'margin':'0',
                                       'padding':'0', 'color':'azure',
                                       'overflowY': 'scroll', 'overflowX': 'hidden',
                                       'justify':'center' },
                                children=[
                                    ddk.Block(width=30,
                                              children=dbc.ListGroup(flush=True, style={'margin': '0', 'border':'0'}, children=[news_item,
                                                                                  news_item,news_item,news_item,news_item,news_item])),
                                    ddk.Block(width=70,
                                              children=[ddk.Block(width=100,
                                                                  style={'padding': '0',
                                                                         'margin': '0',},
                                                                  children=[top3_live,top3_live,top3_live]),
                                                        ddk.Block(width=100,
                                                                  children=[ddk.Card(width=100,
                                                                                     style={
                                                                                         'background-color': 'transparent',
                                                                                         'max-height': '50vh',
                                                                                         'min-height': '50vh',
                                                                                         'overflowY': 'hidden',
                                                                                         'margin': '10px'},
                                                                                     children=[
                                                                                         ddk.CardHeader(title='Матчи',
                                                                                                        style={'background-color': 'transparent',
                                                                                                               'margin': '10px'},),
                                                                                         Card_matches])]),
                                                        ddk.Block(width=100,
                                                                  children=[ddk.Card(width=100,
                                                                                     style={
                                                                                         'background-color': 'transparent',
                                                                                         'max-height': '50vh',
                                                                                         'min-height': '50vh',
                                                                                         'overflowY': 'hidden',
                                                                                         'margin': '10px'},
                                                                                     children=[
                                                                                         ddk.CardHeader(title='Турнииры',
                                                                                                        style={'background-color': 'transparent',
                                                                                                               'margin': '10px'}),
                                                                                         Card_matches])]),
                                                        ddk.Block(width=100,
                                                                  children=[top3_live,top3_live,top3_live])]),
]),
])


