class Bug:
    def __init__(self, initialPosition):
        self.position = initialPosition
        self.direction = 1 

    def turn(self):
        self.direction *= -1 

    def move(self):
        self.position += self.direction 

    def getPosition(self):
        return self.position


bugsy = Bug(10)
print("Initial position:", bugsy.getPosition())

bugsy.move()
print("After move:", bugsy.getPosition())

bugsy.turn()
bugsy.move()
print("After turning and move:", bugsy.getPosition())
