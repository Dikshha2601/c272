import os

from flask import Flask, request, jsonify, render_template, redirect, url_for,send_file
from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import SyncGrant
from werkzeug.utils import secure_filename

app = Flask(__name__)
fake = Faker()


@app.route('/')
def index():
    return render_template('index.html')

# Add your Twilio credentials
@app.route('/token')
def generate_token():
    TWILIO_ACCOUNT_SID = 'ACc1b772a131f155b295ee2ae043f5b147'
    TWILIO_SYNC_SERVICE_SID = 'ISc5f0f2f11c0b0dd4b56b6c93b8bef1ef'
    TWILIO_API_KEY = 'SK12fa933ac7b1e2e3cc38401d8de1025e'
    TWILIO_API_SECRET = 'PgMbXtSrdBBof4mFEk6vzGyVy749Qirf'

    username = request.args.get('username', fake.user_name())

    # create access token with credentials
    token = AccessToken(TWILIO_ACCOUNT_SID, TWILIO_API_KEY, TWILIO_API_SECRET, identity=username)
    # create a Sync grant and add to token
    sync_grant_access = SyncGrant(TWILIO_SYNC_SERVICE_SID)
    token.add_grant(sync_grant_access)
    return jsonify(identity=username, token=token.to_jwt().decode())

# Write the code here
@app.route('/', methods=['POST'])
def download_text():
    textfromnotepad=reuest.form['text']
    with open('workfile.txt', 'w') as f:
        f.write(textfromnotepad)

    path='workfile.txt'

    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run(host='localhost', port='5001', debug=True)
