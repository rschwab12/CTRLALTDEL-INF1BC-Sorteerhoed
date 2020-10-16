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

    mycursor.execute("SELECT * FROM questions")

    myresult = mycursor.fetchall()

    Questions = {}
    Rotation = 0

    #for x in myresult:
     #   Rotation += 1
      #  Questions.update({Rotation: {"vraag": }}) 
       # 
    #return Questions
    
    for row in myresult:
        print(row['text'])
    
    
    

def insert_vragenlijst(username, score):
    # score = {fict=0, bdam=3} etc
    return

# etc etc
