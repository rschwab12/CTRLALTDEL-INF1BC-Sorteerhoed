import string
import random

def hasSession(session):
    return "huidige_vraag" in session

def createSession(session):
    clearSession(session)
    session["huidige_vraag"] = 1
    session["antwoorden"] = {}

def clearSession(session):
    if hasSession(session):
        session.pop("huidige_vraag", None)
        session.pop("antwoorden", None)


def getHuidigeVraag(session):
    return session["huidige_vraag"]

def setHuidigeVraag(session, vraag):
    session["huidige_vraag"] = vraag

def setAntwoord(session, vraag_id: int, antwoord_id: int):
    session["antwoorden"][str(vraag_id)] = antwoord_id

def getAntwoord(session, vraag_id: int):
    if not isIngevuld(session, vraag_id): return 0
    return session["antwoorden"][str(vraag_id)]

def getAnswerList(session):
    return session["antwoorden"]
    
def isIngevuld(session, vraag_id: int):
    return str(vraag_id) in session["antwoorden"]

def getAntwoorden(session):
    return session["antwoorden"]

def getIngevuldeAntwoorden(session):
    ingevuld = []
    for a in getAntwoorden(session):
        ingevuld.append(int(a))

    return ingevuld

def getCSRFToken(session):
    return session["CSRF-TOKEN"]

def setCSRFToken(session):
    letters = string.ascii_letters
    token = ''.join(random.choice(letters) for i in range(20))
    session["CSRF-TOKEN"] = token
    return token
