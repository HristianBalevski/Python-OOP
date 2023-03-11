from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = self.find_by_id(self.subscriptions, subscription_id)
        customer = self.find_by_id(self.customers, subscription.customer_id)
        trainer = self.find_by_id(self.trainers, subscription.trainer_id)
        plan = self.find_by_id(self.plans, subscription.exercise_id)
        equipment = self.find_by_id(self.equipment, plan.equipment_id)

        return f'{repr(subscription)}' + '\n' + f'{repr(customer)}' + '\n' \
               f'{repr(trainer)}' + '\n' + f'{repr(equipment)}' + '\n' + f'{repr(plan)}' + '\n'


    def find_by_id(self, collection, object_id):
        for obj in collection:
            if obj.id == object_id:
                return obj




