from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply


class Controller:
    VALID_TYPES = {
        'Food': Food,
        'Drink': Drink
    }

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        players_added_now = []
        for player in args:
            if player not in self.players:
                self.players.append(player)
                players_added_now.append(player)
        return f"Successfully added: {', '.join([p.name for p in players_added_now])}"

    def add_supply(self, *args):
        for obj in args:
            self.supplies.append(obj)

    def sustain(self, player_name: str, sustenance_type: str):
        there_is_foods_left = [p.name for p in self.supplies if p.__class__.__name__ == 'Food']
        there_is_drinks_left = [p.name for p in self.supplies if p.__class__.__name__ == 'Drink']

        if sustenance_type == 'Food' and not there_is_foods_left:
            raise Exception("There are no food supplies left!")

        if sustenance_type == 'Drink' and not there_is_drinks_left:
            raise Exception("There are no drink supplies left!")

        for player in self.players:
            if player.name == player_name and sustenance_type in Controller.VALID_TYPES:

                if player.stamina == 100:
                    return f"{player_name} have enough stamina."

                for index in range(len(self.supplies) - 1, -1, -1):
                    supply = self.supplies[index]
                    if supply.__class__.__name__ == sustenance_type:
                        if player.stamina + supply.energy > 100:
                            player.stamina = 100
                        else:
                            player.stamina += supply.energy

                        self.supplies.pop(index)

                        return f"{player_name} sustained successfully with {supply.name}."
                #
                # for index in range(len(self.supplies) - 1, -1, -1):
                #     product = self.supplies[index]
                #     if product.__class__.__name__ == 'Drink':
                #         if player.stamina + product.energy > 100:
                #             player.stamina = 100
                #         else:
                #             player.stamina += product.energy
                #
                #     elif product.__class__.__name__ == 'Food':
                #         if player.stamina + product.energy > 100:
                #             player.stamina = 100
                #         else:
                #             player.stamina += product.energy
                #     del self.supplies[index]
                #
                #     return f"{player_name} sustained successfully with {product.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player_one = [p for p in self.players if p.name == first_player_name][0]
        second_player = [p for p in self.players if p.name == second_player_name][0]

        if player_one.stamina == 0 and second_player.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina.\n" \
                   f"Player {second_player_name} does not have enough stamina."

        if player_one.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."

        if second_player.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."

        if player_one.stamina > second_player.stamina:
            player_one.stamina -= second_player.stamina / 2

            if player_one.stamina <= 0:
                player_one.stamina = 0
                return f"Winner: {second_player_name}"

        if player_one.stamina < second_player.stamina:
            second_player.stamina -= player_one.stamina / 2

            if second_player.stamina <= 0:
                second_player.stamina = 0
                return f"Winner: {first_player_name}"

        if player_one.stamina > second_player.stamina:
            return f"Winner: {first_player_name}"
        else:
            return f"Winner: {second_player_name}"

    def next_day(self):
        for player in self.players:
            stamina_to_decrease = player.age * 2
            if player.stamina - stamina_to_decrease < 0:
                player.stamina = 0
            else:
                player.stamina -= stamina_to_decrease
        for player in self.players:
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        players_info = ''
        food_info = []

        for player in self.players:
            players_info += player.__str__() + '\n'

        for supply in self.supplies:
            food_info.append(supply.details())

        return players_info + '\n'.join(food_info)






