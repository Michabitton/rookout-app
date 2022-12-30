import rook
from flask import Flask
rook.start(token='YOUR_ROOKOUT_TOKEN')


app = Flask(__name__)

@app.route('/')
def home():
    rook.flask.breakpoint()
    return 'Hello, Candidate speaking'
