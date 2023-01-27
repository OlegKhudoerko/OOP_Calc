class MultController:

    def __init__(self, view, multModel):
        self.view = None
        self.multModel = None

        self.view = view
        self.multModel = multModel

    def Mult(self):
        a = self.view.getValue()
        b = self.view.getValue()
        self.multModel.setX(a)
        self.multModel.setY(b)
        result = self.multModel.result()
        self.view.print(result, "Произведение: ")  # вывод msg(...)
