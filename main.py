from flask import *
from datetime import timedelta






app = Flask(__name__)

app.permanent_session_lifetime = timedelta(days=14)




@app.route('/Home_Page', methods=["POST","GET"])
def Home_Page():
    if request.method == "POST":
        session.permanent = True
        user = request.form["usr_name"]
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
        return redirect(url_for('Home_Page'))


@app.route('/<usr>')
def user(usr):
    if "user" in session:
        user = session["user"]
        return render_template("main_page.html")
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run()
