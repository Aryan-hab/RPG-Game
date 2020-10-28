import random
from Classes.magic import Spell


class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic", "Items"]

    def generate_dmg(self):
        return random.randrange(self.atkl, self.atkh)

    def heal(self, dmg):
        self.hp += dmg
        if self.hp < self.maxhp:
            self.hp = self.maxhp

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_max_mp(self):
        return self.maxmp

    def get_mp(self):
        return self.mp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        for item in self.actions:
            print(str(i) + ':', item)
            i += 1

    def action_name(self, i):
        return self.actions[i]

    def choose_magic(self):
        i = 1
        for spell in self.magic:
            print(str(i) + ':', spell.name, ('cost:', str(spell.cost) + ')'))
            i += 1





