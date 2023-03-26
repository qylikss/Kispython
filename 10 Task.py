class MealyError(Exception):
    pass


class Mealy:
    def __init__(self):
        self.state = 'A'

    def click(self):
        match self.state:
            case 'A':
                self.state = 'B'
                return 0
            case 'C':
                self.state = 'D'
                return 3
            case 'F':
                self.state = 'A'
                return 8
            case _:
                raise MealyError("click")

    def clean(self):
        match self.state:
            case 'B':
                self.state = 'C'
                return 2
            case 'E':
                self.state = 'G'
                return 6
            case _:
                raise MealyError("clean")

    def scan(self):
        match self.state:
            case 'A':
                self.state = 'E'
                return 1
            case 'E':
                self.state = 'F'
                return 5
            case 'D':
                self.state = 'E'
                return 4
            case 'F':
                self.state = 'G'
                return 7
            case 'G':
                self.state = 'A'
                return 9
            case _:
                raise MealyError("scan")


def try_click(obj, state, val=None):
    obj.state = state
    try:
        assert (obj.click() == val)
    except MealyError:
        pass


def try_clean(obj, state, val=None):
    obj.state = state
    try:
        assert (obj.clean() == val)
    except MealyError:
        pass


def try_scan(obj, state, val=None):
    obj.state = state
    try:
        assert (obj.scan() == val)
    except MealyError:
        pass


def test():
    obj = main()
    try_clean(obj, 'A')
    try_click(obj, 'A', 0)
    try_scan(obj, 'A', 1)
    try_click(obj, 'B')
    try_scan(obj, 'B')
    try_clean(obj, 'B', 2)
    try_clean(obj, 'C')
    try_scan(obj, 'C')
    try_click(obj, 'C', 3)
    try_click(obj, 'D')
    try_clean(obj, 'D')
    try_scan(obj, 'D', 4)
    try_click(obj, 'E')
    try_clean(obj, 'E', 6)
    try_scan(obj, 'E', 5)
    try_clean(obj, 'F')
    try_click(obj, 'F', 8)
    try_scan(obj, 'F', 7)
    try_clean(obj, 'G')
    try_click(obj, 'G')
    try_scan(obj, 'G', 9)


def main():
    return Mealy()


test()
