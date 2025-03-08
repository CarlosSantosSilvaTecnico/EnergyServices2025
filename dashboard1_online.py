import dash
from dash import html
from dash import dcc

#Define CSS style
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server=app.server

app.layout = html.Div([
    html.H1('IST Energy Monitor - Dashboard 1'),

    html.Div('        Visualization of total electricity consumption at IST over the last years'),

    dcc.Graph(
        id='yearly-data',
        figure={
            'data': [
                {'x': [2017, 2018, 2019], 'y': [9709, 10000, 10110], 'type': 'bar', 'name': 'Total'},
                {'x': [2017, 2018, 2019], 'y': [1440, 1605, 1000], 'type': 'bar', 'name': 'Civil'},
                {'x': [2017, 2018, 2019], 'y': [1658, 1598, 500], 'type': 'bar', 'name': 'Central'},
                {'x': [2017, 2018, 2019], 'y': [898, 1002, 400], 'type': 'bar', 'name': 'North Tower'},
                {'x': [2017, 2018, 2019], 'y': [1555, 1523, 300], 'type': 'bar', 'name': 'South Tower'},
            ],
            'layout': {
                'title': 'IST yearly electricity consumption (kWh)'
            }
        }
    ),

])

if __name__ == '__main__':
    app.run_server()
