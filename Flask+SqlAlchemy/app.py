from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from base import *
from flask.helpers import url_for
import hashlib
import base64

app = Flask(__name__)
# create an engine
# engine = create_engine('postgresql://')
# engine = create_engine('db2+ibm_db://')

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('home.html', name = request.form['username'])

@app.route('/login', methods=['GET','POST'])
def do_admin_login():
    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # create a Session
    s = Session()
    if request.method == 'GET':
        return render_template('login.html')
 
    username = str(request.form['username'])
    inputpassword = base64.b64encode(hashlib.sha1(bytes(request.form['password'], 'utf-8')).digest())
    encodedpassword = "{SHA}" + str(inputpassword.decode())

    registered_user = s.query(UserMaster.PASSWORD).filter(UserMaster.login_id == username,UserMaster.PASSWORD == encodedpassword)
    
    if registered_user is None:
        flash('Username or Password is invalid' , 'error')   
        session['logged_in'] = False       
    else:
        session['logged_in'] = True
        return render_template('home.html', name = request.form['username'])

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='localhost', port=4000)