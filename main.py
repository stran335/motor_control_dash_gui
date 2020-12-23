import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import stepper

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H6("Run Stepper!"),
    html.Div(["Step Delay Time (ms): ",
        dcc.Input(id='step-delay', 
            value='0', 
            type='number', 
            step='0.1',
            placeholder='ex 0.001'),
        html.Br(),
        "Rotation Direction: ",
        dcc.Dropdown(
            id='rotate-direction',
            options=[
                {'label': 'clockwise', 'value': 'cw'},
                {'label': 'counter-clockwise', 'value': 'ccw'}
                ],
            value='cw'
            ),
        html.Br(),
        html.Button("start/stop", id='btn-start-stop', n_clicks=0)]),
    html.Br(),
    html.Div(id='my-output'),

])

motor = stepper.Motor()

@app.callback(
    Output(component_id='my-output', component_property='children'),
    [Input(component_id='btn-start-stop', component_property='n_clicks'),
    State(component_id='step-delay', component_property='value'),
    State(component_id='rotate-direction', component_property='value')]
)
def motor_start_stop(n_clicks, step_delay, rotate_direction):
    msg = ""

    if motor.running == True:
        motor.stop_command = True
        return "Motor Stopped"

    if step_delay == 0:
        return

    # print('step_delay: ' + str(step_delay))
    # if (float(step_delay)) < 0.0001:
    #     return "Cannot have delay below 0.0001"

    if rotate_direction == "cw":
        clockwise = True
    else:
        clockwise = False

    motor.run_stepper(float(step_delay), clockwise)

    if msg == "": msg = "run complete"
    return f'Output: {msg}'




if __name__ == '__main__':
    app.run_server(debug=True)