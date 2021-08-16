from flask import Flask, render_template

app = Flask(__name__)


@app.route("/for-loops")
def render_for_loop():
    user_os = {
        "Bob Smith": "Arch",
        "John Silver": "Mac",
        "Adam Mcornick": "Ubuntu",
        "Leo Camaro": "Windows",
    }
    return render_template("for_loops.html", user_os=user_os)
# def render_for_loop():
#     planets = [
#         "Mercury",
#         "Venus",
#         "Mars",
#         "Pluto",
#         "Jupiter",
#         "Saturn",
#         "Uranus",
#         "Neptune"
#     ]

#     return render_template("for_loops.html", planets=planets)
