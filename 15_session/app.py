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

        # If already logged in, send them to the response page
        return redirect(url_for('response'))
    else:

        # If not logged in, show login page
        return render_template('login.html')

@app.route('/auth', methods=['GET', 'POST'])
def response():
    method = request.method

    if method == 'GET':

        # Need to check key before use in order to avoid crash
        if session.get('username') is not None:

            # If session is stored, automatically render page
            username = session['username']
            return render_template('response.html', username=username, successful=True, reason='n/a')
        else:
            # If session does not exist, send them back to login page
            return redirect(url_for('login'))

    if method == 'POST':

        # Get information from request.form since it is submitted via post
        username = request.form['username']
        password = request.form['password']


        # Check username and password and get the reason
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

    # Once again check for a key before popping it
    if session.get('username') is not None:
        session.pop('username')

    # After logout, return to login page
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.debug = True
    app.run()
