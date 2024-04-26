#Create a feedback form for passenger about train journey using the Dash framework. This should collect user feedback, suggestions, or bug reports and store them in a database.                        

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import sqlite3

# Create a connection to the database
conn = sqlite3.connect('feedback.db')
c = conn.cursor()

# Create a table to store the feedback
c.execute('''CREATE TABLE IF NOT EXISTS feedback
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              feedback_text TEXT,
              feedback_type TEXT)''')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the feedback form
app.layout = html.Div([
    html.H1('Passenger Feedback Form'),
    html.Label('Feedback Text'),
    dcc.Input(id='feedback-text', type='text'),
    html.Label('Feedback Type'),
    dcc.Dropdown(
        id='feedback-type',
        options=[
            {'label': 'Feedback', 'value': 'feedback'},
            {'label': 'Suggestion', 'value': 'suggestion'},
            {'label': 'Bug Report', 'value': 'bug_report'}
        ],
        value='feedback'
    ),
    html.Button('Submit', id='submit-button'),
    html.Div(id='output-message')
])

# Define the callback function to handle form submission
@app.callback(
    Output('output-message', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('feedback-text', 'value'),
     State('feedback-type', 'value')]
)
def submit_feedback(n_clicks, feedback_text, feedback_type):
    if n_clicks is not None:
        # Insert the feedback into the database
        c.execute("INSERT INTO feedback (feedback_text, feedback_type) VALUES (?, ?)",
                  (feedback_text, feedback_type))
        conn.commit()
        return 'Feedback submitted successfully!'

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)