def hasSession(session):
    return "huidige_vraag" in session

def createSession(session, name, student, mail):
    clearSession(session)
    # session["username"] = name
    # session["student_number"] = student
    # session["mail_address"] = mail
    session["huidige_vraag"] = 1
    session["antwoorden"] = {}

def clearSession(session):
    if hasSession(session):
        # session.pop("username", None)
        # session.pop("student_number", None)
        # session.pop("email_address", None)
        session.pop("huidige_vraag", None)
        session.pop("antwoorden", None)

# def getUsername(session):
#     return session["username"]
#
# def setUsername(session, naam):
#     session["username"] = naam
#
# def getStudentNumber(session):
#     return session["student_number"]
#
# def setStudentNumber(session, naam):
#     session["student_number"] = naam
#
# def getEmailAddress(session):
#     return session["email_address"]
#
# def setEmailAddress(session, naam):
#     session["email_address"] = naam

def getHuidigeVraag(session):
    return session["huidige_vraag"]

def setHuidigeVraag(session, vraag):
    session["huidige_vraag"] = vraag

def setAntwoord(session, vraag_id: int, antwoord_id: int):
    session["antwoorden"][str(vraag_id)] = antwoord_id

def getAntwoord(session, vraag_id: int):
    if not isIngevuld(session, vraag_id): return 0
    return session["antwoorden"][str(vraag_id)]

def isIngevuld(session, vraag_id: int):
    return str(vraag_id) in session["antwoorden"]

def getAntwoorden(session):
    return session["antwoorden"]

def getIngevuldeAntwoorden(session):
    ingevuld = []
    for a in getAntwoorden(session):
        ingevuld.append(int(a))

    return ingevuld
