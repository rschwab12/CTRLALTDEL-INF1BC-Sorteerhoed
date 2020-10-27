import mysql.connector

def setup():
    mydb = mysql.connector.connect(
        host="51.195.90.173",
        user="sorteerhoed",
        password="wbN8Xw3&Fgt3F6!",
        database="sorteerhoed"
    )

    return mydb


def laad_vragen(conn):
    mycursor = conn.cursor(dictionary=True)
    try:
        mycursor.execute("SELECT * FROM questions")
    except:
        print('sorry but it looks like we cant fetch from the database')

    myresult = mycursor.fetchall()

    Questions = {}
    Rotation = 0
    
    
    for row in myresult:
        Rotation += 1
        try:
            Questions.update({Rotation:{ 
                                "vraag":row['text'], 
                                "antwoorden": {}}}) 
        except:
            Questions.update({Rotation:{ 
                                "vraag":'CantFetch', 
                                "antwoorden": {}}}) 

    return Questions    
    
    
def set_ans(conn, Base): #supposed to run with laad_vragen()
    try:
        Questions = dict(Base)
    except:
        print('looks like we didnt recieve a correct variable chief')
     
    mycursor = conn.cursor(dictionary=True)
    
    
    
    for Instance in Questions:
        Query = "SELECT * FROM answers WHERE questionId=" + str(Instance) + " ORDER BY answerId"
        try:
            mycursor.execute(Query) #Try emptying the database again
        except:
            print('sorry but it looks like we cant fetch from the database')
        myresult = mycursor.fetchall()
        try:
            for Var2 in myresult:
                pos = int(Var2['position'])
                Letter = chr(pos + 96)
                
                
                Questions[Instance]['antwoorden'].update({pos: {'letter':Letter, 'antwoord':Var2['text'], 'punten': {'FICT': Var2['fict'], 'SE': Var2['se'], 'BDM': Var2['bdam'], 'IAT': Var2['iat']}}}) 
                
                
        except Exception as a:
            print('het werkte niet...')
            print(a)
    return Questions

def insert_vragenlijst(username, score):
    # score = {fict=0, bdam=3} etc
    return

def get_punten_voor_spec(vraag, antwoord, conn):
    mycursor = conn.cursor(dictionary=True)
    #Query = f"SELECT `fict`,`iat`,`bdam`,`se` FROM answers WHERE `questionId` = 2 AND `position` = 2"
    Query = f"SELECT `fict`,`iat`,`bdam`,`se` FROM answers WHERE `questionId` = {vraag} AND `position` = {antwoord}"
    try:
        mycursor.execute(Query)
    except:
        print('sorry but it looks like we cant fetch from the database')
    myresult = mycursor.fetchall()
    return myresult