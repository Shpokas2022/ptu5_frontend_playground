from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Mano pirmas puslapis su Python"

@app.route("/darius")

def darius():
    return "darius, darius, darius, darius, darius"

@app.route("/keliamieji_skaiciavimai")
def keliamieji():
    # Kreipiuosi į žodyną
    ivesta = int(request.args["metai"])
    if ivesta % 4 == 0 or (ivesta % 100 !=0 and ivesta % 400 == 0):
        atsakymas = "keliamieji"
    else:
        atsakymas = "nekeliamieji"
        
    return render_template("keliamieji_skaiciavimai.html", **request.args, atsakymas=atsakymas)

@app.route("/keliamieji2")
def keliamieji2():
    return render_template("keliamieji2.html")




if __name__ == "__main__":
    app.run(debug=True)
