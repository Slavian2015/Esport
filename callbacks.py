from dash.dependencies import Input, Output, State, ALL
from app import dash_app
import dash
import PARSER
import Structure
from layouts import all_matches, layout_main, match_card
# from dash.exceptions import PreventUpdate
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
                print(i)
                return match_card(i)
        if pathname == '/match_card':
            return layout_main
        elif pathname == '/all_matches':
            return all_matches
        elif pathname == '/':
            return layout_main
        else:
            return '404'

def refresh(app: dash.Dash):

    ###############################    RESTART ALL FUNCTIONS     ########################################
    @app.callback(Output('table-container', 'children'), [Input('interval', 'n_intervals')])
    def trigger_by_modify(n):

        PARSER.new_refresh()
        Structure.refresh_BD()

        print("###############  UPDATE   #########################")
        return

cardwindow(dash_app)
refresh(dash_app)