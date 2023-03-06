from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity and self.__budget >= price:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if len(self.animals) < self.__animal_capacity and self.__budget < price:
            return "Not enough budget"

        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        else:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        needed_money = 0

        for worker in self.workers:
            needed_money += worker.salary

        if self.__budget >= needed_money:
            self.__budget -= needed_money
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        needed_money = 0

        for animal in self.animals:
            needed_money += animal.money_for_care

        if self.__budget >= needed_money:
            self.__budget -= needed_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        output = f'You have {len(self.animals)} animals\n'
        lions_info = [repr(lion) for lion in self.animals if isinstance(lion, Lion)]
        tigers_info = [repr(tiger) for tiger in self.animals if isinstance(tiger, Tiger)]
        cheetahs_info = [repr(cheetah) for cheetah in self.animals if isinstance(cheetah, Cheetah)]
        output += f'----- {len(lions_info)} Lions:\n' + '\n'.join(lions_info) + '\n'\
                  f'----- {len(tigers_info)} Tigers:\n' + '\n'.join(tigers_info) + '\n'\
                  f'----- {len(cheetahs_info)} Cheetahs:\n' + '\n'.join(cheetahs_info).strip()

        return output

    def workers_status(self):
        output = f'You have {len(self.workers)} workers\n'
        keepers_info = [repr(person) for person in self.workers if isinstance(person, Keeper)]
        caretakers_info = [repr(person) for person in self.workers if isinstance(person, Caretaker)]
        vets_info = [repr(person) for person in self.workers if isinstance(person, Vet)]

        output += f'----- {len(keepers_info)} Keepers:\n' + '\n'.join(keepers_info) + '\n' \
                  f'----- {len(caretakers_info)} Caretakers:\n' + '\n'.join(caretakers_info) + '\n' \
                  f'----- {len(vets_info)} Vets:\n' + '\n'.join(vets_info)
        return output



