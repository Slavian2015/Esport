from dash.dependencies import Input, Output, State, ALL
from app import dash_app
import dash
from layouts import all_matches, layout_main, match_card
from dash.exceptions import PreventUpdate
dash_app.config['suppress_callback_exceptions'] = True


def cardwindow(app: dash.Dash):
    @app.callback(
        Output('page-content', 'children'),
        [Input('url', 'pathname')],
        [State({'type': 'dynamic-cards-item', 'index': ALL}, 'id'),
         State({'type': 'dynamic-cards-item', 'index': ALL}, 'href')])
    def display_output(pathname, href, id):

        for i in id:
            if pathname == "{}".format(i):
                return match_card(i)
        if pathname == '/match_card':
            return match_card("/370630")
        elif pathname == '/all_matches':
            return all_matches
        elif pathname == '/':
            return layout_main
        else:
            return '404'

cardwindow(dash_app)