import time
from flask import render_template, flash, redirect, url_for, request

from time import sleep                                                                                                                                                                         
import multiprocessing
from app import app, socketio
from app.forms import IDForm, Tasker, exitApp

from app import oHAB
import simplejson as json

th = False


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
    global t
    global th
    if (th==True):
        print(t.is_alive())
        t.terminate()
        t.join()
        print(t.is_alive())
        th = False
        th = 0

    form = Tasker()
    if form.validate_on_submit():
        if form.submit1.data:
            return render_template('TaskA.html', title='Task A', currStep="do something")
            
        elif form.submit2.data:
            return redirect(url_for('TaskB'))
    return render_template('taskselect.html', title='Tasks', form=form)


@app.route('/TaskB', methods=['GET','POST'])
def TaskB():
    global th 
    th = 1
    form = exitApp()
    return render_template('TaskB.html', title='Task B', form=form)


 
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
    

@socketio.on('rundummy2')
def rund2(rundummy2):
    sleep(1)
    print('rundummy2')
    global t
    t = multiprocessing.Process(target=oHAB.dummy2)
    t.start()
    global th
    th=True
    
   

