from flask import Flask, render_template

app = Flask(__name__)


@app.route("/expressions/")
def hello_world():

    color = "brown"
    animal_one = "fox"
    animal_two = "dog"

    orange_amount = 30
    apple_amount = 20
    donate_amount = 15

    first_name = "Jaden"
    last_name = "Yuki"

    kwargs = {
        "color": color,
        "animal_one": animal_one,
        "animal_two": animal_two,
        "orange_amount": orange_amount,
        "apple_amount": apple_amount,
        "donate_amount": donate_amount,
        "first_name": first_name,
        "last_name": last_name
    }
    return render_template("expressions.html", **kwargs)
