from project.car.car import Car


class MuscleCar(Car):
    MINIMUM_SPEED = 250
    MAXIMUM_SPEED = 450

    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if value < self.MINIMUM_SPEED or value > self.MAXIMUM_SPEED:
            raise ValueError(f"Invalid speed limit! Must be between {self.MINIMUM_SPEED} and {self.MAXIMUM_SPEED}!")
        self.__speed_limit = value