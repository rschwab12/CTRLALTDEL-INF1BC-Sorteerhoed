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
    
    try:
        for row in myresult:
            Rotation += 1
            Questions.update({Rotation: {"vraag":row['text'], 
                                        "antwoord": {
                                            1:{"FICT": 0, "SE": 0, "BDM": 0, "IAT": 0},
                                            2:{"FICT": 0, "SE": 0, "BDM": 0, "IAT": 0},
                                            3:{"FICT": 0, "SE": 0, "BDM": 0, "IAT": 0},
            }}}) 
            
    return Questions
    
    except:
        print('we cant make that dictionary right now :(')
        
    
    
#def set_ans(Base): #supposed to run with laad_vragen()
 #   try:
  #      Questions = dict(Base)
   # except:
    #    print('looks like we didnt recieve a correct variable chief')
     #
#    mycursor = conn.cursor(dictionary=True)
 #   
  #  try:
   #     mycursor.execute("SELECT * FROM questions") #Try emptying the database again
    #except:
#        print('sorry but it looks like we cant fetch from the database')
 #       
  #  myresult = mycursor.fetchall()

def insert_vragenlijst(username, score):
    # score = {fict=0, bdam=3} etc
    return
