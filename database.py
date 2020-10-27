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
    
    
    
    for Var1 in Questions:
        MyComm = "SELECT * FROM answers WHERE questionId=" + str(Var1) + " ORDER BY answerId"
        try:
            mycursor.execute(MyComm) #Try emptying the database again
        except:
            print('sorry but it looks like we cant fetch from the database')
        myresult = mycursor.fetchall()
        try:
            for Var2 in myresult:
                #Letter = chr(Var1 + 96)
                Letter = 'Z'
                Questions[Var1]['antwoorden'].update({'letter':'z', 'antwoord':Var2['text'], 'punten': {'FICT': Var2['fict'], 'SE': Var2['se'], 'BDM': Var2['bdam'], 'IAT': Var2['iat']}}) 
                
                
        except Exception as a:
            print('het werkte niet...')
            print(a)
        
    return Questions

def insert_vragenlijst(username, score):
    # score = {fict=0, bdam=3} etc
    return
