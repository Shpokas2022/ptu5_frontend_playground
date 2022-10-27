from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("styling/home_dva.html")
if __name__ == "__main__":
    app.run(debug=True)