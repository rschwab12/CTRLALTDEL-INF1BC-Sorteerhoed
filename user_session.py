def hasSession(session):
    return "username" in session

def createSession(session, name, student, mail):
    clearSession(session)
    session["username"] = name
    session["student_number"] = student
    session["mail_address"] = mail
    session["huidige_vraag"] = 1
    session["ingevulde_vragen"] = {}

    # session["punten"] = {
    #     "FICT": 0,
    #     "SE": 0,
    #     "BDM": 0,
    #     "IAT": 0
    # }

def clearSession(session):
    if hasSession(session):
        session.pop("username", None)
        session.pop("student_number", None)
        session.pop("email_address", None)
        session.pop("huidige_vraag", None)
        session.pop("ingevulde_vragen", None)
        # session.pop("punten", None)

def getUsername(session):
    return session["username"]

def setUsername(session, naam):
    session["username"] = naam

def getStudentNumber(session):
    return session["student_number"]

def setStudentNumber(session, naam):
    session["student_number"] = naam

def getEmailAddress(session):
    return session["email_address"]

def setEmailAddress(session, naam):
    session["email_address"] = naam

def getHuidigeVraag(session):
    return int(session["huidige_vraag"])

def setHuidigeVraag(session, vraag: int):
    session["huidige_vraag"] = vraag

def getIngevuldeVragen(session):
    return list(session["ingevulde_vragen"])

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
