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
    return render_template('surfing_spots.html', user=user, surfing_spots=surfing_spots)


@app.route('/')
def index():
    return render_template('index.html')


# register template context handler
@app.context_processor
def inject_info():
    foo = 'I am foo.'
    return dict(foo=foo)  # equal to: return {'foo': foo}


# register template global function
@app.template_global()
def bar():
    return 'I am bar.'


# register template filter
@app.template_filter()
def musical(s):
    return s + Markup(' &#9835;')


# register template test
@app.template_test()
def baz(n):
    if n == 'baz':
        return True
    return False


@app.route('/surfing_spots2')
def surfing_spots_with_static():
    return render_template('surfing_spots_with_static.html', user=user, surfing_spots=surfing_spots)


# message flashing
@app.route('/flash')
def just_flash():
    flash('I am flash, who is looking for me?')
    return redirect(url_for('index'))


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