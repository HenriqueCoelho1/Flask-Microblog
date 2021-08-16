from flask import Flask, render_template

app = Flask(__name__)


@app.route("/conditionals-basics")
def render_conditionals_basics():
    company = "Microsoft"
    return render_template("conditional_basics.html", company=company)
