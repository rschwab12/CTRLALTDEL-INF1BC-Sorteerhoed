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
    # Homepage, creates session
    if request.values.get('a') == 'start':
        user_session.clearSession(session)
        user_session.createSession(session)
        return redirect(url_for("vraag"))

    return render_template('index.html')

@app.route("/einde", methods=["GET"])
def einde():
    # Checking if every question has been answered, before going to results page
    if len(user_session.getIngevuldeAntwoorden(session)) < len(questions):
        return redirect(url_for("badrequest"))

    punten = {'fict': 0, 'bdm': 0, 'iat': 0, 'se': 0}

    # Acquiring maximum points for each specialisation
    puntenperspec = {'fict': getMaxPointsBySpec("FICT"), 'bdm': getMaxPointsBySpec("BDM"), 'iat': getMaxPointsBySpec("IAT"), 'se': getMaxPointsBySpec("SE")}

    # Adding the assigned specialisation points for each answered question
    for question in questions:
        antwoord = question.getAntwoordByID(user_session.getAntwoord(session, question.getID()))

        punten['fict'] += antwoord.getPunten('FICT')
        punten['bdm'] += antwoord.getPunten('BDM')
        punten['iat'] += antwoord.getPunten('IAT')
        punten['se'] += antwoord.getPunten('SE')

    # Calculating the final score, by dividing the achieved points with the maximum possible points for each specialisation
    for spec in punten:
        punten[spec]
        punten[spec] = punten[spec] / puntenperspec[spec] * 100

        # Rounding the score to 2 decimals
        punten[spec] = round(punten[spec], 2)

    max_key = max(punten, key=punten.get)

    # Checking if multiple specialisations have the same score
    maxpunt = punten[max_key]
    maxspecs = []
    for spec in punten:
        if punten[spec] == maxpunt:
            maxspecs.append(spec)
    if len(maxspecs) > 1:
        print("error")
        pass
        # Oh no, multiple specialisations have the same score. We will show the first one to the user.

    return render_template('finished.html', eindspecialisatie=specialisaties.get_specialisatie_naam(max_key), tekst=specialisaties.get_promotekst(max_key))


@app.route("/vraag", methods=["POST", "GET"])
def vraag():
    # If the user doesn't have a current session, redirect them to the homepage
    if not user_session.hasSession(session):
        return redirect(url_for("home"))

    current_question = int(user_session.getHuidigeVraag(session))
    back = getQuestionByID(current_question-1) is not None
    next = getQuestionByID(int(current_question+1)) is not None

    filledAnswers = len(user_session.getAnswerList(session))

    finishable = False
    if filledAnswers > 18 and not next:
        finishable = True

    # Called on when answering
    if request.method == 'POST':
        if request.values.get('csrf-token') == user_session.getCSRFToken(session):
            userAnswer = request.values.get('user-answer')
            user_session.setAntwoord(session, current_question, int(userAnswer))

            # Checking if we can show another question, or if this is the final question
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
            # Session doesn't belong to this user...
            user_session.clearSession(session)
            return redirect(url_for("badrequest"))

    # User wants to go back to the previous question
    if request.values.get('a') == 'back':
        user_session.setHuidigeVraag(session, (current_question-1))
        return redirect(url_for("vraag"))
    filled = user_session.getAntwoord(session, current_question)

    # Updating the progressbar
    progress = (100 / len(questions)) * len(user_session.getAntwoorden(session))
    return render_template('vraag.html', question=getQuestionByID(current_question), back=back, next=next, filled=filled, progress=progress, csrfToken=user_session.setCSRFToken(session), ready=str(finishable), answerCount=filledAnswers)

@app.route("/overzicht", methods=["POST", "GET"])
def overzicht():
    # If the user doesn't have a current session, redirect them to the homepage
    if not user_session.hasSession(session):
        return redirect(url_for("home"))

    if request.method == "POST" and "button" in request.form:
        form = request.form

        if form["button"] == "Resultaat berekenen":
            return redirect(url_for("home"))

        user_session.setHuidigeVraag(session, int(form["button"]))
        return redirect(url_for("vraag"))

    return render_template('overzicht.html', questions=questions, filled=user_session.getIngevuldeAntwoorden(session))

def getQuestionByID(id: int):
    # Get the question that belongs to this id
    for question in questions:
        if question.id == id:
            return question

def getMaxPointsBySpec(specialisatie):
    # Get maximum possible points for a specialisation
    points = 0
    for question in questions:
        points += question.getPunten(specialisatie)
    return int(points)

@app.route("/bad-request", methods=["GET"])
def badrequest():
    return render_template('errors/400.html'), 400

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(400)
def bad_request(e):
    return render_template('errors/400.html'), 400

if __name__ == "__main__":
    # Initialization, connecting with the database, retrieving questions
    db_conn = database.setup()
    vragen_dict = database.set_ans(db_conn, database.laad_vragen(db_conn))
    questions = []

    # Converts the questions from the dictionary to objects
    for id in vragen_dict:
        questions.append(Question(vragen_dict, id))

    app.run(debug=True)
