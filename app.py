from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "SUBDOMAIN TAKEOVER BY https://hackerone.com/theweekndxoxo?type=user"
