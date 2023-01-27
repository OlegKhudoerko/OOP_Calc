class SubController:

    def __init__(self, view, subModel):
        self.view = None
        self.subModel = None

        self.view = view
        self.subModel = subModel

    def Sub(self):
        a = self.view.getValue()
        b = self.view.getValue()
        self.subModel.setX(a)
        self.subModel.setY(b)
        result = self.subModel.result()
        self.view.print(result, "Разность: ")  # вывод msg(...)
