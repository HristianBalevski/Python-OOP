from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.stolen import Stolen
from project.delicacies.gingerbread import Gingerbread


class ChristmasPastryShopApp:
    VALID_TYPES_DELICACY = ("Gingerbread", "Stolen")
    VALID_TYPES_BOOTHS = ("Open Booth", "Private Booth")

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        for delicacy in self.delicacies:
            if delicacy.name == name:
                raise Exception(f"{name} already exists!")

        if type_delicacy not in self.VALID_TYPES_DELICACY:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        if type_delicacy == 'Gingerbread':
            product = Gingerbread(name, price)
            self.delicacies.append(product)
        elif type_delicacy == 'Stolen':
            product = Stolen(name, price)
            self.delicacies.append(product)

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.VALID_TYPES_BOOTHS:
            raise Exception(f"{type_booth} is not a valid booth!")

        if type_booth == "Open Booth":
            obj = OpenBooth(booth_number, capacity)
            self.booths.append(obj)

        if type_booth == "Private Booth":
            obj = PrivateBooth(booth_number, capacity)
            self.booths.append(obj)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                booth.is_reserved = True
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                break
        else:
            raise Exception(f"Could not find booth {booth_number}!")

        for delicacy in self.delicacies:
            if delicacy.name == delicacy_name:
                booth.delicacy_orders.append(delicacy)
                return f"Booth {booth_number} ordered {delicacy_name}."
        else:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

    def leave_booth(self, booth_number: int):

        for booth in self.booths:
            if booth.booth_number == booth_number:
                bill = booth.price_for_reservation + sum([p.price for p in booth.delicacy_orders])
                booth.delicacy_orders = []
                booth.price_for_reservation = 0
                booth.is_reserved = False
                self.income += bill

                return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."





