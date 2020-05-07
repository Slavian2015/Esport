from app import dash_app, app
import dash_core_components as dcc
import dash_html_components as html
import dash_design_kit as ddk

# import PARSER
import callbacks

# git push heroku master
# https://dash-gallery.plotly.host/Docs/packages/dash-design-kit/dash_design_kit-1.4.0.tar.gz
# --extra-index-url=https://dash-gallery.plotly.host/Docs/packages
# dash-design-kit==1.4.0

dash_app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    ddk.App(style={'background-color': 'transparent'},
                     children=[
                         ddk.Header(style={'height': '7vh', 'background-color': '#163d47', 'opacity': '1', 'margin':'0'},
                                    children=[
                                        ddk.Logo(src='../assets/logo.gif'),
                                        ddk.Block(style={'text-align': 'right'}, children=[
                                            dcc.Link('Главная', style={'color': 'azure', 'margin': '10px'}, href='/'),
                                            # dcc.Link('Карточка Матча', style={'color': '#fff', 'margin': '10px'}, href='/match_card'),
                                            # dcc.Link('МАТЧИ', style={'color': '#fff', 'margin': '10px'}, href='/all_matches')
                                        ])]),






    html.Div(id='page-content'),
    html.Div(id='table-container'),


])])



if __name__ == "__main__":
    # app.run_server(debug=True)
    app.run(debug=False)