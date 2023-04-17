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

if __name__ == '__main__':
    port = 5000
    app.run(host='0.0.0.0', port=port, debug=True)