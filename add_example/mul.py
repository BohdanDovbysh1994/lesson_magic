class Mul:
    def __init__(self, speed, strength):
        self.speed = speed
        self.strength = strength

    def __str__(self):
        return f'{self.__class__.__name__}\n\t{{\n\t"speed": {self.speed}\n\t"strength": {self.strength}\n\t}}'
