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
