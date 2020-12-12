import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import stepper

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H6("Run Stepper!"),
    html.Div(["Step Delay Time (s): ",
              dcc.Input(id='step-delay', value='0', type='number', placeholder='ex 0.001'),
              html.Button("start/stop", id='btn-start-stop', n_clicks=0)]),
    html.Br(),
    html.Div(id='my-output'),

])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    [Input(component_id='btn-start-stop', component_property='n_clicks')],
    State(component_id='step-delay', component_property='value')
)
def update_output_div(n_clicks, step_delay):
    msg = ""

    if step_delay == 0:
        return

    if (float(step_delay)) < 0.0001:
        return "Cannot have delay below 0.0001"

    motor = stepper.Motor()
    motor.run_stepper(float(step_delay))

    if msg == "": msg = "run complete"
    return f'Output: {msg}'




if __name__ == '__main__':
    app.run_server(debug=True)