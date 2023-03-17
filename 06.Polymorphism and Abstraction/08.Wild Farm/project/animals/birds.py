from project.animals.animal import Bird


class Owl(Bird):
    def make_sound(self):
        return 'Hoot Hoot'

    @property
    def allowed_food(self):
        return ['Meat']

    @property
    def add_weight(self):
        return 0.25


class Hen(Bird):
    def make_sound(self):
        return 'Cluck'

    @property
    def add_weight(self):
        return 0.35

    @property
    def allowed_food(self):
        return ['Vegetable', 'Fruit', 'Meat', 'Seed']
