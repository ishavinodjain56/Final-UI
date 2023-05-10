from flask import *
from flask_mysqldb import MySQL
from datetime import datetime
from bs4 import BeautifulSoup as bs
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import pytz
import json
import os
import base64

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
    if "curr_user" in session:
        eprofile = session['curr_user']
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM events where email='"+eprofile+"' LIMIT 3 ")
    eventdetails = cur.fetchall()

    cur.execute("SELECT FN,LN from profile_info where email='"+eprofile+"'")
    namedetails=cur.fetchall()
    print(namedetails)

    cur.execute("SELECT ID, Plan, StartDate, Amount from subscription where email='"+eprofile+"' LIMIT 3")
    plandetails=cur.fetchall()
    print(plandetails)

    cur.execute("SELECT * FROM chart LIMIT 5")
    webdetails=cur.fetchall()
    print(webdetails)

    # cur.execute("SELECT * FROM busydays LIMIT 5")
    # busydays=cur.fetchall()
    # print(busydays)

    cur.execute("SELECT date, SUM(time) AS totaltime FROM timeline GROUP BY date ORDER BY totaltime DESC LIMIT 5")
    timeline=cur.fetchall()
    print("da",timeline)

    cur.execute("SELECT COUNT(domain), SUM(time) FROM timeline")
    timeline2=cur.fetchall()
    print("ta",timeline2)

    top_intrest = cur.execute("SELECT category FROM genre_data ORDER BY count DESC LIMIT 1 ")
    top_intrest = cur.fetchall()
    cur.close()

    return render_template('index.html',eventdetails=eventdetails,namedetails=namedetails,plandetails=plandetails,webdetails=webdetails,timeline=timeline,timeline2=timeline2,top_intrest=top_intrest)
  

@app.route('/bar_data')
def bar_data():
    cur = mysql.connection.cursor()
    output = cur.execute("select Topic_5,Count_5 from lda_output")
    data = cur.fetchall()
    data_bar = [{'y':row[0],'a' : row[1]} for row in data]
    print(data_bar)
    return jsonify(data_bar)

@app.route('/barg_data')
def barg_data():
    cur = mysql.connection.cursor()
    output1 = cur.execute("select category,count from genre_data")
    datag = cur.fetchall()
    data_barg = [{'y':row[0],'a' : row[1]} for row in datag]
    print(data_barg)
    return jsonify(data_barg)

@app.route('/browsing_sites', methods=['GET', 'POST'])
def browsingSitesPage():
    from_date = request.form.get('from_date')
    to_date = request.form.get('to_date')
    search_term = request.form.get('search')

    cur = mysql.connection.cursor()

    if not from_date or not to_date:
        cur.execute("SELECT URL, Title FROM browsing_sites")
    else:
        from_date = datetime.strptime(from_date, '%d/%m/%Y')
        to_date = datetime.strptime(to_date, '%d/%m/%Y')
        cur.execute("SELECT URL, Title FROM browsing_sites WHERE Timestamp BETWEEN %s AND %s", (from_date, to_date))

    browsing_info = cur.fetchall()
    
    # Apply search filter
    if search_term:
        browsing_info = [row for row in browsing_info if search_term in row[0] or search_term in row[1]]

    cur.close()
    return render_template('clients.html', browsing_info=browsing_info)

@app.route('/intrests')
def intrestPage():
    cur = mysql.connection.cursor()
    interests_data = cur.execute("SELECT id, Topic_5,Count_5 FROM lda_output")
    interests_info1 = cur.fetchall()

    interests_data = cur.execute("SELECT id, Topic_4,Count_4 FROM lda_output")
    interests_info2 = cur.fetchall()

    interests_data = cur.execute("SELECT id, Topic_2,Count_2 FROM lda_output")
    interests_info3 = cur.fetchall()

    interests_data = cur.execute("SELECT id, Topic_2,Count_2 FROM lda_output")
    interests_info4 = cur.fetchall()

    interests_data = cur.execute("SELECT id, Topic_6,Count_6 FROM lda_output")
    interests_info5 = cur.fetchall()

    interests_data = cur.execute("SELECT id, Topic_8,Count_8 FROM lda_output")
    interests_info6 = cur.fetchall()

    interests_data = cur.execute("SELECT id, Topic_3,Count_3 FROM lda_output")
    interests_info7 = cur.fetchall()

    interests_data = cur.execute("SELECT id, Topic_7,Count_7 FROM lda_output")
    interests_info8 = cur.fetchall()

    interests_data = cur.execute("SELECT id, Topic_10,Count_10 FROM lda_output")
    interests_info9 = cur.fetchall()

    interests_data = cur.execute("SELECT id, Topic_1,Count_1 FROM lda_output")
    interests_info10 = cur.fetchall()

    cur.close()
    return render_template('intrests.html', interests_info1 = interests_info1 ,
                            interests_info2 = interests_info2 ,
                            interests_info3 = interests_info3 ,
                            interests_info4 = interests_info4 ,
                            interests_info5 = interests_info5 ,
                            interests_info6 = interests_info6 ,
                            interests_info7 = interests_info7 ,
                            interests_info8 = interests_info8 ,
                            interests_info9 = interests_info9 ,
                            interests_info10 = interests_info10) 

@app.route('/top_genres')
def GenresPage():
    cur = mysql.connection.cursor()
    genres_info = cur.execute("SELECT category,cat_desc,count FROM genre_data")
    genres_info = cur.fetchall()
    cur.close()
    return render_template('projects.html',genres_info = genres_info)

@app.route('/subscription',methods=['GET','POST'])
def subscriptionPage():
    if "curr_user" in session:
        eprofile = session['curr_user']
        # cur.execute("SELECT * FROM subscription WHERE DATE(datetime) BETWEEN %s AND %s", (fromm, to))
    from_date = ''
    to_date = ''
    status=''
    if request.method == 'POST':
        from_date = request.form['fromm']
        to_date = request.form['to']
        status = request.form['status']
    cur = mysql.connection.cursor()
    print("hello fdate",from_date)
    
    if (from_date == '' or to_date == ''):
        if (status!=''):
            cur.execute("SELECT * FROM subscription WHERE email='"+eprofile+"' AND status='"+status+"' ")
        else:
            cur.execute("SELECT * FROM subscription WHERE email='"+eprofile+"' ")
    else:
        if (status!=''):
            cur.execute("SELECT * FROM subscription WHERE email='"+eprofile+"' AND status='"+status+"' ")
        else:
            fromm = datetime.strptime(from_date,'%d/%m/%Y')
            to = datetime.strptime(to_date,'%d/%m/%Y')
            print("Hello in")
            cur.execute("SELECT * FROM subscription WHERE email='"+eprofile+"' AND DATE(StartDate) BETWEEN %s AND %s", (fromm, to))
        
    subdetails = cur.fetchall()
    cur.close()
    return render_template('invoices.html',subdetails=subdetails)


@app.route('/addsubscription',methods=['GET','POST'])
def addsubscription():
    if "curr_user" in session:
        eprofile = session['curr_user']
    if request.method == 'POST':
        planname = request.form['plan']
        planamount = request.form['amount']

        cur = mysql.connection.cursor()
        if planamount == '$19.99 3-month':
            cur.execute("ALTER TABLE subscription AUTO_INCREMENT=1")
            cur.execute("INSERT INTO subscription VALUES (NULL,%s,%s,NOW(),DATE_ADD(NOW(), INTERVAL 3 MONTH),%s,%s)", (eprofile,planname,planamount,'Paid'))
        else:
            cur.execute("ALTER TABLE subscription AUTO_INCREMENT=1")
            cur.execute("INSERT INTO subscription VALUES (NULL,%s,%s,NOW(),DATE_ADD(NOW(), INTERVAL 1 MONTH),%s,%s)", (eprofile,planname,planamount,'Paid'))

        mysql.connection.commit()

        cur.close()
    return redirect('/subscription')

@app.route('/screen_time', methods=['GET', 'POST'])
def screentimePage():
    from_date = ''
    if request.method == 'POST':
        from_date = request.form['fromm']
    
    cur = mysql.connection.cursor()
    if from_date != '':
        from_date = from_date.replace("/", "-")
        print(from_date)
        cur.execute("Select * from timeline where date='"+from_date+"'")
    else:
        cur.execute("Select * from timeline")
    timedetail = cur.fetchall()
    print(timedetail)
    cur.close
    return render_template('worksheet.html',timedetail=timedetail)


@app.route('/tickets', methods=['GET', 'POST'])
def complaintPage():
    from_date = ''
    to_date = ''
    if request.method == 'POST':
        from_date = request.form['fromm']
        to_date = request.form['to']
    cur = mysql.connection.cursor()
    print("hello",from_date)
    if (from_date == '' or to_date == ''):
        cur.execute("SELECT * FROM tickets")
    else:
        fromm = datetime.strptime(from_date,'%d/%m/%Y')
        to = datetime.strptime(to_date,'%d/%m/%Y')
        cur.execute("SELECT * FROM tickets WHERE DATE(datetime) BETWEEN %s AND %s", (fromm, to))
    ticketdetails = cur.fetchall()
    cur.close()
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
    if "curr_user" in session:
        eprofile = session['curr_user']
        cur = mysql.connection.cursor()
        getprofile = cur.execute("SELECT * FROM events where email='"+eprofile+"' ")
        if getprofile>0:
            profiledetails = cur.fetchall()
            print("pd",profiledetails)
            event_list=[]
            for event in profiledetails:
                event_dict = {'id': event[0], 'ename': event[2], 'date': event[3].strftime('%Y-%m-%d')}
                event_list.append(event_dict)
                print("list",event_list)
            return render_template('events.html', event_list = event_list)
        else:
            return render_template('events.html')

    return ''
    

@app.route('/createevent',methods=['GET','POST'])
def createevent():
    if request.method == 'POST':
        if "curr_user" in session:
            eprofile = session['curr_user']
        evename = request.form['ename']
        evedate = request.form['edate']
        evedate = datetime.strptime(evedate,'%d/%m/%Y')
        print(evedate)
        # file = request.form['files']
        
        cur = mysql.connection.cursor()
        cur.execute("ALTER TABLE tickets AUTO_INCREMENT=1")
        cur.execute("INSERT INTO events VALUES (NULL,%s,%s,%s)", (eprofile,evename,evedate))

        mysql.connection.commit()

        cur.close()
    return redirect('/events')

@app.route('/ajax_delete', methods=['POST'])
def ajax_delete():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        print("form",request.form)
        getid = request.form['id']
        print(getid)
        cur.execute('DELETE FROM events WHERE ID = {0}'.format(getid))
        mysql.connection.commit()       
        cur.close()
        msg = 'Record deleted successfully'  
    return jsonify(msg)

@app.route('/chat')
def chatbotPage():
    return render_template('chat.html')

@app.route('/notifications')
def notificationsPage():
    return render_template('activities.html')

@app.route('/profile')
def profilePage():
    if "curr_user" in session:
        eprofile = session['curr_user']
        print(eprofile)
        cur = mysql.connection.cursor()
        getprofile = cur.execute("SELECT * FROM profile_info where email='"+eprofile+"' ")
        if getprofile>0:
            profiledetails = cur.fetchall()
            print("hello",profiledetails[0][1])
            encoded_image = base64.b64encode(profiledetails[0][1]).decode('utf-8')
            # print(encoded_image)
            return render_template('profile.html',profiledetails=profiledetails,encoded_image=encoded_image)
    
    return redirect('/editprofile')

@app.route('/editprofile')
def editprofilePage():
    eprofile = session['curr_user']
    cur = mysql.connection.cursor()
    count = cur.execute("SELECT * FROM profile_info where email='"+eprofile+"' ")
    if count != 0:
        profiledetails = cur.fetchall()
        encoded_image = base64.b64encode(profiledetails[0][1]).decode('utf-8')
        return render_template('edit-profile.html',profiledetails=profiledetails,eprofile=eprofile,encoded_image=encoded_image)
    else:
        return render_template('edit-profile.html',profiledetails='N',eprofile=eprofile)
    

@app.route('/addprofileinfo',methods=['GET','POST'])
def addprofile():
    if request.method == 'POST':
        pimg = request.files['img']
        pimg = pimg.read()
        firstname = request.form['FN']
        lastname = request.form['LN']
        bd = request.form['BD']
        birthdate = datetime.strptime(bd,'%d/%m/%Y')

        gender = request.form['gender']
        address = request.form['address']
        country = request.form['country']
        state = request.form['state']
        pin = request.form['pin']
        mobile = request.form['mobile']
        email = request.form['email']
        institution = request.form['institution']
        degree = request.form['degree']
        sd = request.form['SD']
        startingdate = datetime.strptime(sd,'%d/%m/%Y')
        cd = request.form['CD']
        endingdate = datetime.strptime(cd, '%d/%m/%Y')
        grade = request.form['grade']
        skills= request.form['skills']
        achievements = request.form['achievements']
        # file = request.form['files']
        
        cur = mysql.connection.cursor()

        count = cur.execute("SELECT email FROM profile_info where email='"+email+"' ")
        if count != 0:
            cur.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'profile_info' ")
            column_names = cur.fetchall()
            # Extract the column names from the list of tuples and store them in a separate list
            column_list = [x[0] for x in column_names]
            print("hello",column_list)
            new_values = ['NULL',pimg,firstname,lastname,birthdate,gender,address,country,state,pin,mobile,email,institution,degree,startingdate,endingdate,grade,skills,achievements]

            # Build the SET clause dynamically
            set_clause = ', '.join([f'{col} = %s' for col in column_list])

            # Build the SQL statement dynamically
            sql = f"UPDATE {'profile_info'} SET {set_clause} WHERE email = %s"

            # Define the ID of the row you want to update
            oemail = email

            # Execute the SQL statement with the new values and row ID
            cur.execute(sql, new_values + [oemail])
        else:
            # cur.execute("ALTER TABLE tickets AUTO_INCREMENT=1")
            cur.execute("INSERT INTO profile_info VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (pimg,firstname,lastname,birthdate,gender,address,country,state,pin,mobile,email,institution,degree,startingdate,endingdate,grade,skills,achievements))

        mysql.connection.commit()

        cur.close()
    return redirect('/profile')

@app.route('/loginsuccess',methods=['GET','POST'])
def loginsuccess():
    if request.method == 'POST':
        eid = json.loads(request.data)
        print(eid['user_email'])
        session["curr_user"] = eid['user_email']
        return redirect('/dashboard')
    
    return ""

@app.route('/donut_data')
def chart_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM chart LIMIT 5")
    data = cur.fetchall()
    data_dict = [{'label': row[2]+'.com', 'value': row[5]} for row in data]
    print(data_dict)
    return jsonify(data_dict)


@app.route('/bar_chart2')
def area_chart():
    cur = mysql.connection.cursor()
    cur.execute("SELECT date, SUM(time) AS totaltime FROM timeline GROUP BY date LIMIT 7")
    data = cur.fetchall()
    data_dict = [{'y': row[0], 'a': int(row[1]/60)} for row in data]
    print(data_dict)
    return jsonify(data_dict)
# bot = ChatBot('Bot')

# # Train the bot using the English corpus
# trainer = ChatterBotCorpusTrainer(bot)
# trainer.train("chatterbot.corpus.english")

# # Define a route for the API endpoint
# @app.route('/api/chatbot', methods=['POST'])
# def chatbot():
#     # Get the user's message from the POST request

#     user_message = request.json['message']
#     print("um",user_message)

#     # Get a response from the chat bot
#     bot_response = bot.get_response(user_message)
#     print("br",bot_response)

#     # Return the response as a JSON object

#     return jsonify({'message': str(bot_response)})

@app.template_filter('strftime')
def _jinja2_filter_datetime(date, fmt=None):
    if isinstance(date, str):
        date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    native = date.replace(tzinfo=None)
    format = fmt or '%b %d, %Y'
    return native.strftime(format)

@app.template_filter('strptime')
def _jinja2_filter_datetime(date, fmt):
    if isinstance(date, str):
        date = datetime.strptime(date, '%d/%m/%Y')
    # native = date.replace(tzinfo=None)
    format = fmt or '%b %d, %Y'
    return date.strftime(format)


if __name__ == '__main__':
    app.run(debug=True)