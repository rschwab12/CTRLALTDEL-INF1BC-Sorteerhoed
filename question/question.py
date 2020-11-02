from .answer import *

class Question:
    def __init__(self, dict: dict, id: int):
        self.dict = dict
        self.id = id

        self.vraag = dict[self.id]["vraag"]
        self.antwoorden = []

        antwoorden_dict = dict[self.id]["antwoorden"]
        for antwoord in antwoorden_dict:
            answer = Answer(antwoorden_dict, int(antwoord))
            self.antwoorden.append(answer)

    def getID(self):
        return self.id

    def getVraag(self):
        return self.vraag

    def getAntwoorden(self):
        return list(self.antwoorden)

    def getAntwoordByID(self, id: int):
        for antwoord in self.antwoorden:
            if antwoord.getID() == id:
                return antwoord

    def getPunten(self, specialisatie):
        points = 0
        for antwoord in self.antwoorden:
            points += antwoord.getPunten(specialisatie)
        return points
