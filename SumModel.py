from CalcModel import CalcModel


class SumModel(CalcModel):
    def __init__(self):
        pass

    # do_it
    def result(self):
        return self.x + self.y

    def setX(self, value):
        self.x = value

    def setY(self, value):
        self.y = value
