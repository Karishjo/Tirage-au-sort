from flask import redirect, url_for, render_template, request
from apps import app, db
from models import main, jeune, enfant
import random

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        choice = request.form.get("group")

        return redirect(url_for("draw_number", groupchoice=choice))

    return render_template("group_choice.html")

@app.route("/draw_number")
def draw_number():
    return render_template("draw_number.html")

@app.route("/display/<number>")
def display(number):
    return render_template("display.html", number=number)

@app.route("/draw/<groupchoice>")
def draw(groupchoice):
    if groupchoice == "main":
        model = main
    elif groupchoice == "jeune":
        model = jeune
    elif groupchoice == "enfant":
        model = enfant
    else:
        return "Invalid group", 400

    available_numbers = model.query.filter_by(status=False).all()

    if not available_numbers:
        return "No more numbers available", 400

    picked = random.choice(available_numbers)
    # 4. Update status
    picked.status = True
    db.session.commit()

    # 5. Redirect to display page
    return redirect(url_for("display", number=picked.num))



