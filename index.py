from app import dash_app, app
from layouts import layout1, layout2, layout_main
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_design_kit as ddk
# git push heroku master

import callbacks


dash_app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    ddk.App(style={'background-color': 'transparent'},
                     children=[
                         ddk.Header(style={'height': '7vh', 'background-color': '#1f78b494', 'opacity': '0.8'},
                                    children=[
                                        ddk.Logo(src='../assets/logo.png'),
                                        ddk.Block(style={'text-align': 'right'}, children=[
                                            dcc.Link('HOME', style={'color': 'azure', 'margin': '10px'}, href='/'),
                                            dcc.Link('Карточка Матча', style={'color': '#fff', 'margin': '10px'}, href='/app1'),
                                            dcc.Link('Карточка Матча2', style={'color': '#fff', 'margin': '10px'}, href='/app1'),
                                            dcc.Link('Go to App 2', style={'color': '#fff', 'margin': '10px'}, href='/app2')])]),





    html.Div(id='page-content')
])])



@dash_app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/app1':
         return layout1
    elif pathname == '/app2':
         return layout2
    if pathname == '/':
         return layout_main
    else:
        return '404'

if __name__ == "__main__":
    # app.run_server(debug=True)
    app.run(debug=False)