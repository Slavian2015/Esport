from app import dash_app, dash_db
import dash
from dash.dependencies import Input, Output, State, ALL, MATCH
import dash_core_components as dcc
# import PARSER
# import Structure
from layouts import all_matches, layout_main
import dash_design_kit as ddk
import Main_page
import Match_sample
import layouts
dash_app.config['suppress_callback_exceptions'] = True
import Live_matches
# import Main_tours_page
import News_card
from dash_database import DashDatabase
from dash.exceptions import PreventUpdate
import Result_page

# putting your callbacks in functions is a nice trick to be able to move them in other modules and import them
def create_callback_save_value(app: dash.Dash, dash_db: DashDatabase):
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
def create_callback_retrieve_value(app: dash.Dash, dash_db: DashDatabase):
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

def cardwindow(app: dash.Dash):
    @app.callback(
        Output('page-content', 'children'),
        [Input('url', 'pathname')],
        # [State({'type': 'dynamic-cards-item', 'index': ALL}, 'id'),
        #  State({'type': 'news-card', 'index': ALL}, 'id'),
        #  State({'type': 'dynamic-cards-item', 'index': ALL}, 'href')]
    )
    def display_output(pathname):
        ctx = dash.callback_context
        # print(id)



        if pathname == '/match_card':
            return layouts.layout_main()
        elif pathname == '/all_matches':
            return all_matches
        elif pathname == '/':
            return layout_main
        else:
            if not ctx.triggered:
                return '404'
                # raise dash.exceptions.PreventUpdate
            else:
                button_id = ctx.triggered[0]['value']

                parametr = button_id.split("/")
                # print('ctx', ctx.triggered[0])
                # print('button_id', button_id)
                # print('split', button_id.split("/")[2])

                print('LENGTH  :',len(parametr))

                if len(parametr) > 2 :
                    if pathname == "/news/{}".format(button_id.split("/")[2]):
                        return News_card.news_page(button_id.split("/")[2])

                else:
                    if pathname == "{}".format(button_id):
                        return Match_sample.match_card(button_id)
def refresh(app: dash.Dash):

    ###############################    RESTART ALL FUNCTIONS     ########################################
    @app.callback([Output('main_matches', 'children'),
                  Output('main_results', 'children'),
                   # Output('main_matches_live', 'children')
                   ],
                  [Input('interval', 'n_intervals')])

                    # events = [Event('graph-update', 'interval')])
    def trigger_by_modify(n):
        # print("###############  UPDATE 1  #########################")
        # PARSER.new_refresh()
        # Structure.refresh_BD()
        # print("###############  UPDATE 2  #########################")
        print("###############  START UPDATE   #########################")

        result = [ddk.CardHeader(title='Матчи',
                                style={'background-color': '#1c424c',
                               'margin': '0px',
                               'padding': '15px',
                               'display':'block',
                               'font-size': '20px'}),
                 Main_page.main_page()]

        # live = [i for i in Live_matches.live()]

        results = [ddk.CardHeader(title='Результаты',
                           style={'background-color': '#1c424c',
                                  'margin': '0px',
                                  'padding': '15px',
                                  'display': 'block',
                                  'font-size': '20px'}),
            Result_page.result_page()]



        #
        # tour = [
        #      ddk.CardHeader(title='Турниры',
        #                     style={'background-color': '#1c424c',
        #                            'margin': '0px',
        #                            'padding': '15px',
        #                            'display':'block',
        #                            'font-size': '20px'}),
        #      Main_tours_page.tour_page()]

        print("###############  UPDATED   #########################")
        return result, results
# def ref_match(app: dash.Dash):
#     @app.callback(
#         [Output({'type': 'dynamic-cards-item', 'index': MATCH}, 'children')],
#         [Input({'type': 'interval_match', 'index': MATCH}, 'n_intervals')],
#         [dash.dependencies.State({'type': 'interval_match', 'index': MATCH}, 'id')],
#                   )
#     def display_output(n, id):
#
#         ctx = dash.callback_context
#
#         if not ctx.triggered:
#             raise dash.exceptions.PreventUpdate
#         else:
#             pass
#         # if n is None:
#         #     raise PreventUpdate
#         # else:
#         print("#########     MATCH     ######    MATCH   #################")
#         print("MATCH Interval  : ", id['index'])
#         div = Match_sample.match_card2(id['index'])
#         return div
def video_div(app: dash.Dash):
    @app.callback(Output({'type': 'video_div', 'index': ALL}, 'is_open'),
        [Input({'type': 'video_btn', 'index': ALL}, 'n_clicks')],
                  [State({'type': 'video_btn', 'index': ALL}, 'id')],
                  )
    def display_output(n, id):

        ctx = dash.callback_context

        if not ctx.triggered:
            raise dash.exceptions.PreventUpdate
        else:
            pass

        # ctx = dash.callback_context
        button_id = ctx.triggered[0]['value']
        print('button_id',button_id)

        if n == 0:
            raise PreventUpdate
        # else:
        #     return True
        elif n:
            print('VIDEO DIV ID', id)
            return [True]
        else:
            return [False]

cardwindow(dash_app)
refresh(dash_app)
create_callback_save_value(dash_app, dash_db)
create_callback_retrieve_value(dash_app, dash_db)
# ref_match(dash_app)
video_div(dash_app)