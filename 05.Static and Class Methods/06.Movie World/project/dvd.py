from calendar import month_name


class DVD:
    def __init__(self, name, number_id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = number_id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, number_id: int, name: str, date: str, age_restriction: int):
        day, month, year = [int(num) for num in date.split('.')]

        return cls(name, number_id, year, month_name[month], age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction " \
               f"{self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"