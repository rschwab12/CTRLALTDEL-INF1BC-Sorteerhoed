import mysql.connector
import os

def setup():
    import configparser

    # Setting up the connection with database
    folder = os.path.dirname(os.path.abspath(__file__))
    configfile = os.path.join(folder, 'config.ini')
    config = configparser.RawConfigParser()
    config.read(configfile)
    mydb = mysql.connector.connect(
        host=config.get('MYSQL', 'host'),
        port=config.get('MYSQL', 'port'),
        user=config.get('MYSQL', 'username'),
        password=config.get('MYSQL', 'password'),
        database=config.get('MYSQL', 'database')
    )

    return mydb


def laad_vragen(conn):
    # Loading questions from the database
    mycursor = conn.cursor(dictionary=True)
    try:
        mycursor.execute("SELECT * FROM questions")
    except:
        print('Unable to fetch from the database')

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
        print('Looks like we didnt recieve a correct variable chief')

    mycursor = conn.cursor(dictionary=True)



    for Instance in Questions:
        Query = "SELECT * FROM answers WHERE questionId=" + str(Instance) + " ORDER BY position"
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
