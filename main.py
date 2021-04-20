import lib
# Import what we need from flask
from flask import Flask, request

# Create a Flask app inside `app`
app = Flask(__name__)


# Assign a function to be called when the path `/` is requested
@app.route("/")
def index():
    
    power1 = request.args.get("power1", "")
    power2 = request.args.get("power2", "")
    
    if power1 and power2:
        solution = power(power1, power2)
    else:
        solution = ""
    
    return (
            """ <br />
                <h2>Thanx Winc Team!</h2>
                <br />
                <form action="" method="get">
                    Number 1: <input type="text" name="power1"><br /><br />
                    Number 2: <input type="text" name="power2"><br /><br />
                    <input type="submit" value="Unleash the POWER!!!">
                </form>"""
            + "Solution: "
            + solution
            )


# def calc(power1, power2):
#     try:
#         solution = lib.power(power1, power2)
#         return str(solution)
#     except ValueError:
#         return "invalid input"
def power(x, y):
    try:
        return str(x**y)
    except ValueError:
        return "invalid input"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)