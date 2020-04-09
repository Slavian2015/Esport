import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
import uuid
import os
from app import dash_app

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


###################  TEAMS CARD of MATCH  #################################
live_teams= ddk.Card(style={'width':'-webkit-fill-available',
                            'margin':'10px',
                            'padding':'0',
                            'background-color': '#f9f9f91c'}, children=[
                                                 ddk.Block(width=100,
                                                           style={'height':'fit-content','vertical-align': '-webkit-baseline-middle'},
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
                                                                                                 src='\\assets\\png\\profil.png',
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
                                                                                                 html.H6('Player1',
                                                                                                         style={
                                                                                                             'text-align': 'center',
                                                                                                             'margin': '0'})]),
                                                                                   ddk.Block(width=100, style={
                                                                                       'max-width': '100px',
                                                                                       'height': 'fit-content'},
                                                                                             children=[html.P('1500',
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
                                                                                                               src='\\assets\\png\\profil.png',
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
                                                                                                                         'Player1',
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
                                                                                                                         '1500',
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
                                                                                                               src='\\assets\\png\\profil.png',
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
                                                                                                                         'Player1',
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
                                                                                                                         '1500',
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
                                                                                                               src='\\assets\\png\\profil.png',
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
                                                                                                                         'Player1',
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
                                                                                                                         '1500',
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
                                                                                                               src='\\assets\\png\\profil.png',
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
                                                                                                                         'Player1',
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
                                                                                                                         '1500',
                                                                                                                         style={
                                                                                                                             'text-align': 'center',
                                                                                                                             'margin': '0'})])]), ]),


                                                                     ddk.Block(width=20,
                                                                               style={'height':'100px','vertical-align': '-webkit-baseline-middle', 'padding': '10px'},
                                                                               children=[ddk.Block(width=100,
                                                                                                   style={'height':'33%'},
                                                                                                   children=[ddk.Block(width=30, style={'height':'fit-content', 'vertical-align': 'middle'}, children=[html.H6('44%', style={'text-align':'center', 'padding': '0px', 'margin':'0'})]),
                                                                                                             ddk.Block(width=40, style={'height':'fit-content', 'vertical-align': 'middle'}, children=[html.H2('WR', style={'text-align':'center', 'padding': '0px', 'margin':'0'})]),
                                                                                                             ddk.Block(width=30, style={'height':'fit-content', 'vertical-align': 'middle'}, children=[html.H6('27%', style={'text-align':'center', 'padding': '0px', 'margin':'0'})])]),
                                                                                         ddk.Block(width=100, style={'height':'33%'}, children=[ddk.Block(width=30, style={'height':'fit-content', 'vertical-align': 'middle'}, children=[html.H6('25%', style={'text-align':'center', 'padding': '0px', 'margin':'0'})]),
                                                                                                             ddk.Block(width=40, style={'height':'fit-content', 'vertical-align': 'middle'}, children=[html.H2('FB', style={'text-align':'center', 'padding': '0px', 'margin':'0'})]),
                                                                                                             ddk.Block(width=30, style={'height':'fit-content', 'vertical-align': 'middle'}, children=[html.H6('16%', style={'text-align':'center', 'padding': '0px', 'margin':'0'})])]),
                                                                                         ddk.Block(width=100, style={'height':'33%'}, children=[ddk.Block(width=30, style={'height':'fit-content', 'vertical-align': 'middle'}, children=[html.H6('32%', style={'text-align':'center', 'padding': '0px', 'margin':'0'})]),
                                                                                                             ddk.Block(width=40, style={'height':'fit-content', 'vertical-align': 'middle'}, children=[html.H2('F10', style={'text-align':'center', 'padding': '0px', 'margin':'0'})]),
                                                                                                             ddk.Block(width=30, style={'height':'fit-content', 'vertical-align': 'middle'}, children=[html.H6('22%', style={'text-align':'center', 'padding': '0px', 'margin':'0'})])])]),




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
                                                                                                 src='\\assets\\png\\profil.png',
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
                                                                                                 html.H6('Player1',
                                                                                                         style={
                                                                                                             'text-align': 'center',
                                                                                                             'margin': '0'})]),
                                                                                   ddk.Block(width=100, style={
                                                                                       'max-width': '100px',
                                                                                       'height': 'fit-content'},
                                                                                             children=[html.P('1500',
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
                                                                                                               src='\\assets\\png\\profil.png',
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
                                                                                                                         'Player1',
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
                                                                                                                         '1500',
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
                                                                                                               src='\\assets\\png\\profil.png',
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
                                                                                                                         'Player1',
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
                                                                                                                         '1500',
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
                                                                                                               src='\\assets\\png\\profil.png',
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
                                                                                                                         'Player1',
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
                                                                                                                         '1500',
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
                                                                                                               src='\\assets\\png\\profil.png',
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
                                                                                                                         'Player1',
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
                                                                                                                         '1500',
                                                                                                                         style={
                                                                                                                             'text-align': 'center',
                                                                                                                             'margin': '0'})])]), ])]),
                                             ])

###################       EXAMPLE of Table   ##############################
Card_matches = dbc.ListGroup(flush=True,style={'max-height':'-webkit-fill-available',
                                               'overflowY':'scroll'},
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
                                                                                style={'text-align': 'center',
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
                                                                                style={'text-align': 'center',
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

##############     HEAD CARD of MATCH   ###################################
match_head = ddk.Card(style={'width':'-webkit-fill-available',
                             'min-height': '120px',
                             'margin':'10px',
                             'padding':'15px',
                             'background-color': '#f9f9f91c'}, children=[
                                                 ddk.Block(width=100, style={'height':'fit-content', }, children=[html.H2('Матч RNG vs NewBee', style={'text-align':'center', 'margin':'0'})]),
                                                 ddk.Block(width=100, style={'max-height':'fit-content'}, children=[html.H6('05 апрб 11:15 MSK', style={'text-align':'center', 'margin':'0'})]),
                                                 ddk.Block(width=40,  style={'max-height':'fit-content'}, children=[
                                                     ddk.Block(width=100,
                                                               children=[
                                                                   ddk.Block(width=70, children=[
                                                                       ddk.Block(width=100,
                                                                                 children=html.H2('Royal Never Give Up',
                                                                                                  style={
                                                                                                      'text-align': 'right', 'margin':'0'})),
                                                                       ddk.Block(width=100,
                                                                                 children=html.H6('P1, P2, P3, P4, P5',
                                                                                                  style={
                                                                                                      'text-align': 'right', 'margin':'0'})),

                                                                   ]),
                                                                   ddk.Block(width=30,
                                                                             style={'max-height':'40px', 'max-width':'40px', 'margin-left':'15px'},
                                                                             children=[
                                                                       ddk.Logo(src='\\assets\\png\\1.png',
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
                                                 ddk.Block(width=20,  style={'max-height':'fit-content'}, children=[html.H1('1 : 2', style={'text-align':'center', 'font-size': '40px', 'margin':'0'})]),
                                                 ddk.Block(width=40,  style={'max-height':'fit-content'}, children=[
                                                     ddk.Block(width=100,
                                                               children=[
                                                                   ddk.Block(width=30,
                                                                             style={'max-height':'40px', 'max-width':'40px','margin-right':'15px'},
                                                                             children=[
                                                                       ddk.Logo(src='\\assets\\png\\3.png',
                                                                                style={
                                                                                    'max-height': '40px',
                                                                                    'text-align': 'center',
                                                                                    'height': '40px',
                                                                                     'width': '40px',
                                                                                    'padding': '0px', 'margin': '0',
                                                                                    'vertical-align': '-webkit-baseline-middle'})
                                                                   ]),
                                                                   ddk.Block(width=70, children=[
                                                                       ddk.Block(width=100, children=html.H2('Royal Never Give Up', style={'text-align':'left', 'margin':'0'})),
                                                                       ddk.Block(width=100, children=html.H6('P1, P2, P3, P4, P5', style={'text-align':'left', 'margin':'0'})),

                                                                   ]),

                                                               ])
                                                 ]),
])

##############     LIVE SCORE TABLES    ###################################
score_table_item = dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
                                           'height': '70px', 'justify-content': 'center',
                                           'vertical-align': '-webkit-baseline-middle',
                                           'max-height': 'fit-content', 'padding': '0px',
                                           'list-style': 'none',
                                           'align-items': 'center'}, children=[ddk.Block(width=100,
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
                              'background-color': '#f9f9f91c'}, children=ddk.Block(width=100,style={'justify-content': 'center',
                                                                       'vertical-align': '-webkit-baseline-middle',
                                                                       'height': '250px',
                                                                       'width': '100%',}, children=[ddk.Logo(src='\\assets\\png\\charts.png',
                                                                                style={
                                                                                     'max-height': '-webkit-fill-available',
                                                                                     'height': '-webkit-fill-available',
                                                                                     'width': '100%',
                                                                                    'text-align': 'left',
                                                                                     'padding': '0px', 'margin': '0',
                                                                                     'vertical-align': '-webkit-baseline-middle'})]))


##############     H 2 H card items    ###################################
head_list_item = ddk.Block(width=100, style={'vertical-align': '-webkit-baseline-middle',
                                  'height':'35px'}, children=[ddk.Block(width=20, style={'vertical-align': '-webkit-baseline-middle'}, children=[html.H2('1', style={'vertical-align': '-webkit-baseline-middle','text-align': 'center', 'margin': '0'})]),
                                                ddk.Block(width=60, style={'vertical-align': '-webkit-baseline-middle'}, children=[html.H6('05.04.20 ', style={'vertical-align': '-webkit-baseline-middle','text-align': 'center', 'margin': '0'})]),
                                                ddk.Block(width=20, style={'vertical-align': '-webkit-baseline-middle'}, children=[html.H2('2', style={'vertical-align': '-webkit-baseline-middle','text-align': 'center', 'margin': '0'})])])
head_list = dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
                                                                       'height': '40px', 'justify-content': 'center',
                                                                       'vertical-align': '-webkit-baseline-middle',
                                                                       'max-height': 'fit-content', 'padding': '0px',
                                                                       # 'background-color':'#0e4e70',
                                                                       'list-style': 'none',
                                                                       'align-items': 'center'}, children=[head_list_item])
head_to_head = ddk.Card(style={'width':'-webkit-fill-available',
                               'margin':'10px',
                               'padding':'0',
                               'background-color': '#f9f9f91c'}, children=[
                                                 ddk.Block(width=100, children=[ddk.Block(width=30, style={'vertical-align': '-webkit-baseline-middle',},children=[ddk.Block(width=100, children=[html.H6('Побед', style={'text-align': 'center', 'margin': '0'})]),
                                                                                                              ddk.Block(width=100, children=[html.H2('3', style={'text-align': 'center', 'margin': '0'})])]),
                                                                                ddk.Block(width=40, style={'vertical-align': '-webkit-baseline-middle',},children=[ddk.Card(shadow_weight='medium', style={'background-color':'transparent'}, children=[html.H2('4', style={'text-align': 'center', 'margin': '0'})])]),
                                                                                ddk.Block(width=30, style={'vertical-align': '-webkit-baseline-middle',},children=[ddk.Block(width=100, children=[html.H6('Побед', style={'text-align': 'center', 'margin': '0'})]),
                                                                                                              ddk.Block(width=100, children=[html.H2('1', style={'text-align': 'center', 'margin': '0'})])])]),
                                                 ddk.Block(width=100, children=dbc.ListGroup(flush=True, children=[head_list, head_list,head_list,head_list,head_list,head_list]))])


##############     Total games card items    ##############################
stat_list_item = ddk.Block(width=100, style={'vertical-align': '-webkit-baseline-middle',
                                             'height':'35px'},children=[ddk.Block(width=50,
                                               style={'vertical-align': '-webkit-baseline-middle'},
                                               children=[
                                                   ddk.Block(
                                                         width=25,
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
                                                           src='\\assets\\png\\2.png',
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
                                                           src='\\assets\\png\\w.png',
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
                                                           src='\\assets\\png\\l.png',
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
                                                 src='\\assets\\png\\2.png',
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
                                                           src='\\assets\\png\\1.png',
                                                           style={
                                                               'text-align': 'center',
                                                               'max-height': '20px',
                                                               'padding': '0',
                                                               'margin': '0',
                                                               'vertical-align': '-webkit-baseline-middle'})]),

                                               ])])
stat_list = dbc.ListGroupItem(style={'line-height': '1', 'margin': '0', 'margin-right': '0',
                                                                       'height': '40px', 'justify-content': 'center',
                                                                       'vertical-align': '-webkit-baseline-middle',
                                                                       'max-height': 'fit-content', 'padding': '0px',
                                                                       # 'background-color':'#0e4e70',
                                                                       'list-style': 'none',
                                                                       'align-items': 'center'}, children=[stat_list_item])
stat_teams = ddk.Card(style={'width':'-webkit-fill-available',
                             'margin':'10px', 'padding':'0',
                             'background-color': '#f9f9f91c',},children=[
                                                 ddk.Block(width=100, children=[ddk.Block(width=30, style={'vertical-align': '-webkit-baseline-middle',},children=[ddk.Block(width=100, children=[html.H6('Побед', style={'text-align': 'center', 'margin': '0'})]),
                                                                                                              ddk.Block(width=100, children=[html.H2('3', style={'text-align': 'center', 'margin': '0'})])]),
                                                                                ddk.Block(width=40, style={'vertical-align': '-webkit-baseline-middle',},children=[ddk.Card(shadow_weight='medium', style={'background-color':'transparent'}, children=[html.H2('4', style={'text-align': 'center', 'margin': '0'})])]),
                                                                                ddk.Block(width=30, style={'vertical-align': '-webkit-baseline-middle',},children=[ddk.Block(width=100, children=[html.H6('Побед', style={'text-align': 'center', 'margin': '0'})]),
                                                                                                              ddk.Block(width=100, children=[html.H2('1', style={'text-align': 'center', 'margin': '0'})])])]),
                                                 ddk.Block(width=100, children=dbc.ListGroup(flush=True, children=[stat_list, stat_list,stat_list,stat_list,stat_list]))


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
first_tab = dcc.Tab(label="Live",children=[live_teams,
                              ddk.Block(width=100, children=html.H2('Team 1', style={'margin': '0px'})),
                              score_table,
                              ddk.Block(width=100, children=html.H2('Team 2', style={'margin': '0px'})),
                              score_table],style={'margin': '10px',
                           'border-radius': '10px', 'background-color': '#0e4e70', 'color':'azure', 'border':'1px solid rgb(14, 78, 112)'},selected_style={'margin': '10px', 'border-radius': '10px',
                                    'background-color': '#0e4e70', 'color':'azure', 'border':'2px solid #1f78b4' })
second_tab = dcc.Tab(label="Statistics",children=[stat,
                               chart_table],style={'margin': '10px',
                                                   'border-radius': '10px', 'background-color': '#0e4e70', 'color':'azure', 'border':'1px solid rgb(14, 78, 112)'},selected_style={'margin': '10px',
                                     'border-radius': '10px', 'background-color': '#0e4e70', 'color':'azure', 'border':'2px solid #1f78b4' })
tabs = dcc.Tabs(children=[first_tab, second_tab])



##########################    ONE MATCH CARD   ##############################
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
                                          ]),

])



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
                                                                                         'max-height': '30vh',
                                                                                         'min-height': '30vh',
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
                                                                                         'max-height': '30vh',
                                                                                         'min-height': '30vh',
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


