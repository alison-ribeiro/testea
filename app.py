import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

df = px.data.iris()

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Iris Data'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df[df['species']==species]['sepal_width'], 'y': df[df['species']==species]['sepal_length'], 'type': 'scatter', 'mode': 'markers', 'name': species} for species in df['species'].unique()
            ],
            'layout': {
                'title': 'Iris Visualization',
                'xaxis': {'title': 'Sepal Width'},
                'yaxis': {'title': 'Sepal Length'},
                'hovermode': 'closest'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
