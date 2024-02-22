# import functions needed ver 0.4.4


import os
import time
import random
import sys

screen_width = 100
game_start = False


# player status management / storage

class Player:
    def __init__(self):
        self.name = ""
        self.karma = 0
        self.max_hp = 0
        self.hp = 0
        self.mp = 0
        self.equipped_weapon = ""
        self.inventory = ["test", "test2"]
        self.location = "c5"
        self.game_over = False
        self.type = ""


player1 = Player()


class Enemy:

    def __init__(self):
        self.name = ""
        self.karma = 0
        self.hp = 0
        self.mp = 0
        self.weapon_affinity = []
        self.equipped_weapon = ""
        self.kill_drop = []
        self.locations = ["c5", "d8", "f3", "h2"]
        self.type = ""


enemy1 = Enemy()


# title screen

def title_screen_input():
    option = input("> ")
    if option.lower() == "play":
        setup_game()
    elif option.lower() == "help":
        help_menu()
    elif option.lower() == "quit":
        sys.exit()
    while option.lower() not in ["play", "help", "quit", "11836"]:
        option = input("> ")
        if option.lower() == "play":
            setup_game()
        elif option.lower() == "help":
            help_menu()
        elif option.lower() == "quit":
            sys.exit()
        elif option.lower() == "11836":
            player1.location = "d8"
            player1.name = "Calico"
            player1.type = "Developer"
            player1.hp = 2000
            print_location("map")
            game()


def title_screen():
    os.system("clear")
    print("\n .d88b      db     8b   d8  8888")
    print(" 8P www    dPYb    8YbmdP8  8www")
    print(" 8b  d8   dPwwYb   8  Y  8  8   ")
    print(" `Y88P'  dP    Yb  8     8  8888")
    print("              Adventure         ")
    print("               -Play-           ")
    print("               -Help-           ")
    print("               -quit-           ")
    title_screen_input()


def help_menu():
    print("+-help------------------------------+")
    print("|                                   |")
    print("|                                   |")
    print("|                                   |")
    print("|                                   |")
    print("|                                   |")
    if not game_start:
        print("               -Play-           ")
        print("               -quit-           ")
        title_screen_input()


def stats():
    os.system("clear")
    hp = str(player1.hp)
    name = player1.name
    ty = player1.type
    inventory = player1.inventory
    spacer = (5 * len(name))
    print(f"+{'-' * spacer}+")
    print(f"|{name} the {ty}{' ' * (spacer - len(name + ty + 'the  '))}|")
    print(f"|HP: {hp} {' ' * (spacer - (5 + len(hp)))}|")
    print(f"|---inventory{'-' * (spacer - 12)}|")
    for item in inventory:
        print(f"|{item}{' ' * (spacer - len(item))}|")
    print(f"+{'=' * spacer}+")


# Map
# [a1] [a2]
# [b1] [b2]

ZONENAME = ""
DESCRIPTION = "description"
EXAMINE = "examine"
UP = "up", "north"
DOWN = "down", "south"
LEFT = "left", "west"
RIGHT = "right", "east"

solved_places = {
    "a1": False, "a2": False, "a3": False, "a4": False, "a5": False, "a6": False, "a7": False, "a8": False,
    "b1": False, "b2": False, "b3": False, "b4": False, "b5": False, "b6": False, "b7": False, "b8": False,
    "c1": False, "c2": False, "c3": False, "c4": False, "c5": False, "c6": False, "c7": False, "c8": False,
    "d1": False, "d2": False, "d3": False, "d4": False, "d5": False, "d6": False, "d7": False, "d8": False,
    "e1": False, "e2": False, "e3": False, "e4": False, "e5": False, "e6": False, "e7": False, "e8": False,
    "f1": False, "f2": False, "f3": False, "f4": False, "f5": False, "f6": False, "f7": False, "f8": False,
    "g1": False, "g2": False, "g3": False, "g4": False, "g5": False, "g6": False, "g7": False, "g8": False,
    "h1": False, "h2": False, "h3": False, "h4": False, "h5": False, "h6": False, "h7": False, "h8": False
}

zone_map = {
    "a1": {
        ZONENAME: "Witches hut",
        DESCRIPTION: "The home of a witch",
        EXAMINE: "picture1",
        UP: "a1",
        DOWN: "b1",
        LEFT: "a1",
        RIGHT: "a2",
    },
    "a2": {
        ZONENAME: "swampland",
        DESCRIPTION: "The water is dark and murky here",
        EXAMINE: "your feet sink into the waterlogged ground",
        UP: "a2",
        DOWN: "b2",
        LEFT: "a1",
        RIGHT: "a3",
    },
    "a3": {
        ZONENAME: "swampland",
        DESCRIPTION: "Swamp gas fills the air",
        EXAMINE: ["something seems to be stalking you"],
        UP: "a3",
        DOWN: "b3",
        LEFT: "a2",
        RIGHT: "a4",
    },
    "a4": {
        ZONENAME: "grassland",
        DESCRIPTION: "You're in beautiful sea of golden grass ",
        EXAMINE: "You take a moment to appreciate \nthe natural beauty of the area",
        UP: "a4",
        DOWN: "b4",
        LEFT: "a3",
        RIGHT: "a5",
    },
    "a5": {
        ZONENAME: "grassland",
        DESCRIPTION: " Gazelle graze on the abundant grass",
        EXAMINE: "You hear a snarl from behind you \nyou also remembered lions live in grasslands",
        UP: "a5",
        DOWN: "b5",
        LEFT: "a4",
        RIGHT: "a6",
    },
    "a6": {
        ZONENAME: "grassland",
        DESCRIPTION: "the grass here seems brighter",
        EXAMINE: "you find an old wishing well",
        UP: "a6",
        DOWN: "b6",
        LEFT: "a5",
        RIGHT: "a7",
    },
    "a7": {
        ZONENAME: "grassland",
        DESCRIPTION: "Fields of glorious golden grass",
        EXAMINE: "you find a strange black rock that's warm to the touch \nmaybe its worth something at a trading post",
        UP: "a7",
        DOWN: "b7",
        LEFT: "a6",
        RIGHT: "a8",
    },
    "a8": {
        ZONENAME: "grassland",
        DESCRIPTION: "The field has a path going through it",
        EXAMINE: "The path seems to be heading north to the city of Calico",
        UP: "a8",
        DOWN: "b8",
        LEFT: "a7",
        RIGHT: "a8",
    },
    "b1": {
        ZONENAME: "swampland",
        DESCRIPTION: "A rotten smell fills the air",
        EXAMINE: "the water ripples as something moves towards you",
        UP: "a1",
        DOWN: "c1",
        LEFT: "b1",
        RIGHT: "b2",
    },
    "b2": {
        ZONENAME: "home",
        DESCRIPTION: "This is your house",
        EXAMINE: "Your homes still the same",
        UP: "a2",
        DOWN: "c2",
        LEFT: "b1",
        RIGHT: "b3",
    },
    "b3": {
        ZONENAME: "forest",
        DESCRIPTION: "a forest full of red and yellow autumn trees",
        EXAMINE: "theres not much of interest here",
        UP: "a3",
        DOWN: "c3",
        LEFT: "b2",
        RIGHT: "b4",
    },
    "b4": {
        ZONENAME: "forest",
        DESCRIPTION: 'A forest full of red and yellow autumn trees',
        EXAMINE: "The trees leaves have a beautiful colour",
        UP: "a4",
        DOWN: "c4",
        LEFT: "b3",
        RIGHT: "b5",
    },
    "b5": {
        ZONENAME: "Town entrance",
        DESCRIPTION: "An entrance to the town of Calico",
        EXAMINE: "A wooden bridge leading into town",
        UP: "a5",
        DOWN: "c5",
        LEFT: "b4",
        RIGHT: "b6",
    },
    "b6": {
        ZONENAME: "home",
        DESCRIPTION: "This is your house",
        EXAMINE: "Your homes still the same",
        UP: "a6",
        DOWN: "c6",
        LEFT: "b5",
        RIGHT: "b7",
    },
    "b7": {
        ZONENAME: "forest",
        DESCRIPTION: "a forest full of red and yellow autumn trees",
        EXAMINE: "theres not much of interest here",

        UP: "a7",
        DOWN: "c7",
        LEFT: "b6",
        RIGHT: "b8",
    },
    "b8": {
        ZONENAME: "forest",
        DESCRIPTION: "A forest full of red and yellow autumn trees",
        EXAMINE: "The trees leaves have a beautiful colour",

        UP: "a8",
        DOWN: "c8",
        LEFT: "b7",
        RIGHT: "b8",
    },
    "c1": {
        ZONENAME: "forest",
        DESCRIPTION: "something seems off about this part of the forest ",
        EXAMINE: "upon closer inspection you notice the trees all have a poisonous fungus on them",

        UP: "b1",
        DOWN: "d1",
        LEFT: "c1",
        RIGHT: "c2",
    },
    "c2": {
        ZONENAME: "forest",
        DESCRIPTION: "A red and yellow autumn forest",
        EXAMINE: "the underbrush makes it difficult to walk",
        UP: "b2",
        DOWN: "d2",
        LEFT: "c1",
        RIGHT: "c3",
    },
    "c3": {
        ZONENAME: "deep forest",
        DESCRIPTION: "your very far into the forest",
        EXAMINE: "theres more trees here and fewer trails",
        UP: "b3",
        DOWN: "d3",
        LEFT: "c2",
        RIGHT: "c4",
    },
    "c4": {
        ZONENAME: "dark forest",
        DESCRIPTION: "the forest is noticeably darker",
        EXAMINE: "as you look around a sense of dread creeps in your mind",
        UP: "b4",
        DOWN: "d4",
        LEFT: "c3",
        RIGHT: "c5",
    },
    "c5": {
        ZONENAME: "forest",
        DESCRIPTION: "something seems off about this part of the forest ",
        EXAMINE: "upon closer inspection you notice the trees all have a poisonous fungus on them",
        UP: "b5",
        DOWN: "d5",
        LEFT: "c4",
        RIGHT: "c6",
    },
    "c6": {
        ZONENAME: "forest",
        DESCRIPTION: "A red and yellow autumn forest",
        EXAMINE: "the underbrush makes it difficult to walk",
        UP: "b6",
        DOWN: "d6",
        LEFT: "c5",
        RIGHT: "c7",
    },
    "c7": {
        ZONENAME: "deep forest",
        DESCRIPTION: "your very far into the forest",
        EXAMINE: "theres more trees here and fewer trails",
        UP: "b7",
        DOWN: "d7",
        LEFT: "c6",
        RIGHT: "c8",
    },
    "c8": {
        ZONENAME: "dark forest",
        DESCRIPTION: "the forest is noticeably darker",
        EXAMINE: "as you look around a sense of dread creeps in your mind",
        UP: "b8",
        DOWN: "d8",
        LEFT: "c7",
        RIGHT: "c8",
    },

    "d1": {
        ZONENAME: "Old cabin",
        DESCRIPTION: "it seems abandoned",
        EXAMINE: "the old cabin is in a state of major disrepair",
        UP: "c1",
        DOWN: "e1",
        LEFT: "d1",
        RIGHT: "d2",
    },
    "d2": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is denser here",
        EXAMINE: "the foliage is extremely thick here",
        UP: "c2",
        DOWN: "e2",
        LEFT: "d1",
        RIGHT: "d3",
    },
    "d3": {
        ZONENAME: "dark forest",
        DESCRIPTION: "the sun doesn't make it through the foliage",
        EXAMINE: "the only thing that grows here is mangled trees and thorn bushes",
        UP: "c3",
        DOWN: "e3",
        LEFT: "d2",
        RIGHT: "d4",
    },
    "d4": {
        ZONENAME: "dark place",
        DESCRIPTION: "this is where all the darkness comes from",
        EXAMINE: "this place isn't safe",
        UP: "c4",
        DOWN: "e4",
        LEFT: "d3",
        RIGHT: "d4",
    },
    "d5": {
        ZONENAME: "Old cabin",
        DESCRIPTION: "it seems abandoned",
        EXAMINE: "the old cabin is in a state of major disrepair",
        UP: "c5",
        DOWN: "e5",
        LEFT: "d4",
        RIGHT: "d6",
    },
    "d6": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is denser here",
        EXAMINE: "the foliage is extremely thick here",
        UP: "c6",
        DOWN: "e6",
        LEFT: "d5",
        RIGHT: "d7",
    },
    "d7": {
        ZONENAME: "dark forest",
        DESCRIPTION: "the sun doesn't make it through the foliage",
        EXAMINE: "the only thing that grows here is mangled trees and thorn bushes",
        UP: "c7",
        DOWN: "e7",
        LEFT: "d6",
        RIGHT: "d8",
    },
    "d8": {
        ZONENAME: "dark place",
        DESCRIPTION: "this is where all the darkness comes from",
        EXAMINE: "wolf",
        UP: "c8",
        DOWN: "e8",
        LEFT: "d7",
        RIGHT: "d8",
    },
    "e1": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is denser here",
        EXAMINE: "the ground seems softer",
        UP: "d1",
        DOWN: "f1",
        LEFT: "e1",
        RIGHT: "e2",
    },
    "e2": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is denser here",
        EXAMINE: "the ground seems softer",
        UP: "d2",
        DOWN: "f2",
        LEFT: "e1",
        RIGHT: "e3",
    },
    "e3": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is denser here",
        EXAMINE: "the ground seems softer",
        UP: "d3",
        DOWN: "f3",
        LEFT: "e2",
        RIGHT: "e4",
    },
    "e4": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is denser here",
        EXAMINE: "the ground seems softer",
        UP: "d4",
        DOWN: "f4",
        LEFT: "e3",
        RIGHT: "e5",
    },
    "e5": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is denser here",
        EXAMINE: "the ground seems softer",
        UP: "d5",
        DOWN: "f5",
        LEFT: "e4",
        RIGHT: "e6",
    },
    "e6": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is denser here",
        EXAMINE: "the ground seems softer",
        UP: "d6",
        DOWN: "f6",
        LEFT: "e5",
        RIGHT: "e7",
    },
    "e7": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is denser here",
        EXAMINE: "the ground seems softer",
        UP: "d7",
        DOWN: "f7",
        LEFT: "e6",
        RIGHT: "e8",
    },
    "e8": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is denser here",
        EXAMINE: "the ground seems softer",
        UP: "d8",
        DOWN: "f8",
        LEFT: "e7",
        RIGHT: "e8",
    },
    "f1": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is denser here",
        EXAMINE: "the ground seems softer",
        UP: "e1",
        DOWN: "g1",
        LEFT: "f1",
        RIGHT: "f2",
    },
    "f2": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is denser here",
        EXAMINE: "the ground seems softer",
        UP: "f2",
        DOWN: "g2",
        LEFT: "f1",
        RIGHT: "f3",
    },
    "f3": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is denser here",
        EXAMINE: "the ground seems softer",
        UP: "e3",
        DOWN: "g3",
        LEFT: "f2",
        RIGHT: "f4",
    },
    "f4": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is denser here",
        EXAMINE: "the ground seems softer",
        UP: "e4",
        DOWN: "g4",
        LEFT: "f3",
        RIGHT: "f5",
    },
    "f5": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is denser here",
        EXAMINE: "the ground seems softer",
        UP: "e5",
        DOWN: "g5",
        LEFT: "f4",
        RIGHT: "f6",
    },
    "f6": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is denser here",
        EXAMINE: "the ground seems softer",
        UP: "e6",
        DOWN: "g6",
        LEFT: "f5",
        RIGHT: "f7",
    },
    "f7": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is denser here",
        EXAMINE: "the ground seems softer",
        UP: "e7",
        DOWN: "g7",
        LEFT: "f6",
        RIGHT: "f8",
    },
    "f8": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is denser here",
        EXAMINE: "the ground seems softer",
        UP: "e8",
        DOWN: "g8",
        LEFT: "f7",
        RIGHT: "f8",
    },
    "g1": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is denser here",
        EXAMINE: "the ground seems softer",
        UP: "f1",
        DOWN: "h1",
        LEFT: "g1",
        RIGHT: "g2",
    },
    "g2": {
        ZONENAME: " deep forest",
        DESCRIPTION: "the foliage is denser here",
        EXAMINE: "the ground seems softer",
        UP: "f2",
        DOWN: "h2",
        LEFT: "g1",
        RIGHT: "g3",
    },
    "g3": {
        ZONENAME: "forest",
        DESCRIPTION: "the trees are dull and grey here",
        EXAMINE: "event1",
        UP: "f3",
        DOWN: "h3",
        LEFT: "g2",
        RIGHT: "g4",
    },
    "g4": {
        ZONENAME: "city bridge",
        DESCRIPTION: "strange engravings line the bridge",
        EXAMINE: "puzzle 2",
        UP: "f4",
        DOWN: "h4",
        LEFT: "g3",
        RIGHT: "g5",
    },
    "g5": {
        ZONENAME: "Hotel",
        DESCRIPTION: "a place for adventurers to rest",
        EXAMINE: "hotel",
        UP: "f5",
        DOWN: "h5",
        LEFT: "g4",
        RIGHT: "g6",
    },
    "g6": {
        ZONENAME: "milk bar",
        DESCRIPTION: "where you can get a drink",
        EXAMINE: "milk bar",
        UP: "f6",
        DOWN: "h6",
        LEFT: "g5",
        RIGHT: "g7",
    },
    "g7": {
        ZONENAME: "ally",
        DESCRIPTION: "shifty eyes watch you",
        EXAMINE: "puzzle1",
        UP: "f7",
        DOWN: "h7",
        LEFT: "g6",
        RIGHT: "g8",
    },
    "g8": {
        ZONENAME: "fighting ring",
        DESCRIPTION: "a place for placing bets or fighting ",
        EXAMINE: "bet",
        UP: "f8",
        DOWN: "h8",
        LEFT: "g7",
        RIGHT: "g8",
    },
    "h1": {
        ZONENAME: "abandoned cabin",
        DESCRIPTION: "it looks ",
        EXAMINE: "item_find_1",
        UP: "g1",
        DOWN: "h1",
        LEFT: "h1",
        RIGHT: "h2",
    },
    "h2": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is denser here",
        EXAMINE: "the ground seems softer",
        UP: "g2",
        DOWN: "h2",
        LEFT: "h1",
        RIGHT: "h3",
    },
    "h3": {
        ZONENAME: "forest",
        DESCRIPTION: "theres a lot of moss here",
        EXAMINE: "collect",
        UP: "g3",
        DOWN: "h3",
        LEFT: "h2",
        RIGHT: "h4",
    },
    "h4": {
        ZONENAME: "city entrance",
        DESCRIPTION: "The entrance to the city of Calico",
        EXAMINE: "the ground seems softer",
        UP: "g4",
        DOWN: "h4",
        LEFT: "h3",
        RIGHT: "h5",
    },
    "h5": {
        ZONENAME: "shop",
        DESCRIPTION: "a humble shop",
        EXAMINE: "shop",
        UP: "g5",
        DOWN: "h5",
        LEFT: "h4",
        RIGHT: "h6",
    },
    "h6": {
        ZONENAME: "Blacksmith",
        DESCRIPTION: "a place to get weapons",
        EXAMINE: "blacksmith",
        UP: "g6",
        DOWN: "h6",
        LEFT: "h5",
        RIGHT: "h7",
    },
    "h7": {
        ZONENAME: "ally",
        DESCRIPTION: "in the darkness you see a grey metal door",
        EXAMINE: "puzzle1",
        UP: "g7",
        DOWN: "h7",
        LEFT: "h6",
        RIGHT: "h7",
    },
    "h8": {
        ZONENAME: "hidden shop",
        DESCRIPTION: "this shop caries many different wares \nfrom all around the world",
        EXAMINE: "hidden shop",
        UP: "g8",
        DOWN: "h8",
        LEFT: "h7",
        RIGHT: "h8",
    }
}


def battle():
    enemies = ["wolf", "gnome", "ogre", "snake", "dragon", "metal-man",
               "rouge automaton", "tin giraffe", "dark orb", "king crab", "slime", "gorgon the great", "average joe"]
    enemy1.name = random.choice(enemies)
    name = enemy1.name
    enemy1.hp = len(name) * 50
    enemy1.defence = len(name) * 10
    state = ""
    while state.lower() not in ["fight", "run"]:
        state = input(f"A {name} charged at you!!! \nFight>\nRun>\n>>>")

    if state.lower() == "fight":
        if len(enemy1.name) >= len(f"{player1.name} {player1.type}"):
            while enemy1.hp > 0:
                if player1.hp <= 0:
                    print("you died :(")
                    game()
                    return
                elif enemy1.hp <= 0:
                    print("you won :)")
                enemy_turn(name)
                player_turn()
        elif len(enemy1.name) < len(f"{player1.name} {player1.type}"):
            while enemy1.hp > 0:
                if player1.hp < 0:
                    print("you died :(")
                    game()
                    return
                elif enemy1.hp < 0:
                    print(f"you defeated the  {name}")
                player_turn()
                enemy_turn(name)
    elif state.lower() == "run":
        print(f"you got away, but not unscathed\nHP - 10")
        player1.hp -= 10
        return


def enemy_turn(enemy_name):
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
    vowels = ["a", "e", "i", "o", "u", "y"]
    maximum = len(enemy_name)
    minimum = round(len(enemy_name) * 0.4)
    length = random.randint(minimum, maximum)
    attack = ""
    while length > 0:
        length -= 1
        choice = random.randint(1, 2)
        if choice == 1:
            attack += f"{random.choice(vowels)}"
        if choice == 2:
            attack += f"{random.choice(consonants)}"
    attack_processor(attack, False, enemy1.name)


def player_turn():
    player_attack = input("choose an attack >>>")
    while len(player_attack) > 12:
        print("max character limit exceeded!!")
        player_attack = input("choose an attack >>>")
    os.system("clear")
    attack_processor(player_attack, True, enemy1.name)


def attack_processor(word, players_choice, enemy_name):
    vowels = ["a", "e", "i", "o", "u", "y"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
    damage = 0
    if players_choice:
        for character in word:
            if character in vowels:
                damage += 5
            elif character in consonants:
                damage += 10
        if "ea" in word or "ae" in word:
            damage += 50
        elif "ing" in word:
            damage += 30
    elif not players_choice:
        for character in word:
            damage += 3
            if character == "s":
                damage -= 1
    if players_choice:
        enemy1.hp -= damage
        print(f"you did {damage} damage to the {enemy_name}")
    elif not players_choice:
        player1.hp -= damage
        print(f"the {enemy_name} did {damage} damage")
        print(f"HP {player1.hp}")


def enemy_gen():
    letters = "abcdefgh"
    numbers = "12345678"
    increment = 0
    for place in enemy1.locations:
        letter = letters[random.randint(0, 7)]
        number = numbers[random.randint(0, 7)]
        location = letter + number
        enemy1.locations[increment] = location
        increment += 1
        print(place)


# shop handling
shop = ""
potion = ""
weapon = ""
hidden = ""

shop_inventory = {
    shop: [],
    potion: [],
    weapon: [],
    hidden: []
}


def shop(kind, karma):
    shop_types = ["shop", "hidden shop", "potion shop", "weapon shop", "hotel"]
    spacer = 10 * len(player1.name)
    if kind not in shop_types:
        print(f"{karma}")
        return
    if kind == "shop":
        print(f"+-Shop-{'-' * (spacer - 5)}+")
        for items in shop_inventory[shop]:
            print(f"|{items}{'' * (spacer - len(items))}|")
        print(f"+{'=' * spacer}+")


# map handling
player_map_unsolved = [["? ", "? ", "? ", "? ", "? ", "? ", "? ", "? "],
                       ["? ", "? ", "? ", "? ", "? ", "? ", "? ", "? "],
                       ["? ", "? ", "? ", "? ", "? ", "? ", "? ", "? "],
                       ["? ", "? ", "? ", "? ", "? ", "? ", "? ", "? "],
                       ["? ", "? ", "? ", "? ", "? ", "? ", "? ", "? "],
                       ["? ", "? ", "? ", "? ", "? ", "? ", "? ", "? "],
                       ["? ", "? ", "? ", "? ", "? ", "? ", "? ", "? "],
                       ["? ", "? ", "? ", "? ", "? ", "? ", "? ", "? "]]

player_map_solved = [["WH", "Sw", "Sw", "Gr", "Gr", "Gr", "Gr", "Gr"],
                     ["Sw", "Sw", "Sw", "TP", "Gr", "Gr", "Gr", "Gr"],
                     ["Sw", "Sw", "Sw", "Sw", "Fo", "H ", "Gr", "Gr"],
                     ["Sw", "Sw", "AC", "Po", "Fo", "Fo", "Fo", "CE"],
                     ["Sw", "Sw", "Fo", "Fo", "Fo", "Fo", "FL", "Al"],
                     ["Sw", "Fo", "Fo", "Fo", "Fo", "MS", "MS", "Al"],
                     ["Sw", "Fo", "Fo", "CB", "Ho", "MB", "Al", "FR"],
                     ["AC", "DF", "Fo", "CE", "Sh", "BS", "Al", "HS"]]
map_legend = "AC = Abandoned Cabin \n Al = Alleyway \n CB = City Bridge \n CC = City Center \n CE = City Entrance \n " \
             "DF = Dark Forest \n Fl = Farmland \n Fo = Forest \n FR = Fighting Ring \n Gr = Grassland \n H  = Home " \
             "\n Ho = Hotel \n HS = Hidden Shop \n MB = Milk Bar \n MS = Main Street \n PS = Potion Shop \n Sw = " \
             "Swampland \n Tp = Trader Post \n Wh = Witches Hut \n WS = Weapon Shop "


def print_location(action):
    y_position = 0
    x_position = 0
    if player1.location[0] == "a":
        y_position = 0
    elif player1.location[0] == "b":
        y_position = 1
    elif player1.location[0] == "c":
        y_position = 2
    elif player1.location[0] == "d":
        y_position = 3
    if player1.location[0] == "e":
        y_position = 4
    elif player1.location[0] == "f":
        y_position = 5
    elif player1.location[0] == "g":
        y_position = 6
    elif player1.location[0] == "h":
        y_position = 7
    if player1.location[1] == "1":
        x_position = 0
    elif player1.location[1] == "2":
        x_position = 1
    elif player1.location[1] == "3":
        x_position = 2
    elif player1.location[1] == "4":
        x_position = 3
    if player1.location[1] == "5":
        x_position = 4
    elif player1.location[1] == "6":
        x_position = 5
    elif player1.location[1] == "7":
        x_position = 6
    elif player1.location[1] == "8":
        x_position = 7
    player_map_unsolved[y_position][x_position] = player_map_solved[y_position][x_position]
    if action == "map":
        print("[" + player_map_unsolved[0][0] + "]" + "[" + player_map_unsolved[0][1] + "]" + "[" +
              player_map_unsolved[0][2] + "]" + "[" + player_map_unsolved[0][3] + "]" + "[" + player_map_unsolved[0][
                  4] + "]" + "[" + player_map_unsolved[0][5] + "]" + "[" + player_map_unsolved[0][6] + "]" + "[" +
              player_map_unsolved[0][7] + "]")
        print("[" + player_map_unsolved[1][0] + "]" + "[" + player_map_unsolved[1][1] + "]" + "[" +
              player_map_unsolved[1][2] + "]" + "[" + player_map_unsolved[1][3] + "]" + "[" + player_map_unsolved[1][
                  4] + "]" + "[" + player_map_unsolved[1][5] + "]" + "[" + player_map_unsolved[1][6] + "]" + "[" +
              player_map_unsolved[1][7] + "]")
        print("[" + player_map_unsolved[2][0] + "]" + "[" + player_map_unsolved[2][1] + "]" + "[" +
              player_map_unsolved[2][2] + "]" + "[" + player_map_unsolved[2][3] + "]" + "[" + player_map_unsolved[2][
                  4] + "]" + "[" + player_map_unsolved[2][5] + "]" + "[" + player_map_unsolved[2][6] + "]" + "[" +
              player_map_unsolved[2][7] + "]")
        print("[" + player_map_unsolved[3][0] + "]" + "[" + player_map_unsolved[3][1] + "]" + "[" +
              player_map_unsolved[3][2] + "]" + "[" + player_map_unsolved[3][3] + "]" + "[" + player_map_unsolved[3][
                  4] + "]" + "[" + player_map_unsolved[3][5] + "]" + "[" + player_map_unsolved[3][6] + "]" + "[" +
              player_map_unsolved[3][7] + "]")
        print("[" + player_map_unsolved[4][0] + "]" + "[" + player_map_unsolved[4][1] + "]" + "[" +
              player_map_unsolved[4][2] + "]" + "[" + player_map_unsolved[4][3] + "]" + "[" + player_map_unsolved[4][
                  4] + "]" + "[" + player_map_unsolved[4][5] + "]" + "[" + player_map_unsolved[4][6] + "]" + "[" +
              player_map_unsolved[4][7] + "]")
        print("[" + player_map_unsolved[5][0] + "]" + "[" + player_map_unsolved[5][1] + "]" + "[" +
              player_map_unsolved[5][2] + "]" + "[" + player_map_unsolved[5][3] + "]" + "[" + player_map_unsolved[5][
                  4] + "]" + "[" + player_map_unsolved[5][5] + "]" + "[" + player_map_unsolved[5][6] + "]" + "[" +
              player_map_unsolved[5][7] + "]")
        print("[" + player_map_unsolved[6][0] + "]" + "[" + player_map_unsolved[6][1] + "]" + "[" +
              player_map_unsolved[6][2] + "]" + "[" + player_map_unsolved[6][3] + "]" + "[" + player_map_unsolved[6][
                  4] + "]" + "[" + player_map_unsolved[6][5] + "]" + "[" + player_map_unsolved[6][6] + "]" + "[" +
              player_map_unsolved[6][7] + "]")
        print("[" + player_map_unsolved[7][0] + "]" + "[" + player_map_unsolved[7][1] + "]" + "[" +
              player_map_unsolved[7][2] + "]" + "[" + player_map_unsolved[7][3] + "]" + "[" + player_map_unsolved[7][
                  4] + "]" + "[" + player_map_unsolved[7][5] + "]" + "[" + player_map_unsolved[7][6] + "]" + "[" +
              player_map_unsolved[7][7] + "]")


def prompt():
    action = input("what would you like to do > ")
    acceptable_actions = ["go", "move", "travel", "quit", "help", "examine", "interact", "check", "look", "map",
                          "legend", "menu", "stats", "pause"]

    while action.lower() not in acceptable_actions:
        print("invalid action")
        action = input(">>> ")
    if action.lower() == "quit":
        sys.exit()
    elif action.lower() in ["go", "move", "travel"]:
        player_move(action.lower())
    elif action.lower() in ["examine", "interact", "check", "look"]:
        player_examine(action.lower())
    elif action.lower() == "map":
        print_location(action.lower())
    elif action.lower() == "legend":
        print(map_legend)
    elif action.lower() in ["menu", "stats", "pause"]:
        stats()
    elif action.lower() == "help":
        help_menu()


def player_move(my_action):
    ask = "what direction would you like to " + my_action + " in?\n"
    destination = input(ask)

    if destination.lower() in ["up", "north"]:
        destination = zone_map[player1.location][UP]
        movement_handler(destination)
    elif destination.lower() in ["down", "south"]:
        destination = zone_map[player1.location][DOWN]
        movement_handler(destination)
    elif destination.lower() in ["left", "west"]:
        destination = zone_map[player1.location][LEFT]
        movement_handler(destination)
    elif destination.lower() in ["right", "east"]:
        destination = zone_map[player1.location][RIGHT]
        movement_handler(destination)
    print_location(my_action)


def movement_handler(destination):
    os.system("clear")
    print("you are now in " + zone_map[destination][ZONENAME] + "\n" + zone_map[destination][DESCRIPTION])
    location_comp = player1.location
    player1.location = destination
    if player1.location == location_comp:
        print("you couldn't go that way \nso you decided to stay here")


def player_examine(my_action):
    triggers = ["puzzle1", "puzzle2", "puzzle3", "puzzle4"]
    shops = ["hidden shop", "weapon shop"]
    if player1.location in enemy1.locations:
        battle()
        enemy_gen()
        return
    if solved_places[player1.location]:
        print("you've already exhausted this area")
        return
    if zone_map[player1.location][EXAMINE] not in triggers and zone_map[player1.location][EXAMINE] not in shops:
        print(zone_map[player1.location][EXAMINE])
    elif my_action in shops:
        print("no shops yet")


def game():
    global game_start
    while not player1.game_over:
        game_start = True
        prompt()
        if player1.hp <= 0:
            player1.game_over = True


def setup_game():
    os.system("clear")
    question1 = "\nwhat is your name? >>> "
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep((random.uniform(0, 4) * 0.1))
    player_name = input("")
    player1.name = player_name
    question2 = "what is your class/occupation? >>> "
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep((random.uniform(0, 4) * 0.1))
    player_type = input("")

    while len(player_type) > 20:
        print("max character limit exceeded")
        player_type = input("")
    player1.type = player_type
    player1.hp += len(player_type) * 100

    reply = f"welcome {player1.name} the {player1.type}, \n"
    for character in str(reply):
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep((random.uniform(0, 4) * 0.1))
    print_location("map")


title_screen()
game()
