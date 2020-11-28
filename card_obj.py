class CardObj:
    def __init__(self, id, cardNum, secNum, endDate,idUser=0 ):
        self.id = id
        self.idUser = idUser
        self.secNum = secNum
        self.endDate= endDate
        self.cardNum = cardNum
