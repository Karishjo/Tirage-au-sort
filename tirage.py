from flask import Flask,redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqilte:///groups.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class main(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    num = db.Column("Number", db.Integer)
    status = db.Column("Status", db.Boolean)
    
    def __init__(self,num, status):
        self.num = num
        self.status = False

class jeune(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    num = db.Column("Number", db.Integer)
    status = db.Column("Status", db.Boolean)
    
    def __init__(self,num, status):
        self.num = num
        self.status = False

class enfant(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    num = db.Column("Number", db.Integer)
    status = db.Column("Status", db.Boolean)
    
    def __init__(self,num, status):
        self.num = num
        self.status = False                



@app.route("/draw_number") #redirect to draw button
def draw_number():
    return render_template("draw_number.html")

@app.route("/", methods = ["POST", "GET"]) #default route
def home():
    if request.method == "POST":
        if choice == request.form["main"]:
            return redirect(url_for("choice", groupchoice = choice))
        elif choice == request.form["jeune"]:
            return redirect(url_for("choice", groupchoice = choice))
        elif choice == request.form["enfant"]:
            return redirect(url_for("choice", groupchoice = choice))
    else:
        return render_template("group_choice.html")
    
@app.route("/<groupchoice>)")    
def choice(groupchoice):
    return groupchoice

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)