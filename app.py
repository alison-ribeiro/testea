import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Gapminder Data'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df[df['year']==year]['gdpPercap'], 'y': df[df['year']==year]['lifeExp'], 'type': 'scatter', 'text': df[df['year']==year]['country'], 'mode': 'markers'},
            ],
            'layout': {
                'title': 'Gapminder Visualization',
                'xaxis': {'title': 'GDP per capita'},
                'yaxis': {'title': 'Life Expectancy'},
                'hovermode': 'closest'
            }
        }
    ),

    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    )
])

@app.callback(
    dash.dependencies.Output('example-graph', 'figure'),
    [dash.dependencies.Input('year-slider', 'value')])
def update_figure(selected_year):
    filtered_df = df[df['year'] == selected_year]
    fig = {
        'data': [
            {'x': filtered_df['gdpPercap'], 'y': filtered_df['lifeExp'], 'type': 'scatter', 'text': filtered_df['country'], 'mode': 'markers'}
        ],
        'layout': {
            'title': 'Gapminder Visualization',
            'xaxis': {'title': 'GDP per capita'},
