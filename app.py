from flask import Flask, redirect, url_for, render_template, request, session
import json
import specialisaties
import database
import user_session
from question.question import *
from question.answer import *
import mysql.connector
import string, random
import time

app = Flask(__name__)
app.secret_key = "HSL-SORTEERHOED-2020-$^&"

@app.route("/", methods=["GET"])
def home():
    if request.values.get('a') == 'start':
        user_session.clearSession(session)
        user_session.createSession(session, "Nope", "TEST123", "Tom@alt-del.nl")
        return redirect(url_for("vraag"))

    return render_template('index.html')

@app.route("/einde", methods=["GET"])
def einde():
    # Controleerd of elke vraag is ingevuld
    if len(user_session.getIngevuldeAntwoorden(session)) < len(questions):
        return redirect(url_for("badrequest"))

    eindantwoorden = user_session.getAntwoorden(session)
    punten = {'fict': 0, 'bdm': 0, 'iat': 0, 'se': 0}

    # Hoeveel punten je per specialisatie maximaal kan krijgen
    puntenperspec = {'fict': getMaxPointsBySpec("FICT"), 'bdm': getMaxPointsBySpec("BDM"), 'iat': getMaxPointsBySpec("IAT"), 'se': getMaxPointsBySpec("SE")}

    for question in questions:
        id = question.getID()
        antwoord = question.getAntwoordByID(user_session.getAntwoord(session, question.getID()))

        punten['fict'] += antwoord.getPunten('FICT')
        punten['bdm'] += antwoord.getPunten('BDM')
        punten['iat'] += antwoord.getPunten('IAT')
        punten['se'] += antwoord.getPunten('SE')

    print(punten['fict'], punten['bdm'], punten['iat'], punten['se'])

    # Op basis van punten de beste spec berekeken
    # TEMP kan eigenlijk weg, we doen het nu met procenten
    max_key = max(punten, key=punten.get)
    print(f"Beste optie: {max_key} volgens absolute aantal punten: {punten}")

    # Procentuele keuze berekenen, delen door max haalbare punten
    for spec in punten:
        punten[spec]
        punten[spec] = punten[spec] / puntenperspec[spec] * 100

        # Afronden op 2 decimalen
        punten[spec] = round(punten[spec], 2)

    max_key = max(punten, key=punten.get)
    print(f"Beste optie: {max_key} volgens procentuele aantal punten: {punten}")

    # Kijken of er meerdere specialisaties gelijk zijn
    maxpunt = punten[max_key]
    maxspecs = []
    for spec in punten:
        if punten[spec] == maxpunt:
            maxspecs.append(spec)
    if len(maxspecs) > 1:
        print(f"Let op! Meerdere specialisaties gelijk aantal punten: {maxspecs}")

    # Staafdiagram maken
    # graph(punten)

    return render_template('finished.html', eindspecialisatie=specialisaties.get_specialisatie_naam(max_key), tekst=specialisaties.get_promotekst(max_key))


@app.route("/vraag", methods=["POST", "GET"])
def vraag():
    if not user_session.hasSession(session):
        return redirect(url_for("home"))

    current_question = int(user_session.getHuidigeVraag(session))
    back = getQuestionByID(current_question-1) is not None
    next = getQuestionByID(int(current_question+1)) is not None

    filledAnswers = len(user_session.getAnswerList(session))

    finishable = False
    if filledAnswers > 18 and not next:
        finishable = True

    if request.method == 'POST':
        if request.values.get('csrf-token') == user_session.getCSRFToken(session):
            userAnswer = request.values.get('user-answer')
            user_session.setAntwoord(session, current_question, int(userAnswer))

            if next:
                user_session.setHuidigeVraag(session, (current_question+1))
                return redirect(url_for("vraag"))
            else:
                user_session.setHuidigeVraag(session, current_question)
                if finishable == True:
                    return redirect(url_for("einde"))
                else:
                    return redirect(url_for("overzicht"))
        else:
            user_session.clearSession(session)
            return redirect(url_for("badrequest"))

    if request.values.get('a') == 'back':
        user_session.setHuidigeVraag(session, (current_question-1))
        return redirect(url_for("vraag"))
    filled = user_session.getAntwoord(session, current_question)

    progress = (100 / len(questions)) * len(user_session.getAntwoorden(session))
    return render_template('vraag.html', question=getQuestionByID(current_question), back=back, next=next, filled=filled, progress=progress, csrfToken=user_session.setCSRFToken(session), ready=finishable, answerCount=filledAnswers)

@app.route("/overzicht", methods=["POST", "GET"])
def overzicht():
    if not user_session.hasSession(session):
        return redirect(url_for("home"))

    if request.method == "POST" and "button" in request.form:
        form = request.form
        method = request.method

        if form["button"] == "Resultaat berekenen":
            return redirect(url_for("home"))

        user_session.setHuidigeVraag(session, int(form["button"]))
        return redirect(url_for("vraag"))

    print(user_session.getIngevuldeAntwoorden(session))
    return render_template('overzicht.html', questions=questions, filled=user_session.getIngevuldeAntwoorden(session))

def getQuestionByID(id: int):
    for question in questions:
        if question.id == id:
            return question

def getMaxPointsBySpec(specialisatie):
    points = 0
    for question in questions:
        points += question.getPunten(specialisatie)
    return int(points)

@app.route("/bad-request", methods=["GET"])
def badrequest():
    return render_template('errors/400.html'), 400

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('errors/404.html'), 404

@app.errorhandler(400)
def bad_request(e):
    # note that we set the 404 status explicitly
    return render_template('errors/400.html'), 400

if __name__ == "__main__":
    db_conn = database.setup()
    vragen_dict = database.set_ans(db_conn, database.laad_vragen(db_conn))
    questions = []

    # Zet de vragen in de dict om in objecten
    for id in vragen_dict:
        questions.append(Question(vragen_dict, id))

    app.run(debug=True)
    #app.run(host='0.0.0.0', debug=True)
