import time
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import IDForm
import simplejson as json


@app.route('/loader')
def loader():
    return render_template('loader.html', title='Loading')
    
@app.route('/',  methods=['GET', 'POST'])
@app.route('/index',  methods=['GET', 'POST'])
def index():
    form = IDForm()
    if form.validate_on_submit():
        flash('Participant ID entered: {}'.format(form.ID.data))
        with open('file.json', 'w') as f:
            json.dump(form.ID.data, f)
        return redirect(url_for('loader'))
    return render_template('index.html', title='Home', form=form)


