from lib import power
# Import what we need from flask
from flask import Flask, request

# Create a Flask app inside `app`
app = Flask(__name__)


# Assign a function to be called when the path `/` is requested
@app.route("/")
def index():
    power1 = request.args.get("power1", "")
    power2 = request.args.get("power2", "")
    return (
        """ <h2>Thanx Winc Team!</h2>
            <br /><br />
            <form action="" method="get">
                <input type="text" name="number 1">
                <input type="text" name="number 2">
                <input type="submit" value="Release the POWER">
            </form>"""
        + power1
    )


@app.route("/<int:power>")
def calculate(power1, power2):
    return power(power1, power2)
