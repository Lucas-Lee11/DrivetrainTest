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

app.secret_key = 'forgotten charger'

@app.route('/', methods=['GET', 'POST'])
def login():

    # Check for session existance
    if session.get('username') is not None:
        return redirect(url_for('response'))
    else:
        return render_template('login.html')

@app.route('/auth', methods=['GET', 'POST'])
def response():
    method = request.method

    # Make sure this is only accessed via a POST request
    if method == 'GET':
        # Need to check key before use in order to avoid crash
        if session.get('username') is not None:
            username = session['username']
            return render_template('response.html', username=username, successful=True, reason='n/a')
        else:
            return redirect(url_for('login'))
            
    if method == 'POST':

        username = request.form['username']
        password = request.form['password']


        if username != USERNAME:
            reason = 'Bad username'
            successful = False
        elif password != PASSWORD:
            reason = 'Bad password'
            successful = False
        else:
            # Store user info into a cookie
            session['username'] = username

            reason = 'n/a'
            successful = True

        return render_template('response.html', username=username, successful=successful, reason=reason)

@app.route('/logout', methods=['GET', 'POST'])
def logout():

    if session.get('username') is not None:
        session.pop('username')

    return redirect(url_for('login'))

if __name__ == '__main__':
    app.debug = True
    app.run()
