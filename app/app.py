from datetime import datetime, timedelta
import pandas as pd

import pymongo

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(
    html.Div([
        html.H4('Brackleshame live wind data'),
        html.Div(id='live-update-text'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1 * 10000,  # in milliseconds
            n_intervals=0
        )
    ])
)


# Multiple components can update everytime interval gets fired.
@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    # gets all data
    with pymongo.MongoClient("mongodb://mongodb:27017") as client:
        mydb = client['wind_data_db']  # the database
        mycol = mydb["brackelsham"]
        df = pd.DataFrame(list(mycol.find()))

    df['timestamp'] = pd.to_datetime(df['timestamp'])

    last_24 = pd.to_datetime(datetime.today() - timedelta(days=1), utc=True)
    df = df[df['timestamp'] > last_24]

    fig = px.line(df, x='timestamp', y='wind_avg')  # col names are wrong

    return fig


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
