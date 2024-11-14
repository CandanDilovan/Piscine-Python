class calculator:
    """a scalar calculator"""
    def __init__(self, vector):
        self.vect = vector

    def __add__(self, object) -> None:
        for a in range(len(self.vect)):
            self.vect[a] += object
        print(self.vect)

    def __mul__(self, object) -> None:
        for a in range(len(self.vect)):
            self.vect[a] *= object
        print(self.vect)

    def __sub__(self, object) -> None:
        for a in range(len(self.vect)):
            self.vect[a] -= object
        print(self.vect)

    def __truediv__(self, object) -> None:
        try:
            for a in range(len(self.vect)):
                self.vect[a] /= object
            print(self.vect)
        except ZeroDivisionError as msg:
            print("Error:", msg)
