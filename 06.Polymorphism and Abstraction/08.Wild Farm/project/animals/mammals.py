from abc import ABC
from project.animals.animal import Mammal


class Mouse(Mammal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"
    
    @property
    def allowed_food(self):
        return ['Vegetable', 'Fruit']

    @property
    def add_weight(self):
        return 0.10


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"
    
    @property
    def allowed_food(self):
        return ['Meat']
    
    @property
    def add_weight(self):
        return 0.40


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def allowed_food(self):
        return ['Meat', 'Vegetable']

    def make_sound(self):
        return "Meow"

    @property
    def add_weight(self):
        return 0.30


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    @property
    def allowed_food(self):
        return ['Meat']

    @property
    def add_weight(self):
        return 1