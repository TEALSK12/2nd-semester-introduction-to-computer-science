import random

class User(object):
    def __init__(self, name):
        self.name = name
        self.pokemon = []
        self.attacking_pokemon = None

    def set_pokemon(self, set_of_pokemon):
        self.pokemon = set_of_pokemon

    def list_pokemon(self):
        for i in range(0, len(self.pokemon)):
            print("Pokemon #" + str(i) + ", " + self.pokemon[i].name)

    def switch(self, pokemon_number):
        pokemon_to_set = self.pokemon[pokemon_number]
        print(self.name + " is trying to set attacking pokemon to " + pokemon_to_set.name)
        if pokemon_to_set.knocked_out:
            print(pokemon_to_set.name + " is K.O. can't use him.")
        else:
            self.attacking_pokemon = pokemon_to_set

    def heal(self):
        print(self.name + " healed.")
        self.attacking_pokemon.heal()

    def is_end_game(self):
        for pok in self.pokemon:
            if not pok.knocked_out:
                return False
        return True

    def print_attacks(self):
        self.attacking_pokemon.print_attacks()

    def attack(self, attack_name, enemy):
        print(self.name + " is attacking.")
        self.attacking_pokemon.attack(attack_name, enemy)

class Computer(User):
    def play_turn(self, enemy):
        random_turn = random.randint(0, 5)
        if self.attacking_pokemon.knocked_out:
            self.switch()
        elif random_turn < 4:
            self.attack(enemy)
        elif random_turn == 4:
            self.heal()
        elif random_turn == 5:
            self.switch()

    def set_pokemon(self, list_pokemon):
        pokemon_in_hand = []
        while len(pokemon_in_hand) < 3:
            random_pokemon = list_pokemon[random.randint(0, len(list_pokemon)-1)]
            if random_pokemon not in pokemon_in_hand:
                pokemon_in_hand.append(random_pokemon)
        self.pokemon = pokemon_in_hand

    def attack(self, enemy):
        attack_name_list = self.attacking_pokemon.get_attacks()
        random_attack = random.randint(0, len(attack_name_list)-1)
        print(self.name + " is attacking.")
        self.attacking_pokemon.attack(attack_name_list[random_attack], enemy)

    def switch(self):
        if self.is_end_game():
            return
        pokemon_number = random.randint(0, len(self.pokemon)-1)
        pokemon_to_set = self.pokemon[pokemon_number]
        while pokemon_to_set.knocked_out:
            pokemon_number = random.randint(0, len(self.pokemon)-1)
            pokemon_to_set = self.pokemon[pokemon_number]
        print(self.name + " is trying to set attacking pokemon to " + pokemon_to_set.name)
        self.attacking_pokemon = pokemon_to_set

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

    def get_attack_power(self, attack, enemy):
        attack_max_power = attack[0]
        attack_accuracy = attack[1]
        if attack_max_power > self.max_ap:
            attack_max_power = self.max_ap
        attack_power = random.randint(attack_max_power-20, attack_max_power)
        return attack_power

    def attack(self, attack_name, enemy):
        attack = self.attacks[attack_name]
        attack_power = self.get_attack_power(attack, enemy)
        enemy.take_damage(attack_power)
        print(self.name + " used " + attack_name + " and did " + str(attack_power) + " damage")

    def take_damage(self, damage_amount):
        if self.hp < damage_amount:
            self.hp = 0
            self.knocked_out = True
        else:
            self.hp -= damage_amount

    def heal(self):
        if self.hp > 0:
            self.hp += 20
        return

    def add_attacks(self, attack_dictionary):
        self.attacks = attack_dictionary

class GrassType(Pokemon):
    def set_type(self):
        return 'grass'

    def set_attacks(self):
        return {
            'leaf storm': [130, 90],
            'mega drain': [50, 100],
            'razor leaf': [55, 95]
        }

    def get_attack_power(self, attack, enemy):
        attack_max_power = attack[0]
        attack_accuracy = attack[1]
        random_attack = random.randint(0 , 100)
        if random_attack > attack_accuracy:
            return 0
        if attack_max_power > self.max_ap:
            attack_max_power = self.max_ap
        attack_power = random.randint(attack_max_power-20, attack_max_power)
        if enemy.pokemon_type == "fire":
            attack_power *= 1.5
        return attack_power

class WaterType(Pokemon):
    def set_attacks(self):
        return {
            'bubble': [40, 100],
            'hydro pump': [185, 30],
            'surf': [70, 90]
        }

    def set_type(self):
        return 'water'

    def get_attack_power(self, attack, enemy):
        attack_max_power = attack[0]
        attack_accuracy = attack[1]
        random_attack = random.randint(0 , 100)
        if random_attack > attack_accuracy:
            return 0
        if attack_max_power > self.max_ap:
            attack_max_power = self.max_ap
        attack_power = random.randint(attack_max_power-20, attack_max_power)
        if enemy.pokemon_type == "grass":
            attack_power *= 1.5
        return attack_power

class FireType(Pokemon):
    def set_type(self):
        return 'fire'

    def set_attacks(self):
        return {
            'ember': [130, 90],
            'fire punch': [50, 100],
            'flame wheel': [70, 90]
        }

    def get_attack_power(self, attack, enemy):
        attack_max_power = attack[0]
        attack_accuracy = attack[1]
        random_attack = random.randint(0 , 100)
        if random_attack > attack_accuracy:
            return 0
        if attack_max_power > self.max_ap:
            attack_max_power = self.max_ap
        attack_power = random.randint(attack_max_power-20, attack_max_power)
        if enemy.pokemon_type == "water":
            attack_power *= 1.5
        return attack_power

def intro_user_name():
    print("Welcome to pokemon. You will pick 3 pokemons, then choose a pokemon to battle. Once all your pokemon are K.O or your opponents pokemon are K.O the game ends.")
    name = input("What is your name? ")
    return name

def get_user_pokemon_list(pokemon_list):
    print("Pick the numbers of the pokemon you would like on your team")
    for i in range(0, len(pokemon_list)):
        print(str(i) + ". " + pokemon_list[i].name)
    pokemon_in_hand = []
    while len(pokemon_in_hand) < 3:
        user_input = input("What number would you like to choose. You can only have one of each pokemon? ")
        pokemon = pokemon_list[int(user_input)]
        if pokemon not in pokemon_in_hand:
            pokemon_in_hand.append(pokemon)
    for pk in pokemon_in_hand:
        pokemon_list.remove(pk)
    return pokemon_in_hand

def switch(player):
    print("Choose you're attacking pokemon")
    player.list_pokemon()
    pokemon_number = input("What number pokemon would you like? ")
    player.switch(int(pokemon_number))

def print_stats(user):
    if user.attacking_pokemon:
        print("attacking pokemon: " + user.attacking_pokemon.name + ", hp: " + str(user.attacking_pokemon.hp))
    for pok in user.pokemon:
        print("pokemon: " + pok.name + ", hp: " + str(pok.hp))

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

    name = intro_user_name()
    computer_name = input("What is your opponents name? ")
    player = User(name)
    user_pokemon_list = get_user_pokemon_list(pokemon_list)
    player.set_pokemon(user_pokemon_list)
    switch(player)
    computer = Computer(computer_name)
    computer.set_pokemon(pokemon_list)
    computer.switch()

    while not game_over:
        user_input = input("What would you like to do, attack, heal, or switch: ")
        if user_input == "attack":
            player.print_attacks()
            attack_name = input("Which attack would you like to do? ")
            player.attack(attack_name, computer.attacking_pokemon)
        elif user_input == "heal":
            player.heal()
        elif user_input == "switch":
            switch(player)
        computer.play_turn(player.attacking_pokemon)
        if player.is_end_game():
            print(computer.name + " won.")
            game_over = True
        if computer.is_end_game():
            print(player.name + " won.")
            game_over = True
        print_stats(player)
        print_stats(computer)

game_loop()
