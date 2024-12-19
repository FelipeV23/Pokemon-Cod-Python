import random
from Pokemon import *

list_names = ["Whitney", "Normando", "Clair", "Íris", "Wallace", "João", "Raihan", "Volkner", "Giovanni", "Leon"]
city_list = ["Kanto", "Johto", "Hoenn", "Sinnoh", "Unova", "Kalos", "Galar", "Paldea", "Pallet"]
pokemons_list = [
    Pokemon_water("Wartortle", "Eletric", "Torrent"),
    Pokemon_water("Blastoise", "Eletric", "Torrent"),
    Pokemon_water("Poliwhirl", "Eletric", "Damp"),
    Pokemon_fire("Growlithe", "Water", "Rock"),
    Pokemon_fire("Charmander", "Water", "Blaze"),
    Pokemon_grass("Bulbasaur", "Fire", "Overgrow"),
    Pokemon_ground("Onix", "Water", "Rock Head"),
    Pokemon_eletric("Pikachu", "Ground", "Thunder Bolt"),
    Pokemon_eletric("Raichu", "Ground", "Static")
]

class personagem:
    def __init__(self, age, city, pokemons=[], name=None,):
        self.age = age
        self.city = city
        self.pokemons = pokemons
        if name:
            self.name = name
        else:
            self.name = random.choice(list_names)

    def __str__(self):
        return (" Character Name: {}, Age: {}, City: {}".format(self.name, self.age, self.city))


    def pokemon_name(self):
        if len(self.pokemons) > 0:
            print("Pokemons {}".format(self.name))
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print("You don't have any pokemons in your pokedex :(, let's capture")


class player(personagem):
    type = "player"
    def capture(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} Capture {} successfully!!".format(self.name, pokemon.specie))

class enemy(personagem):
    type = "enemy"
    def __init__(self, age=None, city=None, pokemons=[], name=None,):
        if not pokemons:
            for i in range(random.randint(1,6)):
                pokemons.append(random.choice(pokemons_list))

        super().__init__(name,pokemons)
        if age:
            self.age = age
        else:
            self.age = random.randint(12,45)
        if city:
            self.city = city
        else:
            self.city = random.choice(city_list)
