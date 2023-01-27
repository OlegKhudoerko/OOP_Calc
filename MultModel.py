from CalcModel import CalcModel


class MultModel(CalcModel):

    def __init__(self):
        pass

    def result(self):
        return self.x * self.y

    def setX(self, value):
        self.x = value

    def setY(self, value):
        self.y = value
