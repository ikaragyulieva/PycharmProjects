from project.player import Player
from typing import List


class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player) -> str:

        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for current_player in self.players:
            if player_name == current_player.name:
                self.players.remove(current_player)
                current_player.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        # result = [f"Guild: {self.name}"]
        # for detail in self.players:
        #     result.append(f"{detail.player_info()}")
        # return '\n'.join(result)

        # Solution with comprehension:
        return '\n'.join([f"Guild: {self.name}"] + [f"{detail.player_info()}" for detail in self.players])

player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
