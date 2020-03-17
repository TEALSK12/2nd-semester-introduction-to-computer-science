import random

class Pokemon(object):
    def __init__(self, name, health_points, attack_power_upper_range, attack_power_lower_range):
        self.name = name
        self.health_points = health_points
        self.attack_power_lower_range = attack_power_lower_range
        self.attack_power_upper_range = attack_power_upper_range

    def attack(self):
        return  random.randint(self.attack_power_lower_range, self.attack_power_upper_range)

    def defend(self, enemy, attack_power):
        self.health_points -= attack_power

    def growl(self):
        print("Growl")

