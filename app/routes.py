import time
from flask import render_template, flash, redirect, url_for, request

from time import sleep                                                                                                                                                                         
import _thread
from app import app, socketio
from app.forms import IDForm, Tasker

from app import oHAB
import simplejson as json


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
            return render_template('TaskB.html', title='Task A', currStep="do something")
    return render_template('taskselect.html', title='Tasks', form=form)
 
@socketio.on('messagecs')
def currStepMes(messagecs):
    socketio.emit('messagecs', messagecs)

@socketio.on('messageps')
def prevStepMes(messageps):
    socketio.emit('messageps', messageps)

@socketio.on('rundummy')
def rund(rundummy):
    sleep(1)
    print('rundummy')
    
    _thread.start_new_thread(oHAB.dummy, ())

@socketio.on('rundummy2')
def rund(rundummy2):
    sleep(1)
    print('rundummy2')
    
    _thread.start_new_thread(oHAB.dummy2, ())

