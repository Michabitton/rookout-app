import os
from flask import Flask, render_template, flash, redirect, url_for, Markup
import rook

app = Flask(__name__)

user = {
    'username': 'Micha Bitton',
    'bio': 'Surfing Spots',
}

surfing_spots = [
    {'name': 'Carinaros', 'location': 'Panama'},
    {'name': 'Banana Beach', 'location': 'Santa Teresa'},
    {'name': 'Elepenth', 'location': 'Sri Lanka'},
    {'name': 'Cocs', 'location': 'Maldives'},
    {'name': 'Punta Roca', 'location': 'El-Salvador'},
    {'name': 'WeachBeach', 'location': 'Secret in Panama'},
    {'name': 'Jaco Beach', 'location': 'Jaco'},
]


@app.route('/surfing_spots')
def surfingSpots():
    rook.flask.breakpoint(surfing_spots=surfing_spots)
    return render_template('surfing_spots.html', user=user, surfing_spots=surfing_spots)


@app.route('/')
def index():
    return render_template('index.html')

# 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


# 500 error handler
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500

if __name__ == '__main__':
    rook.start(token=os.environ["ROOKOUT_TOKEN"], labels={"env":"dev", "function": "candidate-test", "git_commit": os.environ["ROOKOUT_COMMIT"]})
    app.run(host="0.0.0.0", port=8000, threaded=True)