from Menu import Menu


class Presenter:

    def __init__(self, sumController, subController, divController, multController, scanner, menu):

        self.sumController = None
        self.subController = None
        self.divController = None
        self.multController = None
        self.menu = None
        self.scanner = None

        self.sumController = sumController
        self.subController = subController
        self.divController = divController
        self.multController = multController
        self.scanner = scanner
        self.menu = Menu.selectFunctions(self)

    def start(self):

        while True:
            if self.menu == "1":
                print(self.menu)
                self.sumController.Sum()
            elif self.menu == "2":
                print(self.menu)
                self.subController.Sub()
            elif self.menu == "3":
                print(self.menu)
                self.divController.Div()
            elif self.menu == "4":
                self.multController.Mult()
            elif self.menu == "0":
                break
            else:
                break
                # print("Неверный ввод")
