from typing import List

from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *args: Player):
        added_players = []
        for player in args:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player)
        return f"Successfully added: {', '.join(pl.name for pl in added_players)}"

    def add_supply(self, *args: Supply):
        for s in args:
            self.supplies.append(s)

    def sustain(self, player_name: str, sustenance_type: str):
        # current_supply = [s for s in self.supplies if s.name == sustenance_type][-1]
        # try:
        #     user = [p for p in self.players if p.name == player_name][0]
        # except IndexError:
        pass

    def duel(self, first_player_name: str, second_player_name: str):
        pass

    def next_day(self):
        pass

    def __str__(self):
        pass
