from flask import *

app = Flask(__name__)
app.secret_key = b'final-ui/admin_dashboard@secret007'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/activities')
def activitiesPage():
    return render_template('activities.html')

@app.route('/assets')
def assetsPage():
    return render_template('assets.html')

@app.route('/login')
def loginPage():
    return render_template('login_page.html')

if __name__ == '__main__':
    app.run(debug=True)