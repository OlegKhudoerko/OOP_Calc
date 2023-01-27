from MultController import MultController
from DivController import DivController
from SubController import SubController
from SumController import SumController
from MultModel import MultModel
from DivModel import DivModel
from SubModel import SubModel
from SumModel import SumModel
from Menu import Menu
from View import View
import Presenter


class Program:
    @staticmethod
    def main():
        scanner = None
        view = View.View
        menu = Menu
        p = Presenter.Presenter(SumController(view, SumModel()),
                                SubController(view, SubModel()),
                                DivController(view, DivModel()),
                                MultController(view, MultModel()),
                                scanner, menu)

        p.start()

    if __name__ == '__main__':
        main()
