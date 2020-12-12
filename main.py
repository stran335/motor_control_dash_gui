import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import stepper

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H6("Run Stepper!"),
    html.Div(["Input: ",
              dcc.Input(id='my-input', value='', type='text'),
              html.Button("start/stop", id='btn-start-stop', n_clicks=0)]),
    html.Br(),
    html.Div(id='my-output'),

])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    [Input(component_id='btn-start-stop', component_property='n_clicks')],
    State(component_id='my-input', component_property='value')
)
def update_output_div(n_clicks, input_val):

    if input_val == "":
        return

    motor = stepper.Motor()
    motor.pulse_x_ccw()

    msg = "output msg here"
    return f'Output: {msg}'




if __name__ == '__main__':
    app.run_server(debug=True)