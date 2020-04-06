import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_design_kit as ddk
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash_database import DashDatabase
import flask
import uuid


# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

external_stylesheets = [dbc.themes.SOLAR]



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

    # create tab to enter a value
    first_tab = dcc.Tab(label="Enter a value",
                        children=[dcc.Input(placeholder="Enter value here", id="input_div"),
                                  html.Button(children="OK", id="ok_button"),
                                  dcc.Markdown(id="success_value_saved")])

    # create tab to retrieve the value entered in the other tab
    second_tab = dcc.Tab(label="Retrieve the value",
                         children=[html.Button(children="Show me the value", id="show_value_button"),
                                   dcc.Markdown(id="show_value_div")])

    # assemble tabs in dcc.Tabs object
    tabs = dcc.Tabs(children=[first_tab, second_tab])

    # create layout
    layout = html.Div(children=[tabs, store_session_id_div])

    return layout


# putting your callbacks in functions is a nice trick to be able to move them in other modules and import them
def create_callback_save_value(app: dash.Dash,
                               dash_db: DashDatabase):
    @app.callback(Output('success_value_saved', 'children'),
                  [Input('ok_button', 'n_clicks')],  # the button triggers the callback
                  [State('input_div', 'value'),  # additional info that does not trigger the callback
                   State('session_id_div_id', 'data')])  # used to identify the user and save its data
    def save_value(n_clicks, value, session_id):
        # when the app starts all callbacks are triggered by default.
        # raise a PreventUpdate to avoid the callback trigger at start (n_clicks is None at this point)
        if n_clicks is None:
            raise PreventUpdate

        # save value
        dash_db.store_user_value(user_id=session_id,
                                 key_name='value',
                                 value=value)

        # return success message
        return "Your value was sucessfully saved. Try to retrieve it in the other tab now :)!"
def create_callback_retrieve_value(app: dash.Dash,
                                   dash_db: DashDatabase):
    @app.callback(Output('show_value_div', 'children'),
                  [Input('show_value_button', 'n_clicks')],
                  [State('session_id_div_id', 'data')])
    def retrieve_value(n_clicks, session_id):
        # when the app starts all callbacks are triggered by default.
        # raise a PreventUpdate to avoid the callback trigger at start (n_clicks is 0 at this point)
        if n_clicks is None:
            raise PreventUpdate

        # save value
        value = dash_db.get_user_value(user_id=session_id,
                                       key_name='value')

        # return success message
        return f"Your value is {value}"




app = flask.Flask(__name__)
dash_app = dash.Dash(__name__,server=app,url_base_pathname="/",external_stylesheets=external_stylesheets)
dash_app.layout = serve_layout
dash_db = DashDatabase()  # create a DashDatabase instance for managing user values
create_callback_save_value(dash_app, dash_db)
create_callback_retrieve_value(dash_app, dash_db)
app.config['suppress_callback_exceptions'] = True

# # create the app, add the layout and the callbacks
# app = dash.Dash()
# app.layout = serve_layout
# dash_db = DashDatabase()  # create a DashDatabase instance for managing user values
# create_callback_save_value(app, dash_db)
# create_callback_retrieve_value(app, dash_db)

if __name__ == "__main__":
    # app.run_server(debug=True)
    app.run(debug=True, port=80, host='127.0.0.1')
