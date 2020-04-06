import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
import uuid
import os
from app import dash_app

###########  Main Page   ################

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
                                                       ddk.CardHeader(title='Live'),
                                                       html.Div(Card_matches)
                          ])]),
                      ddk.Block(width=33,
                                # style={'margin': '10px'},
                                children=[ddk.Card(width=100,
                                                   style={'background-color': 'transparent', 'margin': '10px'},
                                                   children=[
                                                       ddk.CardHeader(title='Matches'),
                                                       html.Div(Card_matches)
                                                   ])]),
                      ddk.Block(width=33,
                                # style={'margin': '10px'},
                                children=[ddk.Card(width=100,
                                                   style={'background-color': 'transparent', 'margin': '10px'},
                                                   children=[
                                                       ddk.CardHeader(title='Results'),
                                                       html.Div(Card_matches)
                                                   ])])])
    return layout
layout_main = serve_layout()


#####       EXAMPLE of Table   ###########
Card_matches = dbc.ListGroup(flush=True,
                             style={'max-height':'-webkit-fill-available', 'overflowY':'scroll'},
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


match_head = ddk.Card(style={'width':'fit-content', 'margin':'10px', 'padding':'0', 'background-color': '#f9f9f91c',},
                                             children=[
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
                                                                   ddk.Block(width=30, children=[
                                                                       ddk.Logo(src='\\assets\\png\\1.png',
                                                                                style={
                                                                                     'max-height': '100px',
                                                                                     'height': '80px',
                                                                                     'width': '80px',
                                                                                    'text-align': 'left',
                                                                                     'padding': '0px', 'margin': '0',
                                                                                     'vertical-align': '-webkit-baseline-middle'})
                                                                   ]),
                                                               ])
                                                 ]),
                                                 ddk.Block(width=20,  style={'max-height':'fit-content'}, children=[]),
                                                 ddk.Block(width=40,  style={'max-height':'fit-content'}, children=[
                                                     ddk.Block(width=100,
                                                               children=[
                                                                   ddk.Block(width=30, children=[
                                                                       ddk.Logo(src='\\assets\\png\\2.png',
                                                                                style={
                                                                                    'max-height': '100px',
                                                                                    'text-align': 'right',
                                                                                    'height': '80px',
                                                                                     'width': '80px',
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

# create tab to enter a value
first_tab = dcc.Tab(label="Live",
                    children=[match_head,
                              match_head])

# create tab to retrieve the value entered in the other tab
second_tab = dcc.Tab(label="Statistics",
                     children=[match_head,
                               match_head,
                               match_head,
                               match_head,
                               match_head,
                               match_head])

# assemble tabs in dcc.Tabs object
tabs = dcc.Tabs(children=[first_tab, second_tab])



#####  ############   #############   ###########

layout1=ddk.Block(width=100,
                  style={'height': '90vh', 'text-align':'center', 'overflowY':'scroll',},
                  children=[
                      ddk.Block(width=70,
                                style={'height':'89vh', 'overflowY': 'scroll', 'overflowX': 'hidden', 'margin':'0', 'padding':'0', 'color':'azure'},
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
                                                       ddk.CardHeader(title='Live'),
                                                       Card_matches]),
                                          ddk.Card(width=100,
                                                   style={'background-color': 'transparent', 'max-height':'45vh', 'min-height':'45vh', 'overflowY': 'hidden','margin': '10px'},
                                                   children=[
                                                       ddk.CardHeader(title='Matches'),
                                                       Card_matches])
                                          ]),

])


layout2 = html.Div([
    html.H3('Slava 2'),
    dcc.Dropdown(
        id='app-2-dropdown',
        options=[
            {'label': 'App 2 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='app-2-display-value'),
    dcc.Link('Go to App 1', href='/app1')
])


