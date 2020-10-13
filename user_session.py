def hasSession(session):
    return "gebruikersnaam" in session

def createSession(session, name):
    clearSession(session)
    session["gebruikersnaam"] = name
    # session["punten"] = {
    #     "FICT": 0,
    #     "SE": 0,
    #     "BDM": 0,
    #     "IAT": 0
    # }
    # session["huidige_vraag"] = 1

def clearSession(session):
    session.pop("gebruikersnaam", None)
    # session.pop("punten", None)
    # session.pop("huidige_vraag", None)

def getGebruikersnaam(session):
    return session["gebruikersnaam"]

def setGebruikersnaam(session, naam):
    session["gebruikersnaam"] = naam

# def getHuidigeVraag(session):
#     return session["huidige_vraag"]
#
# def setHuidigeVraag(session, vraag):
#     session["huidige_vraag"] = vraag
#
# def addHuidigeVraag(session):
#     setHuidigeVraag(session, (getHuidigeVraag(session) + 1))
#
# def getPunten(session, specialisatie):
#     if specialisatie in session["punten"]:
#         return session["punten"][specialisatie]
#     return 0
#
# def setPunten(session, specialisatie, punten: int):
#     session["punten"][specialisatie] = punten
#
# def addPunten(session, specialisatie, punten: int):
#     setPunten(session, specialisatie, (getPunten(session, specialisatie) + punten))
