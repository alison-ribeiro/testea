import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

# Carrega os dados
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/iris.csv')

# Cria a aplicação
app = dash.Dash(__name__)

# Define o layout
app.layout = html.Div([
    html.H1('Exemplo de aplicação Dash'),
    html.Div([
        dcc.Graph(
            id='grafico-iris',
            figure=px.scatter(df, x='sepal_width', y='sepal_length', color='species')
        )
    ], style={'width': '50%', 'display': 'inline-block'}),
    html.Div([
        html.H3('Tabela de dados'),
        html.Table([
            html.Thead(
                html.Tr([html.Th(col) for col in df.columns])
            ),
            html.Tbody([
                html.Tr([
                    html.Td(df.iloc[i][col]) for col in df.columns
                ]) for i in range(min(len(df), 10))
            ])
        ])
    ], style={'width': '50%', 'display': 'inline-block', 'vertical-align': 'top'})
])

# Inicia o servidor
if __name__ == '__main__':
    app.run_server(debug=True)
