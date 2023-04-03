from project import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    INCREMENT = 2

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):

        if self.speed + self.INCREMENT > self.MAX_SPEED:
            self.speed = self.MAX_SPEED
        else:
            self.speed += self.INCREMENT