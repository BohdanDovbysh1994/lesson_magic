from add_example.mul import Mul


class Horse:
    def __init__(self):
        self.speed = 100
        self.age = 5

    def __add__(self, other):
        return Mul(self.speed, other.strength)

    def __radd__(self, other):
        return Mul(self.speed, other.strength)

    def __iadd__(self, other):
        return Mul(self.speed, other.strength)
