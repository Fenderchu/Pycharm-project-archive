
# import functuons needed ver 0.4.0

import cmd
import textwrap
import os
import time
import random
import sys
screan_width = 100


# player statas management / storage

class player:
    def __init__ (self):
        self.name = ""
        self.karma = 0
        self.hp = 0
        self.mp = 0
        self.speed = 0
        self.deffence = 0
        self.attack = 0
        self.attacks =[]
        self.weaponaf = []
        self.equwep = ""
        self.spells = []
        self.inventory = ["test", "test2"]
        self.status = []
        self.location = "c5"
        self.gameover = False
        self.type = ""


player1 = player()


class enemy:
    def __init__(self):
        self.name = ""
        self.karma = 0
        self.hp = 0
        self.mp = 0
        self.speed = 0
        self.deffence = 0
        self.attack = 0
        self.attacks = []
        self.weaponaf = []
        self.equwep = ""
        self.spells = []
        self.killdrop = []
        self.status = []
        self.location = "c5"
        self.type = ""


enemy1 = enemy()


# title screan

def title_screan_input():
    option = input("> ")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ["play", "help", "quit"]:
        option = input("> ")
        if option.lower() == ("play"):
            setup_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()


def title_screan():
    os.system("clear")
    print ("\n .d88b      db     8b   d8  8888")
    print (" 8P www    dPYb    8YbmdP8  8www")
    print (" 8b  d8   dPwwYb   8  Y  8  8   ")
    print (" `Y88P'  dP    Yb  8     8  8888")
    print ("              Adventure         ")
    print ("               -Play-           ")
    print ("               -Help-           ")
    print ("               -quit-           ")
    title_screan_input()


def help_menu():
    print ("         Welcome to the game         ")
    print (" Use the move or go command to travel")
    print (" use the look or interact commands   ")
    print (" to examine your environment         ")
    print (" avalable class roles                ")
    print (" ranger,knight,mage,rouge,bard,cleric")
    print (" open the map with the map command   ")
    print (" use the legend command to veiw the  ")
    print (" map legend                          ")
    print ("               -play-                ")
    print ("               -quit-                ")
    title_screan_input()


def stats():
    os.system("clear")
    hp = player1.hp
    df = player1.deffence
    ak = player1.attack
    name = player1.name
    ty = player1.type
    inventory = player1.inventory
    spacer = (5 * len(name))
    print("+" + "=" * spacer + "+")
    print("|" + name + " the " + ty + " " * (spacer - (5 + len(name) + len(ty))) + "|")
    print("|" + "hp " + str(hp) + " mp " + str(player1.mp) + " " * (
                spacer - (7 + len(str(hp)) + len(str(player1.mp)))) + "|")
    print("|" + "attack " + str(ak) + " " * (spacer - (7 + len(str(ak)))) + "|")
    print("defence " + str(df) + " " * (spacer - (8 + len(str(ak)))) + "|")
    print("+" + "=" * spacer + "+")
    print("|-Inventory-" + "-" * (spacer - 11) + "|")
    for item in inventory:
        print("|" + item + " " * (spacer - (len(item))) + "|")
    print("+" + "=" * spacer + "+")

    # Map


# a1 a2
# [] [] b1
# [] [] b2
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

zonemap = {
    "a1": {
        ZONENAME: "Witches hut",
        DESCRIPTION: "The home of a witch",
        EXAMINE: "picture",
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
        EXAMINE: "the foliage is extramly thick here",
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
        DESCRIPTION: "the foliage is dencer here",
        EXAMINE: "the ground seems softer",
        UP: "d1",
        DOWN: "f1",
        LEFT: "e1",
        RIGHT: "e2",
    },
    "e2": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is dencer here",
        EXAMINE: "the ground seems softer",
        UP: "d2",
        DOWN: "f2",
        LEFT: "e1",
        RIGHT: "e3",
    },
    "e3": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is dencer here",
        EXAMINE: "the ground seems softer",
        UP: "d3",
        DOWN: "f3",
        LEFT: "e2",
        RIGHT: "e4",
    },
    "e4": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is dencer here",
        EXAMINE: "the ground seems softer",
        UP: "d4",
        DOWN: "f4",
        LEFT: "e3",
        RIGHT: "e5",
    },
    "e5": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is dencer here",
        EXAMINE: "the ground seems softer",
        UP: "d5",
        DOWN: "f5",
        LEFT: "e4",
        RIGHT: "e6",
    },
    "e6": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is dencer here",
        EXAMINE: "the ground seems softer",
        UP: "d6",
        DOWN: "f6",
        LEFT: "e5",
        RIGHT: "e7",
    },
    "e7": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is dencer here",
        EXAMINE: "the ground seems softer",
        UP: "d7",
        DOWN: "f7",
        LEFT: "e6",
        RIGHT: "e8",
    },
    "e8": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is dencer here",
        EXAMINE: "the ground seems softer",
        UP: "d8",
        DOWN: "f8",
        LEFT: "e7",
        RIGHT: "e8",
    },
    "f1": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is dencer here",
        EXAMINE: "the ground seems softer",
        UP: "e1",
        DOWN: "g1",
        LEFT: "f1",
        RIGHT: "f2",
    },
    "f2": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is dencer here",
        EXAMINE: "the ground seems softer",
        UP: "f2",
        DOWN: "g2",
        LEFT: "f1",
        RIGHT: "f3",
    },
    "f3": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is dencer here",
        EXAMINE: "the ground seems softer",
        UP: "e3",
        DOWN: "g3",
        LEFT: "f2",
        RIGHT: "f4",
    },
    "f4": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is dencer here",
        EXAMINE: "the ground seems softer",
        UP: "e4",
        DOWN: "g4",
        LEFT: "f3",
        RIGHT: "f5",
    },
    "f5": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is dencer here",
        EXAMINE: "the ground seems softer",
        UP: "e5",
        DOWN: "g5",
        LEFT: "f4",
        RIGHT: "f6",
    },
    "f6": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is dencer here",
        EXAMINE: "the ground seems softer",
        UP: "e6",
        DOWN: "g6",
        LEFT: "f5",
        RIGHT: "f7",
    },
    "f7": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is dencer here",
        EXAMINE: "the ground seems softer",
        UP: "e7",
        DOWN: "g7",
        LEFT: "f6",
        RIGHT: "f8",
    },
    "f8": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is dencer here",
        EXAMINE: "the ground seems softer",
        UP: "e8",
        DOWN: "g8",
        LEFT: "f7",
        RIGHT: "f8",
    },
    "g1": {
        ZONENAME: "deep forest",
        DESCRIPTION: "the foliage is dencer here",
        EXAMINE: "the ground seems softer",
        UP: "f1",
        DOWN: "h1",
        LEFT: "g1",
        RIGHT: "g2",
    },
    "g2": {
        ZONENAME: " deep forest",
        DESCRIPTION: "the foliage is dencer here",
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
        DESCRIPTION: "it looks unstable",
        EXAMINE: "item",
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
        DESCRIPTION: "theres alot of moss here",
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

move_stats = {
    "Dev_move": {
        "attack_damage": "high",
        "stat_drop": "defence",
        "stat_raise": "deffence",
        "description": "if you can see this \nsomething is wrong \nand you should tell the developer"

    },
    "punch": {
        "attack_damage": "medium",
        "stat_drop": "none",
        "stat_raise": "",
        "description": "the user punches the foe"
    }
}

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
    if kind == shop:
        print("+-Shop-" + "-" * (spacer - 5) + "+")
        for items in shop_inventory[shop]:
            print("|" + items + " " * (spacer - len(items)) + "|")
        print("+" + "=" * (spacer) + "+")


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
map_legend = " AC = Abandoned Cabin \n Al = Allyway \n CB = City Bridge \n CC = City Center \n CE = City Entrance \n DF = Dark Forest \n Fl = Farmland \n Fo = Forest \n FR = Fighting Ring \n Gr = Grassland \n H  = Home \n Ho = Hotel \n HS = Hidden Shop \n MB = Milk Bar \n MS = Main Street \n PS = Potion Shop \n Sw = Swampland \n Tp = Trader Post \n Wh = Witches Hut \n WS = Weapon Shop "


def print_location(action):
    if player1.location[0] == "a":
        ypos = 0
    elif player1.location[0] == "b":
        ypos = 1
    elif player1.location[0] == "c":
        ypos = 2
    elif player1.location[0] == "d":
        ypos = 3
    if player1.location[0] == "e":
        ypos = 4
    elif player1.location[0] == "f":
        ypos = 5
    elif player1.location[0] == "g":
        ypos = 6
    elif player1.location[0] == "h":
        ypos = 7
    if player1.location[1] == "1":
        xpos = 0
    elif player1.location[1] == "2":
        xpos = 1
    elif player1.location[1] == "3":
        xpos = 2
    elif player1.location[1] == "4":
        xpos = 3
    if player1.location[1] == "5":
        xpos = 4
    elif player1.location[1] == "6":
        xpos = 5
    elif player1.location[1] == "7":
        xpos = 6
    elif player1.location[1] == "8":
        xpos = 7
    player_map_unsolved[ypos][xpos] = player_map_solved[ypos][xpos]
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
    acceptable_actions = ["go", "move", "travel", "quit", "examine", "interact", "check", "look", "map", "legend",
                          "menu", "stats", "pause"]

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


def player_move(myaction):
    ask = "what direction would you like to " + myaction + " in?"
    destination = input(ask)

    if destination.lower() in ["up", "north"]:
        dest = zonemap[player1.location][UP]
        movment_handler(dest)
    elif destination.lower() in ["down", "south"]:
        dest = zonemap[player1.location][DOWN]
        movment_handler(dest)
    elif destination.lower() in ["left", "west"]:
        dest = zonemap[player1.location][LEFT]
        movment_handler(dest)
    elif destination.lower() in ["right", "east"]:
        dest = zonemap[player1.location][RIGHT]
        movment_handler(dest)
    print_location(myaction)


def movment_handler(destination):
    os.system("clear")
    print("you are now in " + zonemap[destination][ZONENAME] + "\n" + zonemap[destination][DESCRIPTION])
    location_comp = player1.location
    player1.location = destination
    if player1.location == location_comp:
        print("you couldent go that way \nso you decided to stay here")


def player_examine(myaction):
    shops = ["hidden shop", "weapon shop"]
    fight_trigers = ["wolf", "snake", "oger"]
    enemy_name = ""
    if solved_places[player1.location] == True:
        print("you've already exausted this area")
        return
    if zonemap[player1.location][EXAMINE] not in shops and zonemap[player1.location][EXAMINE] not in fight_trigers:
        print(zonemap[player1.location][EXAMINE])
    elif myaction in shops:
        print ("no shops yet")


def game():
    while player1.gameover == False:
        prompt()
        if player1.hp <= 0:
            player.gameover = True


def setup_game():
    os.system("clear")
    question1 = "\nwhat is your name?"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush
        time.sleep(0.05)
    player_name = input(">>>")
    player1.name = player_name
    question2 = "what is your class?"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush
        time.sleep(0.05)
    player_type = input(">>>")
    if player_type.lower() in ["ranger", "knight", "mage", "rouge", "bard", "cleric", ]:
        player1.type = player_type
        print("your now a " + player1.type)
    else:
        while player1.type not in ["ranger", "knight", "mage", "rouge", "bard", "cleric", ]:
            print("thats not a valid class")
            player_type = input(">")
            if player_type.lower() in ["ranger", "knight", "mage", "rouge", "bard", "cleric", ]:
                player1.type = player_type
                print("your now a " + player1.type)
    if player1.type.lower() == "ranger":
        player1.hp = 125
        player1.mp = 75
        player1.speed = 8
        player1.deffence = 5
        player1.weaponaf = ["wood bow", "steel bow", "crossbow", "Chinese fire lance"]
        player1.equwep = "sling"
        player1.spells = ["defence", "aim", "swift"]
        player1.attacks = ["presision shot", "rapid fire"]
    elif player1.type.lower() == "knight":
        player1.hp = 50
        player1.mp = 25
        player1.speed = 5
        player1.deffence = 20
        player1.weaponaf = ["spear", "tin sword", "steel sword"]
        player1.equwep = "fist"
        player1.spells = ["defence"]
        player1.attacks = ["charge", "bludgeon", "war cry"]
    elif player1.type.lower() == "mage":
        player1.hp = 150
        player1.mp = 200
        player1.speed = 6
        player1.deffence = 10
        player1.weaponaf = ["magic stick", "strage ball", "shiny pebble"]
        player1.equwep = "fist"
        player1.spells = ["fireball", "defence", "stun", "observe"]
        player1.attacks = ["punch", "magic trick", "foolery"]
    elif player1.type.lower() == "rouge":
        player1.hp = 100
        player1.mp = 75
        player1.speed = 9
        player1.deffence = 5
        player1.weaponaf = ["dagger", "poisen dagger", "staff", "dart blower"]
        player1.equwep = "fist"
        player1.spells = ["swift"]
        player1.attacks = ["back stab", "sabotoge", "bambozle"]
    elif player1.type.lower() == "bard":
        player1.hp = 75
        player1.mp = 150
        player1.speed = 3
        player1.deffence = 12
        player1.weaponaf = ["pan flute", "mallets", "triangle", "golden banjo", "Danceing For Dummys"]
        player1.equwep = "fist"
        player1.spells = ["stun", "break"]
        player1.attacks = ["sour note", "B-flat", "A-sharp"]
    elif player1.type.lower() == "cleric":
        player1.hp = 50
        player1.mp = 100
        player1.speed = 4
        player1.deffence = 30
        player1.weaponaf = ["magic stick", "holy mackerel", "wood sword"]
        player1.equwep = "fist"
        player1.spells = ["healing", "stun"]
        player1.attacks = ["exorcise", "sheild bash"]
    question1 = "welcome " + player1.name + " the " + player1.type + ", \n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush
    print_location("map")


title_screan()
game()














