from flask import Flask, redirect, url_for, render_template, request, session
import json
import database
import user_session
from question.question import *
from question.answer import *
import mysql.connector
import pprint
import string
import random
import plotly.express as px
import pandas as pd

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
    eindantwoorden = user_session.getAntwoorden(session)
    punten = {'fict': 0, 'bdam': 0, 'iat': 0, 'se': 0}

    # Hoeveel punten je per specialisatie kan krijgen
    puntenperspec = {'fict': 19, 'bdam': 15, 'iat': 22, 'se': 16}

    # Voor elk antwoord de bijbehorende punten optellen
    for vraag in eindantwoorden:
        antwoorden = database.get_punten_voor_spec(vraag, eindantwoorden[vraag], db_conn)
        for specialisatie in antwoorden:
            punten['fict'] += specialisatie['fict']
            punten['bdam'] += specialisatie['bdam']
            punten['iat'] += specialisatie['iat']
            punten['se'] += specialisatie['se']
        
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
    #graph(punten)

    # Doorgeven aan html welke specialisatie gekozen is
    if max_key == "fict":
        eindspecialisatie = "Forensisch ICT"
    elif max_key == "bdam":
        eindspecialisatie = "Business Data Management"
    elif max_key == "iat":
        eindspecialisatie = "Interactie Technologie"
    elif max_key == "se":
        eindspecialisatie = "Software Engineering"
    
    return render_template('finished.html', eindspecialisatie=eindspecialisatie, tekst=get_promotekst(max_key))

def graph(punten):
    # Staafdiagram maken
    data = pd.DataFrame({'Specialisatie': ['FICT', 'BDAM', 'IAT', 'SE'], 'antwoorden': [punten['fict'], punten['bdam'], punten['iat'], punten['se']]})
    fig = px.bar(data, x='Specialisatie', y='antwoorden', labels={'antwoorden':'Past bij jou (%)'}, range_y=[0,100])
    fig.show()

    # Maakt er een svg van
    fig.write_image("graph.svg")


@app.route("/vraag", methods=["POST", "GET"])
def vraag():
    if not user_session.hasSession(session):
        return redirect(url_for("home"))

    current_question = int(user_session.getHuidigeVraag(session))
    back = getQuestionByID(current_question-1) is not None
    next = getQuestionByID(int(current_question+1)) is not None

    if request.method == 'POST':

        if request.values.get('csrf-token') == user_session.getCSRFToken(session):
            userAnswer = request.values.get('user-answer')
            user_session.setAntwoord(session, current_question, int(userAnswer))

            if next:
                user_session.setHuidigeVraag(session, (current_question+1))
                return redirect(url_for("vraag"))
            else:
                return redirect(url_for("einde"))
        else:
            user_session.clearSession(session)
            return redirect(url_for("badrequest"))

    if request.values.get('a') == 'back':
        user_session.setHuidigeVraag(session, (current_question-1))
        return redirect(url_for("vraag"))

    filled = user_session.getAntwoord(session, current_question)
    return render_template('vraag.html', question=getQuestionByID(current_question), back=back, next=next, filled=filled, csrfToken=user_session.setCSRFToken(session))

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

@app.route("/bad-request", methods=["GET"])
def badrequest():
    return render_template('errors/400.html'), 400

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('errors/404.html'), 404

@app.errorhandler(400)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('errors/400.html'), 400

def get_promotekst(specialisatie):
    # Sorry, beetje rommelig dit... maar het werkt :)
    fict = 'Jij bent analytisch, doelgericht en vasthoudend. Je houdt van rechercheren en onderzoeken en voelt je verantwoordelijk voor het bevorderen van een veilige maatschappij en het verminderen van criminaliteit. Je bent innovatief en nieuwsgierig naar de nieuwste technologieën en de mogelijkheden die ze bieden.<br> Je kunt goed omgaan met mensen en weet ze naar waarde in te schatten. Je hebt er plezier in om slimme wegen te vinden die leiden naar oplossingen voor ingewikkelde zaken.<br> Met Forensisch ICT heb je carrièrekansen bij politie, justitie, defensie maar ook in de particuliere markt! <br><br>Meer weten over Forensisch ICT? <a href="https://www.hsleiden.nl/informatica/opbouw-studie/forensisch-ict.html" target="_blank"><b>Klik hier!</b></a>'
    bdam = 'Jij bent nieuwsgierig en analytisch ingesteld. Je bent niet bang om veel met data te werken, sterker nog, jij haalt hier je plezier uit! Je bent een data-tovenaar, van modelleren tot analyseren en adviseren, met data krijg jij alles voor elkaar. Je vindt het leuk om onderzoek te doen en gaat werken met Artificial Intelligence.<br> Jouw kennis en vaardigheden helpen bedrijven te verbeteren en optimaliseren.<br> Met Business Data Management kan je bijvoorbeeld aan de slag als data-analist of als Business Intelligence consultant. <br><br>Meer weten over Business Data Management? <a href="https://www.hsleiden.nl/informatica/opbouw-studie/business-data-management.html" target="_blank"><b>Klik hier!</b></a>'
    iat = 'Jij bent creatief en hebt geen vrees voor technologie. Je bent nieuwsgierig naar de nieuwste ontwikkelingen in technologie, social media en mogelijkheden van gebruikersinteractie.<br> Je bent kritisch en kan je goed verplaatsen in gebruikers.<br> Je kunt goed luisteren naar de wensen en belangen van verschillende partijen en samenwerken in multidisciplinaire teams.<br> Met Interactie Technologie kan je aan de slag als bijvoorbeeld Interaction designer of als Desktoppublisher.<br><br>Meer weten over Interactie Technologie? <a href="https://www.hsleiden.nl/informatica/opbouw-studie/interactie-technologie.html" target="_blank"><b>Klik hier!</b></a>'
    se = 'Jij hebt een sterk analytisch vermogen. Je bent creatief en ontwerpt en programmeert graag. Je hebt er plezier in om slimme oplossingen voor ingewikkelde problemen te bedenken.<br> Je beschikt over de nodige sociale vaardigheden om samen met anderen te bedenken welk product het beste past bij de wensen van een bedrijf of instelling.<br> Met Software Engineering kan je aan de slag als bijvoorbeeld Software Engineer, Back-end developer, Front-end developer, Technical Designer of als Database Engineer. <br><br>Meer weten over Software Engineering? <a href="https://www.hsleiden.nl/informatica/opbouw-studie/software-engineering.html" target="_blank"><b>Klik hier!</b></a>'
    if specialisatie == "fict":
        return fict
    elif specialisatie == "bdam":
        return bdam
    elif specialisatie == "iat":
        return iat
    elif specialisatie == "se":
        return se

if __name__ == "__main__":
    pp = pprint.PrettyPrinter()
    db_conn = database.setup()
    vragen_dict = database.set_ans(db_conn, database.laad_vragen(db_conn)) 
    questions = []
    for id in vragen_dict:
        questions.append(Question(vragen_dict, id))
    app.run(debug=True)
    #app.run(host='0.0.0.0', debug=True)

    # question = Question(q, 1)
    # print(question.getVraag())
    # for antwoord in question.getAntwoorden():
    #     print(antwoord.getTekst())
    #     print(antwoord.getPunten("FICT"))

    # TODO: Maak database connectie
    # TODO: Laad vragelijst
