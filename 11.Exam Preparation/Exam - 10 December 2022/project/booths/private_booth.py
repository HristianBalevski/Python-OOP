from project.booths.booth import Booth


class PrivateBooth(Booth):
    PRICE_FOR_RESERVATION = 3.50

    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):

        self.price_for_reservation = self.PRICE_FOR_RESERVATION * number_of_people
        self.is_reserved = True