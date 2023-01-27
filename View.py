class View:
    View = None

    def __init__(self):

        self.in_ = int(input())

    def getValue(self):
        print("Введите число: ")
        val = None
        self.in_ = int(input())
        if self.in_.hasNextInt():
            val = self.in_.nextInt()
        else:
            print("Не допустимое значение, попробуйте еще раз: ")
            self.in_.next()
            val = self.getValue()
        return val

    def getValueDiv(self):
        print("Введите следующее число, не равное нулю: ")
        val = None
        if self.in_.hasNextInt():
            val = self.in_.nextInt()
            if val == 0:
                print("На ноль делить нельзя, введите следующее число: ")
                val = self.getValue()
        else:
            print("Не допустимое значение, введите следующее число: ")
            self.in_.next()
            val = self.getValue()
        return val

    def print(self, data, title):
        print("{0} {1:d}\n".format(title, data), end='')

    @classmethod
    def Menu(cls, scanner):
        pass
