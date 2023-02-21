from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

app = Dash(__name__)

df = pd.read_csv(r'C:\Users\lenovo\Downloads\sample.csv')

fig1 = px.bar(df, y=['Pre Tax Income', 'Income After Taxes', 'Income From Continuous Operations'], x='Dates',
              barmode='group')
fig2 = go.Figure(data=go.Scatter(
    x=df['Revenue'],
    y=df['Dates'],
    mode='markers',
    name='Random Walk in 1D',
    marker=dict(
        size=7,
        colorscale='Reds',
        showscale=True,
    )
))
fig3 = go.Figure(go.Indicator(
    mode="gauge+number",
    value=df['Gross profit'].sum(),
    domain={'x': [0, 1], 'y': [0, 1]},
    title={'text': "Gross Profit"}))
fig4 = go.Indicator(
    value=df['Net Income'].mean(),
    gauge={
        'shape': "bullet",
        'axis': {'visible': False}})

app.layout = html.Div([
    html.Div([
        html.Label('Column-Name: '),
        dcc.Dropdown(
            id='var-1',
            options=[{'label': i, 'value': i} for i in df.columns],
            value=df.columns[0]
        ),
        dcc.Dropdown(
            id='var-2',
            options=[{'label': i, 'value': i} for i in df.columns],
            value=df.columns[0]
        ),
        dcc.Dropdown(
            id='var-3',
            options=[{'label': i, 'value': i} for i in df.columns],
            value=df.columns[0]
        ),
        dcc.Graph(id='bar-plot', figure=fig1),
    ], style={'width': '100%', 'display': 'inline-block'}),
    html.Div([
        dcc.Graph(id='gauge-plot', figure=fig3),
        dcc.Graph(figure=fig2, id='bar-plot-2')
    ], style={'width': '50%', 'display': 'flex', 'flex-direction': 'row', 'align-self': 'center'}),
])


@app.callback(
    Output('bar-plot', 'figure'),
    Input('var-1', 'value'),
    Input('var-2', 'value'),
    Input('var-3', 'value')
)
def update_column_plot(var_1, var_2, var_3):
    fig = px.bar(df, y=[var_1, var_2, var_3], x='Dates', barmode='group')
    return fig


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

app.run_server(debug=True, use_reloader=True)
