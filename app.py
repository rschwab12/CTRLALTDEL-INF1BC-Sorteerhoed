from flask import Flask, redirect, url_for, render_template, request, session
import json
import database
import user_session
from question.question import *
from question.answer import *
import mysql.connector

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
    return render_template('finished.html')

@app.route("/vraag", methods=["POST", "GET"])
def vraag():
    if not user_session.hasSession(session):
        return redirect(url_for("home"))

    current_question = int(user_session.getHuidigeVraag(session))
    back = getQuestionByID(current_question-1) is not None
    next = getQuestionByID(int(current_question+1)) is not None

    if request.method == 'POST':
        userAnswer = request.values.get('user-answer')
        user_session.setAntwoord(session, current_question, int(userAnswer))

        if next:
            user_session.setHuidigeVraag(session, (current_question+1))
            return redirect(url_for("vraag"))
        else:
            return redirect(url_for("einde"))

    if request.values.get('a') == 'back':
        user_session.setHuidigeVraag(session, (current_question-1))
        return redirect(url_for("vraag"))

    filled = user_session.getAntwoord(session, current_question)
    return render_template('vraag.html', question=getQuestionByID(current_question), back=back, next=next, filled=filled)

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

if __name__ == "__main__":
    q = {
        1: {
            "vraag": "Vraag 1?",
            "antwoorden": {
                1: {
                    "letter": "A",
                    "antwoord": "Antwoord 1",
                    "punten": {"FICT": 1, "SE": 1, "BDM": 1, "IAT": 1}
                },
                2: {
                    "letter": "B",
                    "antwoord": "Antwoord 2",
                    "punten": {"FICT": 1, "SE": 1, "BDM": 1, "IAT": 1}
                },
                3: {
                    "letter": "C",
                    "antwoord": "Antwoord 3",
                    "punten": {"FICT": 1, "SE": 1, "BDM": 1, "IAT": 1}
                }
            }
        },
        2: {
            "vraag": "Vraag 2?",
            "antwoorden": {
                1: {
                    "letter": "A",
                    "antwoord": "Antwoord 1",
                    "punten": {"FICT": 1, "SE": 1, "BDM": 1, "IAT": 1}
                },
                2: {
                    "letter": "B",
                    "antwoord": "Antwoord 2",
                    "punten": {"FICT": 1, "SE": 1, "BDM": 1, "IAT": 1}
                },
                3: {
                    "letter": "C",
                    "antwoord": "Antwoord 3",
                    "punten": {"FICT": 1, "SE": 1, "BDM": 1, "IAT": 1}
                }
            }
        },
        3: {
            "vraag": "Vraag 3?",
            "antwoorden": {
                1: {
                    "letter": "A",
                    "antwoord": "Antwoord 1",
                    "punten": {"FICT": 1, "SE": 1, "BDM": 1, "IAT": 1}
                },
                2: {
                    "letter": "B",
                    "antwoord": "Antwoord 2",
                    "punten": {"FICT": 1, "SE": 1, "BDM": 1, "IAT": 1}
                },
                3: {
                    "letter": "C",
                    "antwoord": "Antwoord 3",
                    "punten": {"FICT": 1, "SE": 1, "BDM": 1, "IAT": 1}
                }
            }
        }
    }

    questions = []
    for id in q:
        questions.append(Question(q, id))

    db_conn = database.setup()
    vragen_dict = database.laad_vragen(db_conn)

    app.run(debug=True)
    # app.run(host='0.0.0.0', debug=True)

    # question = Question(q, 1)
    # print(question.getVraag())
    # for antwoord in question.getAntwoorden():
    #     print(antwoord.getTekst())
    #     print(antwoord.getPunten("FICT"))

    # TODO: Maak database connectie
    # TODO: Laad vragelijst
