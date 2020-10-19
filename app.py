from flask import *
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = 'H8QEt7JrraIV'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(days=14)
email = []
db = SQLAlchemy(app)
class user(db.Model):
    _id = db.Column("id",db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    def __init__(self,name, email):
        self.name = name
        self.email = email




@app.route('/SignIN', methods=["POST","GET"])
def SignIN():
    if request.method == "POST":
        session.permanent = True
        user = request.form["username"]
        session['user'] = user
        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session["email"] = found_user.email


        else:
            usr = users(user,"")
            db.session.add(usr)
            db.session.commit()

        return redirect(url_for("user", usr=user))
    else:
        return render_template("index.html")


@app.route('/')
def home_page():
    # if "user" in session:
    #     user =  session["user"]
        return render_template("main_page.html")
    # else:
        return redirect(url_for('SignIN'))


@app.route('/<usr>')
def user(usr):
    if "user" in session:
        user = session["user"]
        return render_template("main_page.html")
    else:
        return render_template("index.html")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
