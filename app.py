from flask import Flask, redirect, url_for, render_template, request, session
import json
import user_session
from question.question import *
from question.answer import *

app = Flask(__name__)
app.secret_key = "HSL-SORTEERHOED-2020-$^&"

@app.route("/sorteerhoed/", methods=["POST", "GET"])
def home():
    if request.method == "POST" and "button" in request.form:
        form = request.form
        method = request.method

        if form["button"] == "Beginnen":
            return redirect(url_for("gegevens"))

    return render_template('index.html')

@app.route("/sorteerhoed/gegevens/", methods=["POST", "GET"])
def gegevens():
    if request.method == "POST" and "button" in request.form:
        form = request.form
        method = request.method

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

    current_question = int(user_session.getHuidigeVraag(session))

    if request.method == "POST" and "button" in request.form:
        form = request.form
        method = request.method

        if "antwoord" in form:
            user_session.setAntwoord(session, current_question, int(form["antwoord"]))
            print(user_session.getAntwoorden(session))

        if form["button"] == "Vorige vraag":
            user_session.setHuidigeVraag(session, (current_question-1))
            return redirect(url_for("vraag"))

        if form["button"] == "Volgende vraag":
            user_session.setHuidigeVraag(session, (current_question+1))
            return redirect(url_for("vraag"))

        if form["button"] == "Overzicht":
            user_session.setHuidigeVraag(session, 1)
            return redirect(url_for("overzicht"))

        if form["button"] == "Bevestigen":
            user_session.setHuidigeVraag(session, 1)
            return redirect(url_for("overzicht"))

    back = getQuestionByID(int(current_question-1)) is not None
    next = getQuestionByID(int(current_question+1)) is not None
    filled = user_session.getAntwoord(session, current_question)
    return render_template('vraag.html', question=getQuestionByID(current_question), back=back, next=next, filled=filled)

@app.route("/sorteerhoed/overzicht/", methods=["POST", "GET"])
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

if __name__ == "__main__":
    q = {
        1: {
            "vraag": "Vraag 1?",
            "antwoorden": {
                1: {
                    "antwoord": "Antwoord 1",
                    "punten": {"FICT": 1, "SE": 1, "BDM": 1, "IAT": 1}
                },
                2: {
                    "antwoord": "Antwoord 2",
                    "punten": {"FICT": 1, "SE": 1, "BDM": 1, "IAT": 1}
                },
                3: {
                    "antwoord": "Antwoord 3",
                    "punten": {"FICT": 1, "SE": 1, "BDM": 1, "IAT": 1}
                }
            }
        },
        2: {
            "vraag": "Vraag 2?",
            "antwoorden": {
                1: {
                    "antwoord": "Antwoord 1",
                    "punten": {"FICT": 1, "SE": 1, "BDM": 1, "IAT": 1}
                },
                2: {
                    "antwoord": "Antwoord 2",
                    "punten": {"FICT": 1, "SE": 1, "BDM": 1, "IAT": 1}
                },
                3: {
                    "antwoord": "Antwoord 3",
                    "punten": {"FICT": 1, "SE": 1, "BDM": 1, "IAT": 1}
                }
            }
        },
        3: {
            "vraag": "Vraag 3?",
            "antwoorden": {
                1: {
                    "antwoord": "Antwoord 1",
                    "punten": {"FICT": 1, "SE": 1, "BDM": 1, "IAT": 1}
                },
                2: {
                    "antwoord": "Antwoord 2",
                    "punten": {"FICT": 1, "SE": 1, "BDM": 1, "IAT": 1}
                },
                3: {
                    "antwoord": "Antwoord 3",
                    "punten": {"FICT": 1, "SE": 1, "BDM": 1, "IAT": 1}
                }
            }
        }
    }

    questions = []
    for id in q:
        questions.append(Question(q, id))

    app.run(debug=True)
    # app.run(host='0.0.0.0', debug=True)

    # question = Question(q, 1)
    # print(question.getVraag())
    # for antwoord in question.getAntwoorden():
    #     print(antwoord.getTekst())
    #     print(antwoord.getPunten("FICT"))

    # TODO: Maak database connectie
    # TODO: Laad vragelijst
