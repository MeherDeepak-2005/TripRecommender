from flask import *
from datetime import timedelta
import os





app = Flask(__name__)
app.secret_key = "H8QEt7JrraIV"
app.permanent_session_lifetime = timedelta(days=14)




@app.route('/SignIN', methods=["POST","GET"])
def SignIN():
    if request.method == "POST":
        session.permanent = True
        user = request.form["usr"]
        session['user'] = user
        return redirect(url_for("user", usr=user))
    else:
        return render_template("index.html")
        
    
@app.route('/')
def home_page():
    if "user" in session:
        user =  session["user"]
        return render_template("main_page.html")
    else:
        return redirect(url_for('SignIN'))


@app.route('/<usr>')
def user(usr):
    if "user" in session:
        user = session["user"]
        return render_template("main_page.html")
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
