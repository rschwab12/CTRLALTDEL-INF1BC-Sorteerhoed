from flask import Flask, redirect, url_for, render_template, request, session
import json
import user_session

app = Flask(__name__)
app.secret_key = "HSL-SORTEERHOED-2020-$^&"

@app.route("/sorteerhoed/", methods=["POST", "GET"])
def home():
    form = request.form
    method = request.method

    if method == "POST" and "button" in request.form:
        if form["button"] == "Beginnen":
            return redirect(url_for("gegevens"))

    return render_template('index.html')

@app.route("/sorteerhoed/gegevens/", methods=["POST", "GET"])
def gegevens():
    form = request.form
    method = request.method

    if method == "POST" and "button" in form:
        if form["button"] == "Vragenlijst starten":
            user_session.clearSession(session)
            user_session.createSession(session, form["username"], "TEST123", "Tom@alt-del.nl")
            # user_session.createSession(session, form["username"], form["student_number"], form["mail_address"])
            return redirect(url_for("vraag"))

    return render_template('gegevens.html')

@app.route("/sorteerhoed/vraag/", methods=["POST", "GET"])
def vraag():
    if not user_session.hasSession(session):
        return redirect(url_for("home"))

    if request.method == "POST":
        return redirect(url_for("done"))

    return render_template('vraag.html')

@app.route("/sorteerhoed/done/", methods=["POST", "GET"])
def done():
    if request.method == "POST":
        user_session.clearSession(session)
        return redirect(url_for("home"))

    return render_template('done.html', name = user_session.getUsername(session))

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', debug=True)

    # TODO: Maak database connectie
    # TODO: Laad vragelijst
