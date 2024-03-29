from project import Jockey
from project import HorseRace
from project import Appaloosa
from project import Thoroughbred


class HorseRaceApp:

    VALID_TYPES_OF_HORSE_BREEDS = {
        'Appaloosa': Appaloosa,
        'Thoroughbred': Thoroughbred
    }

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        horse = [h for h in self.horses if h.name == horse_name]

        if horse:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.VALID_TYPES_OF_HORSE_BREEDS:
            horse = self.VALID_TYPES_OF_HORSE_BREEDS[horse_type](horse_name, horse_speed)
            self.horses.append(horse)

            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        jockey = [j for j in self.jockeys if j.name == jockey_name]

        if jockey:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        horse_race = [hr for hr in self.horse_races if hr.race_type == race_type]

        if horse_race:
            raise Exception(f"Race {race_type} has been already created!")

        horse_race = HorseRace(race_type)
        self.horse_races.append(horse_race)

        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))
        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        try:
            horse = list(filter(lambda h: h.__class__.__name__ == horse_type and not h.is_taken, self.horses))[-1]
        except IndexError:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."
        else:
            jockey.horse = horse
            horse.is_taken = True
            return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        try:
            horse_race = next(filter(lambda hr: hr.race_type == race_type, self.horse_races))
        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))
        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(jockey)

        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        try:
            horse_race = next(filter(lambda hr: hr.race_type == race_type, self.horse_races))
        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        highest_speed = 0
        jockey_name = ''
        horse_name = ''

        for jockey in horse_race.jockeys:
            if jockey.horse.speed > highest_speed:
                highest_speed = jockey.horse.speed
                jockey_name = jockey.name
                horse_name = jockey.horse.name

        return f"The winner of the {race_type} race, with a speed of {highest_speed}km/h is {jockey_name}" \
               f"! Winner's horse: {horse_name}."
