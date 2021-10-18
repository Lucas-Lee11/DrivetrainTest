'''
Forgotten Charger: Lewis Cass, Aryaman Goenka, Oscar Wang
Softdev
K15: Cookie and Sessions Introduction
2021-10-19
'''

from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

USERNAME = 'user'
PASSWORD = 'pass'

@app.route('/')
def login():

    return render_template('login.html')

@app.route('/auth')
def response(methods=['GET', 'POST']):
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args) #dictionary containing the queries as entries
    print("***DIAG: request.headers ***")
    print(request.headers)


    method = request.method

    # Make sure this is only accessed via a POST request
    if method == 'GET':
        return redirect(url_for('login'))
    if method == 'POST':

        username = request.form['username']
        password = request.form['password']


        if username != 'user':
            reason = 'Bad username'
            successful = False
        elif password != 'pass':
            reason = 'Bad password'
            successful = False
        else:
            # Store user info into a cookie
            session['username'] = username
            session['password'] = password

            reason = 'n/a'
            successful = True

        return render_template('response.html', username=username, method=request.method, successful=successful, reason=reason)

if __name__ == '__main__':
    app.debug = True
    app.run()