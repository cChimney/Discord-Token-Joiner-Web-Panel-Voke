from flask import Flask , render_template, request
from discord_defs import *
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import threading
app = Flask(__name__,template_folder='templates')

db = {"123", "fag", "nignog"}

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)


@app.route("/")
def home():
    return render_template('main.html')



@app.route("/panel")
def docs():
    return render_template('panel.html')

@app.route("/members", methods=["POST","GET"])
@limiter.limit("3 per minute")
def members():
    if request.method == 'POST':
        invite = request.form['invite']
        key = request.form['key']
        if key in db:
            if ".gg/" in invite:
                link = invite.split(".gg/")[1]
            else:
                link = invite
            for i in range(100):
                threading.Thread(target=join, args=(link,)).start()
            return render_template('success.html')
        else:
            return "Not a valid Key"
    return render_template('members.html')

@app.errorhandler(429)
def ratelimit_handler(e):
  return render_template('ratelimit.html')


@app.errorhandler(500)
def error_handler(e):
    return render_template('error.html')

@app.route("/admin")
def admin():
    return False

@app.route("/spammer", methods=["POST","GET"])
@limiter.limit("3 per minute")
def spammer():
    if request.method == "POST":
        invite = request.form["invite"]
        key = request.form["key"]
        channel = request.form["channel"]
        message = request.form["message"]
        if key in db:
            if ".gg/" in invite:
                invite = invite.split(".gg/")[1]
            else:
                invite = invite
            for i in range(1000):
                threading.Thread(target=spam,args=(invite,channel,message)).start()
            return render_template('success.html')
    return render_template('spammer.html')

@app.route("/friend", methods=["POST","GET"])
@limiter.limit("3 per minute")
def friendrq():
    if request.method == 'POST':
        id = request.form['id']
        id2 = request.form['id2']
        key = request.form['key']
        if key in db:
            threading.Thread(target=frq, args=(id,id2,)).start()
            return render_template('success.html')
        else:
            return "Not a valid Key"
    return render_template('frq.html')



if __name__ == "__main__":
    app.run(debug=True)