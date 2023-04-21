from flask import *
from flask_mysqldb import MySQL
from datetime import datetime
from bs4 import BeautifulSoup as bs
import json
import os

# from flask import Flask, redirect, request, url_for
# from flask_login import (
#     LoginManager,
#     current_user,
#     login_required,
#     login_user,
#     logout_user,
# )
# from oauthlib.oauth2 import WebApplicationClient
# import requests

# # Internal imports
# from db import init_db_command
# from user import User

app = Flask(__name__)
app.secret_key = b'final-ui/admin_dashboard@secret007'

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "fyp"

mysql = MySQL(app)


@app.route('/')
def homePage():
    return render_template('main_landingpage.html')

@app.route('/login')
def loginPage():
    return render_template('login_page.html')

@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

@app.route('/browsing_sites')
def browsingSitesPage():
    return render_template('clients.html')

@app.route('/top_genres')
def GenresPage():
    return render_template('projects.html')

@app.route('/subscription')
def subscriptionPage():
    # cur = mysql.connection.cursor()
    # getsubscription = cur.execute("SELECT * FROM subscription")

    # if getsubscription>0:
    #     subscriptiondetails = cur.fetchall()
    #     for row in subscriptiondetails:
    #         ed = cur.execute("SELECT DATE_ADD(2017-06-15', INTERVAL 10 DAY)")
    #         print(ed)

    return render_template('invoices.html')

@app.route('/addsubscription',methods=['GET','POST'])
def addsubscription():
    if request.method == 'POST':
        with open("templates/invoices.html") as file:
            html = file.read()
        soup = bs(html, "html.parser")
        plan = soup.find('div', id = "plan")
        plan = plan.string.strip()
        amount = soup.find('h5',id="amount").string

        cur = mysql.connection.cursor()
        cur.execute("ALTER TABLE subscription AUTO_INCREMENT=1")
        cur.execute("INSERT INTO subscription (Plan,Amount) VALUES (%s,%s)", (plan,amount))

        mysql.connection.commit()

        cur.close()
    return redirect('/subscription')

@app.route('/screen_time')
def screentimePage():
    return render_template('worksheet.html')

@app.route('/tickets')
def complaintPage():
    cur = mysql.connection.cursor()
    gettickets = cur.execute("SELECT * FROM tickets")

    if gettickets>0:
        ticketdetails = cur.fetchall()

    return render_template('tickets.html',ticketdetails=ticketdetails)

@app.route('/addticket',methods=['GET','POST'])
def addticket():
    if request.method == 'POST':
        subject = request.form['subject']
        description = request.form['description']
        # file = request.form['files']
        
        cur = mysql.connection.cursor()
        cur.execute("ALTER TABLE tickets AUTO_INCREMENT=1")
        cur.execute("INSERT INTO tickets (SUbject,Description) VALUES (%s,%s)", (subject,description))

        mysql.connection.commit()

        cur.close()
    return redirect('/tickets')


@app.route('/events')
def eventsPage():
    return render_template('events.html')

@app.route('/chat')
def chatbotPage():
    return render_template('chat.html')

@app.route('/notifications')
def notificationsPage():
    return render_template('activities.html')

@app.route('/profile')
def profilePage():
    return render_template('profile.html')

@app.route('/editprofile')
def editprofilePage():
    return render_template('edit-profile.html')

@app.template_filter('strftime')
def _jinja2_filter_datetime(date, fmt=None):
    if isinstance(date, str):
        date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    native = date.replace(tzinfo=None)
    format = fmt or '%b %d, %Y'
    return native.strftime(format)

if __name__ == '__main__':
    app.run(debug=True)