import random

class User(object):
    def __init__(self, name):
        self.name = name
        self.pokemon = []
        self.attacking_pokemon = None

    def set_pokemon(self, set_of_pokemon):
        self.pokemon = set_of_pokemon

    def list_pokemon(self):
        pass

    def switch(self, pokemon_number):
        pass

    def heal(self):
        pass

    def is_end_game(self):
        pass

    def print_attacks(self):
        pass

    def attack(self, attack_name, enemy):
        pass

class Computer(User):
    def play_turn(self, enemy):
        pass

    def set_pokemon(self, list_pokemon):
        pass

    def attack(self, enemy):
        pass

    def switch(self):
        pass

class Pokemon(object):
    def __init__(self, hp, max_ap, name):
        self.hp = hp
        self.max_ap = max_ap
        self.name = name
        self.knocked_out = False
        self.attacks = self.set_attacks()
        self.pokemon_type = self.set_type()

    def set_type(self):
        return None

    def set_attacks(self):
        self.attacks = {}

    def get_attacks(self):
        return list(self.attacks.keys())

    def print_attacks(self):
        for attack in self.attacks:
            print(attack)

    def add_attacks(self, attack_dictionary):
        self.attacks = attack_dictionary

    def get_attack_power(self, attack, enemy):
        pass

    def attack(self, attack_name, enemy):
        pass

    def take_damage(self, damage_amount):
        pass

    def heal(self):
        pass

class GrassType(Pokemon):
    def set_type(self):
        return 'grass'

    def set_attacks(self):
        pass

    def get_attack_power(self, attack, enemy):
        pass

class WaterType(Pokemon):
    def set_attacks(self):
        pass

    def set_type(self):
        return 'water'

    def get_attack_power(self, attack, enemy):
        pass

class FireType(Pokemon):
    def set_type(self):
        return 'fire'

    def set_attacks(self):
        pass

    def get_attack_power(self, attack, enemy):
        pass
    
def game_loop():
    pokemon_list = [
        GrassType(60, 40, 'Bulbasoar'),
        GrassType(40, 60, 'Bellsprout'),
        GrassType(50, 50, 'Oddish'),
        FireType(25, 70, 'Charmainder'),
        FireType(30, 50, 'Ninetails'),
        FireType(40, 60, 'Ponyta'),
        WaterType(80, 20, 'Squirtle'),
        WaterType(70, 40, 'Psyduck'),
        WaterType(50, 50, 'Polywag')]

    game_over = False

    while not game_over:
        print_stats(player)
        print_stats(computer)

game_loop()
