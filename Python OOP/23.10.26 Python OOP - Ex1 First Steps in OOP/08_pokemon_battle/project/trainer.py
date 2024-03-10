from typing import List
from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.pokemons: List[Pokemon] = []
        self.name = name

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str) -> str:
        for p_obj in self.pokemons:
            if pokemon_name == p_obj.name:
                self.pokemons.remove(p_obj)
                return f"You have released {pokemon_name}"

        return f"Pokemon is not caught"

    def trainer_data(self) -> str:
        result = ''
        result += f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}"
        for p in self.pokemons:
            result += f"\n- {p.pokemon_details()}"
        return result


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())

