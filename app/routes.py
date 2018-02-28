import time
from flask import render_template, flash, redirect, url_for, request

from time import sleep                                                                                                                                                                         

from app import app, socketio
from app.forms import IDForm, Tasker

import simplejson as json


#turn the flask app into a socketio app


@app.route('/',  methods=['GET', 'POST'])
@app.route('/index',  methods=['GET', 'POST'])
def index():
    form = IDForm()
    if form.validate_on_submit():
        flash('Participant ID entered: {}'.format(form.ID.data))
        with open('file.json', 'w') as f:
            json.dump(form.ID.data, f)
        return redirect(url_for('taskselect'))
    return render_template('index.html', title='Home', form=form)



@app.route('/taskselect', methods=['GET', 'POST'])
def taskselect():
    form = Tasker()
    if form.validate_on_submit():
        if form.submit1.data:
            return render_template('TaskA.html', title='Task A', currStep="do something")
            
        elif form.submit2.data:
            return "Done B"
    return render_template('taskselect.html', title='Tasks', form=form)
 


@app.route('/TaskA')
def TaskA():
    return render_template('TaskA.html', title='Task A')

@socketio.on('messagecs')
def currStepMes(messagecs):
    socketio.emit('messagecs', messagecs)

@socketio.on('messageps')
def prevStepMes(messageps):
    socketio.emit('messageps', messageps)