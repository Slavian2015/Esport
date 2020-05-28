import dash
import dash_bootstrap_components as dbc
from dash_database import DashDatabase
import flask

external_stylesheets = [dbc.themes.SOLAR]
app = flask.Flask(__name__)
dash_app = dash.Dash(__name__,
                     server=app,
                     url_base_pathname="/",
                     meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}],
                     external_stylesheets=external_stylesheets)
# dash_app.layout = serve_layout
dash_app.title = 'ELTV'
dash_db = DashDatabase()  # create a DashDatabase instance for managing user values
# create_callback_save_value(dash_app, dash_db)
# create_callback_retrieve_value(dash_app, dash_db)
