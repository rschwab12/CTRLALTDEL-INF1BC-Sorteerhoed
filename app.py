from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = "HSL-SORTEERHOED-2020-$^&"

# Eerste pagina van de applicatie. Hierin komen gebruikens wanneer ze naar het hoofddomein van de website gaan
@app.route("/sorteerhoed", methods=["POST", "GET"])
def home():
    # Controleerd of de user al in een eerdere sessie zit. Zo ja? dan verwijderd die deze sessie
    if "user" in session:
        session.pop("user", None)

    # Post method controleerd of de user op de start knop heeft gedrukt
    if request.method == "POST":
        session["user"] = request.form["name"]
        return redirect(url_for("vragenlijst"))

    # Laad de hoofdpagina
    return render_template('index.html')

# Pagina waar alle vragen op komen te staan, hier moet nog code toegevoegd worden om de vragen uit python naar html te pushen
@app.route("/sorteerhoed/vragenlijst", methods=["POST", "GET"])
def vragenlijst():
    # Controleerd of de user in een sessie zit. Zo niet? dan word de user naar de homepagina gestuurd
    if not "user" in session:
        return redirect(url_for("home"))

    # Post method controleerd of de user op de invul knop heeft gedrukt
    if request.method == "POST":
        return redirect(url_for("done"))

    # Laad de vragenlijst pagina in
    return render_template('vragenlijst.html')

# Deze pagina geeft aan dat de vragenlijst is ingevuld. Ook geeft het je de funcite om terug te gaan naar de hoofdpagina
@app.route("/sorteerhoed/done", methods=["POST", "GET"])
def done():
    # Post method controleerd of de user op de terug knop heeft gedrukt. Zo ja? Dan word de sessie leeggemaakt en word de gebruiker naar de hoofdpagina gestuur
    if request.method == "POST":
        session.pop("user", None)
        return redirect(url_for("home"))

    # Laad de laatste (done) pagina in
    return render_template('done.html', name = getSessionName())

# Vraagt de naam van de user op (De naam die je op de hoofdpagina invult)
def getSessionName():
    return session["user"]

# Main method
if __name__ == "__main__":
    app.run(debug=True)

    # TODO: Maak database connectie
    # TODO: Laad vragelijst
