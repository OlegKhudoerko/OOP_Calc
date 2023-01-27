import math

from CalcModel import CalcModel


class DivModel(CalcModel):

    def __init__(self):
        pass

    def result(self):
        return math.trunc(self.x / float(self.y))

    def setX(self, value):
        self.x = value

    def setY(self, value):
        self.y = value
