class DivController:

    def __init__(self, view, divModel):
        self.view = None
        self.divModel = None

        self.view = view
        self.divModel = divModel

    def Div(self):
        a = self.view.getValue()
        b = self.view.getValueDiv()
        self.divModel.setX(a)
        self.divModel.setY(b)
        result = self.divModel.result()
        self.view.print(result, "Частное: ")  # вывод msg(...)
