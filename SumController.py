class SumController:

    def __init__(self, view, model):
        self.view = None
        self.model = None

        self.view = view
        self.model = model

    def Sum(self):
        a = self.view.getValue(self)
        b = self.view.getValue()
        self.model.setX(a)
        self.model.setY(b)
        result = self.model.result()
        self.view.print(result, "Сумма: ")  # вывод msg(...)
