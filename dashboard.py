import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load the cleaned data
cleaned_data = pd.read_csv('data/cleaned_data.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div(children=[
    html.H1(children='NHANES Data Dashboard'),

    dcc.Graph(
        id='age-distribution',
        figure=px.histogram(cleaned_data, x='RIDAGEYR', nbins=30, title='Age Distribution')
    ),

    dcc.Graph(
        id='bmi-vs-age',
        figure=px.scatter(cleaned_data, x='RIDAGEYR', y='BMXBMI', title='BMI vs. Age')
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
