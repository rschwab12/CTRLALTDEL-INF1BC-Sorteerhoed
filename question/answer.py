class Answer:
    def __init__(self, dict: dict, id: int):
        self.dict = dict
        self.id = id

        self.antwoord = dict[self.id]["antwoord"]
        self.punten = dict[self.id]["punten"]

    def getID(self):
        return self.id

    def getTekst(self):
        return self.antwoord

    def getPunten(self, specialisatie):
        return self.punten[specialisatie]
