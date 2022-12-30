import rook
from flask import Flask


rook.start(token='6cc58c7efd501c59c6ca851aad023c9ca14ca303088b847fb64764e3495e9393', labels={"env":"dev", "team": "micha-bitton"})


app = Flask(__name__)

@app.route('/')
def home():
    rook.flask.breakpoint()
    return 'Hello, Candidate speaking'



