from flask import Flask,request, render_template , session,jsonify,redirect,url_for
from DBHandler import DBHandler
import re

app = Flask(__name__)
app.secret_key='s@#*je09el%^&'

@app.route('/')
@app.route('/login',methods=['POST', 'GET'])
def login():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    else:
        return render_template('index.html')
@app.route('/logout')
def logout():
    session.pop("username", None)
    session.pop('email',None)
    return redirect(url_for('login'))
@app.route('/register',methods=['POST', 'GET'])
def register():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    else:
        obj = DBHandler('localhost', 'root', 's@ajeel', 'testdb')
        return render_template('signup.html',invalid="")
@app.route('/signup',methods=['POST', 'GET'])
def signup():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    elif request.method!='POST':
        return redirect(url_for('register'))
    else:
        response = request.get_json(silent=True)
        message=''
        regex='[a-zA-Z0-9\._]+[@]+[a-zA-Z0-9]+[.]{1}[a-zA-Z]+'
        reg='^\S*$'

        if re.search(regex, response['email']):
            obj = DBHandler("localhost", "root", "s@ajeel", "testdb")
            if obj.isEmailExist(response['email']):
                message = 'That Email already exists.'
            elif re.search(reg, response['username'])==None:
                message = 'Invalid Username. Spacing not Allowed'
            elif obj.isUserExist(response['username'].lower()):
                message='That username is taken. Try Another.'
            else:
                if obj.signUp(response['fullname'],response['email'],response['username'].lower(),response['password']):
                    message='VALID'
                    session["username"] = response['username'].lower()
                    session["email"]=response['email']
        else:
            message='Invalid Email'
        return message
@app.route('/loggingin',methods=['POST', 'GET'])
def loggingin():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    elif request.method!='POST':
        return redirect(url_for('login'))
    else:
        response = request.get_json(silent=True)
        message =''
        obj = DBHandler('localhost', 'root', 's@ajeel', 'testdb')
        if obj.login(response['username'].lower(),response['password']):
            session["username"] = response['username'].lower()
            session["email"] = obj.getEmail(response['username'].lower())
            message='VALID'
        else:
            message='Invalid Username/Password'
        return message
@app.route('/dashboard' ,methods=['GET', 'POST'])
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', msg=session['username']+' '+session['email']+"\nsuccessfully logged in")
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()
