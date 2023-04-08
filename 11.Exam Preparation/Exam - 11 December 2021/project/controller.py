from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    VALID_TYPES_CARS = {
        "MuscleCar": MuscleCar,
        "SportsCar": SportsCar
    }

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def __check_if_driver_exist(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver
        return False

    def __check_if_the_race_exist(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race
        return False

    def create_car(self, car_type: str, model: str, speed_limit: int):
        for car in self.cars:
            if car.model == model:
                raise Exception(f"Car {model} is already created!")

        if car_type in self.VALID_TYPES_CARS:
            new_car = self.VALID_TYPES_CARS[car_type](model, speed_limit)
            self.cars.append(new_car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if self.__check_if_driver_exist(driver_name):
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        if not self.__check_if_driver_exist(driver_name):
            raise Exception(f"Driver {driver_name} could not be found!")

        if car_type in self.VALID_TYPES_CARS:

            current_car = ''

            for car in reversed(self.cars):
                if not car.is_taken and car.__class__.__name__ == car_type:
                    current_car = car
                    break

            if current_car == '':
                raise Exception(f"Car {car_type} could not be found!")
            else:
                driver = self.__check_if_driver_exist(driver_name)
                if driver.car is None:
                    driver.car = current_car
                    current_car.is_taken = True
                    return f"Driver {driver_name} chose the car {current_car.model}."
                else:
                    old_car_model = driver.car.model
                    driver.car.is_taken = False
                    driver.car = current_car
                    current_car.is_taken = True
                    return f"Driver {driver_name} changed his car from {old_car_model} to {current_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        if not self.__check_if_the_race_exist(race_name):
            raise Exception(F"Race {race_name} could not be found!")

        if not self.__check_if_driver_exist(driver_name):
            raise Exception(f"Driver {driver_name} could not be found!")

        driver = self.__check_if_driver_exist(driver_name)
        race = self.__check_if_the_race_exist(race_name)

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        elif driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."
        else:
            race.drivers.append(driver)
            return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        if not self.__check_if_the_race_exist(race_name):
            raise Exception(f"Race {race_name} could not be found!")

        race = self.__check_if_the_race_exist(race_name)

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        finalists = {}

        for driver in race.drivers:
            finalists[driver] = driver.car.speed_limit

        last_three = {}
        sort_result = dict(sorted(finalists.items(), key=lambda kv: kv[1], reverse=True))

        for key, value in sort_result.items():
            key.number_of_wins += 1
            last_three[key] = value

            if len(last_three) == 3:
                break
        output = []
        for member, speed in last_three.items():
            output.append(f"Driver {member.name} wins the {race_name} race with a speed of {speed}.")

        return '\n'.join(output)
















