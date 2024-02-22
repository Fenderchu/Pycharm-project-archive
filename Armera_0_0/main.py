import random


# character class
class character:

    def __init__(self):
        self.name = " "
        self.gender = "null"
        self.abilities = []
        self.sturdiness = 0
        self.endearment = 0
        self.acuity = 0
        self.luck = 0
        self.area = "00"
        self.pos1 = 1
        self.pos2 = 1
        self.inventory = []
        self.weapon = "008"
        self.armor = "009"
        self.health = 100
        self.max_health = 100


# enemy class
class enemy:

    def __init__(self):
        self.name = " "
        self.attack = 0
        self.attack_type = ""
        self.hard_armor = 0
        self.soft_armor = 0
        self.drops = []
        self.health = 100


player = character()
save_available = True
game_over = False


# title screen display and inputs
def title():
    title_sprite = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    possible_inputs = [1, 2]
    save = open("save", "r")
    global save_available
    for position, line in enumerate(save):
        if "empty" in line:
            save_available = False
    if save_available:
        title_sprite += [9]
        possible_inputs += [3]
    sprite_renderer(title_sprite)
    input1 = input_manager(possible_inputs)
    if input1 == 1:
        # open help menu
        return help_menu()
    elif input1 == 2:
        return character_setup()
    elif input1 == 3:
        return continue_manager()


def help_menu():
    current_page = 0
    possible_inputs = [1, 2, 3, 4, 5, 6]
    pages = [[12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
             [28, 29, 30, 31, 32, 33, 34, 35, 36],
             [38, 39, 40, 41, 42, 43, 44, 45, 46],
             [48, 49, 50, 51, 52, 53, 54, 55, 56],
             [108, 109, 110, 111, 112, 113, 114, 115, 116]
             ]
    sprite_renderer(pages[current_page])
    while True:
        input1 = input_manager(possible_inputs)
        possible_inputs = [1]
        if input1 == 1 and current_page == 0:
            current_page = 1
        elif input1 == 1 and current_page != 0:
            current_page = 0
            possible_inputs = [1, 2, 3, 4]
        elif input1 == 2 and current_page == 0:
            current_page = 4
        elif input1 == 3 and current_page == 0:
            current_page = 3
        elif input1 == 4 and current_page == 0:
            return title()

        sprite_renderer(pages[current_page])


def sprite_renderer(lines_needed):
    sprite = ""
    sprite_sheet = open("asci_Sprites", "r")
    for position, line in enumerate(sprite_sheet):
        if position in lines_needed:
            line.strip("\n")
            sprite += f"{line}"
    sprite_sheet.close()
    print(sprite)


def input_manager(available_inputs):
    while True:
        input1 = input(">>>")
        if input1.isnumeric():
            if int(input1) in available_inputs:
                return int(input1)
            else:
                print("Invalid input")
        elif str(input1) in available_inputs:
            return str(input1)
        else:
            print("Invalid input")


def save_manager(save_subject):
    if save_subject == 0:
        save = open("save", "a")
        save.truncate(0)
        save.writelines(["empty"])
        save.close()
    elif save_subject == 1:
        stats = [player.name + "\n",
                 player.gender + "\n",
                 str(player.sturdiness) + "\n",
                 str(player.endearment) + "\n",
                 str(player.acuity) + "\n",
                 str(player.luck) + "\n",
                 str(player.area) + "\n",
                 str(player.pos1) + "\n",
                 str(player.pos2) + "\n"
                 ]
        save = open("save", "a")
        save.truncate(0)
        save.writelines(stats)


def continue_manager():
    save = open("save", "r")
    data = []
    global game_over
    lines_needed = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    counter = 0
    for position, line in enumerate(save):
        if position in lines_needed:
            line.strip("\n")
            data.append(f"{line}")
    save.close()
    for _ in data:
        data[counter] = data[counter].rstrip()
        counter += 1
    player.name = data[0]
    player.gender = data[1]
    player.sturdiness = int(data[2])
    player.endearment = int(data[3])
    player.acuity = int(data[4])
    player.luck = int(data[5])
    player.area = data[6]
    player.pos1 = int(data[7])
    player.pos2 = int(data[8])
    game_over = False
    game_loop()


def character_setup():
    skill_points = 18
    if save_available:
        print("Are you sure you want to overwrite the stored save data?\n1:Yes\n2:No")
        input1 = input_manager([1, 2])
        if input1 == 1:
            save_manager(0)
            return title()
        elif input1 == 2:
            return title()
    elif not save_available:
        while player.name == " ":
            sprite_renderer([58, 59, 60, 61, 62, 63, 64, 77, 78])
            name = input(">>>")
            if len(name) > 12:
                print("Name exceeds character limit!")
            else:
                player.name = name
        while player.gender == "null":
            sprite_renderer([58, 59, 60, 61, 62, 75, 76, 77, 78])
            gender = input_manager([1, 2, 3])
            if gender == 1:
                gender = "male"
            elif gender == 2:
                gender = "female"
            elif gender == 3:
                gender = "non-binary"
            player.gender = gender
        while player.sturdiness < 1:
            sprite_renderer([58, 59, 61, 62, 67, 68, 77, 78])
            print(f"you have {skill_points} points left")
            input2 = input_manager([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            if skill_points - input2 < 0:
                print("not enough points left!!!")
            else:
                skill_points -= input2
                player.sturdiness = input2

        while player.endearment < 1:
            sprite_renderer([58, 59, 61, 62, 71, 72, 77, 78])
            print(f"you have {skill_points} points left")
            input2 = input_manager([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            if skill_points - input2 < 0:
                print("not enough points left!!!")
            else:
                player.endearment = input2
                skill_points -= input2
        while player.acuity < 1:
            sprite_renderer([58, 59, 61, 62, 69, 70, 77, 78])
            print(f"you have {skill_points} points left")
            input2 = input_manager([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            if skill_points - input2 < 0:
                print("not enough points left!!!")
            else:
                player.acuity = input2
                skill_points -= input2
        while player.luck < 1:
            sprite_renderer([58, 59, 61, 62, 73, 74, 77, 78])
            print(f"you have {skill_points} points left")
            input2 = input_manager([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            if skill_points - input2 < 0:
                print("not enough points left!!!")
            else:
                player.luck = input2
                skill_points -= input2
        save_manager(1)
        game_loop()


# Item cataloging/qualities
item_name = "name"
item_type = "type"
item_subtype = "subtype"
weapon_stats = "weapon"
armor_stats = "armor"
aid_stats = "aid"
items = {
    "001": {
        item_name: "test",
        item_type: "aid",
        aid_stats: [0]
    },
    "002": {
        item_name: "Bandages",
        item_type: "aid",
        aid_stats: [10 * round(player.sturdiness / 2)]
    },
    "003": {
        item_name: "Ormanal",
        item_type: "Aid",
        aid_stats: [100, 10 * round(player.sturdiness / 3)]
    },
    "004": {
        item_name: "Steroids",
        item_type: "aid",
        aid_stats: [2]
    },
    "005": {
        item_name: "Focus Fluid",
        item_type: "aid",
        aid_stats: [2]
    },
    "006": {
        item_name: "Fine Wine",
        item_type: "aid",
        aid_stats: [2]
    },
    "007": {
        item_name: "Scotch Chews",
        item_type: "aid",
        aid_stats: [2]
    },
    "008": {
        item_name: "Fists",
        item_type: "weapon",
        item_subtype: "melee",
        weapon_stats: [1]
    },
    "009": {
        item_name: "Bare",
        item_type: "armor",
        armor_stats: [1, 1]
    },
    "010": {
        item_name: "Iron Knuckles",
        item_type: "weapon",
        item_subtype: "melee",
        weapon_stats: [3]
    },
    "011": {
        item_name: "Thick Cloth Armor",
        item_type: "armor",
        armor_stats: [3, 1]
    },
    "012": {
        item_name: "sling",
        item_type: "weapon",
        item_subtype: "ranged",
        weapon_stats: [3]
    },
    "013": {
        item_name: "Leather Armor",
        item_type: "armor",
        armor_stats: [4, 2]
    },
    "014": {
        item_name: "Wrench",
        item_type: "weapon",
        item_subtype: "melee",
        weapon_stats: [5]
    },
    "015": {
        item_name: "Scrap Plate Armor",
        item_type: "armor",
        armor_stats: [4, 3]
    },
    "016": {
        item_name: "bow",
        item_type: "weapon",
        item_subtype: "ranged",
        weapon_stats: [5]
    },

}

# map stuff
area_map = "map"
loot_pool = "pool"
area_difficulty = "difficulty"
armera_map = {
    "00": {
        area_map: [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, "D", 0, 0, 0, 0, 0, 0],
            [0, 0, "!", 0, 0, "D", 0, 0, 0],
            [0, 0, 0, 0, "D", "D", 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ],
        loot_pool: [
            ["011", "012", "011", "013", "010"],
            ["012", "011", "006", "007", "010"]
        ],
        area_difficulty: 1
    },
    "01": {
        area_map: [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ],
        loot_pool: [
            ["001", "001", "001", "001", "001"],
            ["001", "001", "001", "001", "001"]
        ],
        area_difficulty: 1
    },
    "02": {
        area_map: [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ],
        loot_pool: [
            ["001", "001", "001", "001", "001"],
            ["001", "001", "001", "001", "001"]
        ],
        area_difficulty: 1
    },
    "10": {
        area_map: [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ],
        loot_pool: [
            ["001", "001", "001", "001", "001"],
            ["001", "001", "001", "001", "001"]
        ],
        area_difficulty: 1
    },
    "11": {
        area_map: [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ],
        loot_pool: [
            ["001", "001", "001", "001", "001"],
            ["001", "001", "001", "001", "001"]
        ],
        area_difficulty: 1
    },
    "12": {
        area_map: [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ],
        loot_pool: [
            ["001", "001", "001", "001", "001"],
            ["001", "001", "001", "001", "001"]
        ],
        area_difficulty: 1
    },
    "20": {
        area_map: [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ],
        loot_pool: [
            ["001", "001", "001", "001", "001"],
            ["001", "001", "001", "001", "001"]
        ],
        area_difficulty: 1
    },
    "21": {
        area_map: [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ],
        loot_pool: [
            ["001", "001", "001", "001", "001"],
            ["001", "001", "001", "001", "001"]
        ],
        area_difficulty: 1
    },
    "22": {
        area_map: [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ],
        loot_pool: [
            ["001", "001", "001", "001", "001"],
            ["001", "001", "001", "001", "001"]
        ],
        area_difficulty: 1
    },
}


def map_printer():
    area = player.area
    area_position1 = player.pos1
    area_position2 = player.pos2
    map_print = ""
    area_line = -1

    for row in armera_map[area][area_map]:
        counter = 0
        area_line += 1
        map_print += "\n"
        for _ in row:
            if area_position1 == area_line and counter == area_position2:
                map_print += " @"
            elif counter == area_position2 - 1 and area_line == area_position1 or \
                    counter == area_position2 + 1 and area_line == area_position1 or \
                    counter == area_position2 and area_line == area_position1 + 1 or \
                    counter == area_position2 and area_line == area_position1 - 1:
                map_print += " " + str(armera_map[area][area_map][area_line][counter])
                pass
            elif counter == area_position2 - 1 and area_line == area_position1 - 1 or \
                    counter == area_position2 - 1 and area_line == area_position1 + 1 or \
                    counter == area_position2 + 1 and area_line == area_position1 - 1 or \
                    counter == area_position2 + 1 and area_line == area_position1 + 1:
                map_print += " " + str(armera_map[area][area_map][area_line][counter])
            else:
                map_print += " #"
            counter += 1
    print(map_print)


# enemy management
def enemy_spawner():
    enemy_map_icons = ["A", "B", "D"]
    new_enemy = enemy()
    difficulty_multiplier = armera_map[player.area][area_difficulty]
    place = str(armera_map[player.area][area_map][player.pos1][player.pos2])
    if place in enemy_map_icons:
        if place == enemy_map_icons[0]:
            new_enemy.name = "Arma Troop"
            new_enemy.hard_armor = round(6 * difficulty_multiplier)
            new_enemy.soft_armor = round(5 * difficulty_multiplier)
            new_enemy.attack = round(4 * difficulty_multiplier)
            new_enemy.attack_type = "ranged"
            new_enemy.drops = ["011", "002", "002"]
            new_enemy.health = 100
        if place == enemy_map_icons[1]:
            new_enemy.name = "Bandit"
            new_enemy.hard_armor = round(3 * difficulty_multiplier)
            new_enemy.soft_armor = round(4 * difficulty_multiplier)
            new_enemy.attack = round(3 * difficulty_multiplier)
            new_enemy.attack_type = "melee"
            new_enemy.drops = ["002", "003", "002"]
            new_enemy.health = 50
        if place == enemy_map_icons[2]:
            new_enemy.name = "Feral Dog"
            new_enemy.hard_armor = round(1 * difficulty_multiplier)
            new_enemy.soft_armor = round(1 * difficulty_multiplier)
            new_enemy.attack = round(2 * difficulty_multiplier)
            new_enemy.attack_type = "melee"
            new_enemy.drops = ["002", "002"]
            new_enemy.health = 10
        fight_manager(new_enemy)


def fight_manager(new_enemy):
    picker1 = random.randint(1, 2)
    message = ""
    player_win = False
    fight = True
    global game_over
    if picker1 == 1:
        message += f"The {new_enemy.name} charges at you"
    else:
        message += f"The {new_enemy.name} is blocking the way"
    print(message)
    while fight:
        player_attack = 0
        player_defence = 0
        player_choice = ""
        pronoun = ""
        enemy_attack = 0
        enemy_defence = 0
        enemy_choice = ""
        # player turn
        if player.gender == "male":
            pronoun += "him"
        elif player.gender == "female":
            pronoun += "her"
        else:
            pronoun += "them"
        print("your turn\n1:Attack\n2:Defend\n3:Item")
        input1 = input_manager([1, 2, 3])
        if input1 == 1:
            player_choice = "attack"
            crit = random.randint(0, (18 - player.luck))
            random_extra = random.randint(0, 10)
            if crit == 1:
                player_attack += 2 * (items[player.weapon][weapon_stats][0]) + random_extra
            else:
                player_attack = items[player.weapon][weapon_stats][0]
            if new_enemy.attack_type == "melee":
                player_defence += items[player.armor][armor_stats][0]
            elif new_enemy.attack_type == "ranged":
                player_defence += items[player.armor][armor_stats][1]
        elif input1 == 2:
            player_choice = "defend"
            if new_enemy.attack_type == "melee":
                player_defence += (items[player.armor][armor_stats][0] * 2)
            elif new_enemy.attack_type == "ranged":
                player_defence += (items[player.armor][armor_stats][1] * 2)
            elif input1 == 3:
                player_choice = "item"
                pass

        if player_attack <= 0:
            player_attack = 1
        # enemy turn
        if new_enemy.health < (enemy().health / 2):
            choice = random.randint(0, 10)
            if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
                enemy_choice += "attack"
                enemy_attack += new_enemy.attack
                if items[player.weapon][item_subtype] == "melee":
                    enemy_defence += new_enemy.hard_armor
                elif items[player.weapon][item_subtype] == "ranged":
                    enemy_defence += new_enemy.soft_armor
            else:
                enemy_choice += "defend"
                enemy_attack = 0
                if items[player.weapon][item_subtype] == "melee":
                    enemy_defence += (new_enemy.hard_armor * 2)
                elif items[player.weapon][item_subtype] == "ranged":
                    enemy_defence += (new_enemy.soft_armor * 2)
        else:
            enemy_choice += "attack"
            enemy_attack += new_enemy.attack
            if items[player.weapon][item_subtype] == "melee":
                enemy_defence += new_enemy.hard_armor
            elif items[player.weapon][item_subtype] == "ranged":
                enemy_defence += new_enemy.soft_armor
        player_attack -= round(enemy_defence / (player.sturdiness / 2))
        enemy_attack -= player_defence
        if player_attack < 0:
            player_attack = 0
        if enemy_attack < 0:
            enemy_attack = 0
        if player_choice == "attack":
            print(f"{player.name} dose {player_attack} damage to {new_enemy.name}")
            new_enemy.health -= player_attack
        elif player_choice == "defend":
            print(f"{player.name} braces {pronoun}self")
        else:
            pass

        if enemy_choice == "attack":
            print(f"{new_enemy.name} dose {enemy_attack} damage")
            player.health -= enemy_attack
        elif enemy_choice == "defend":
            print(f"{new_enemy.name} braces themself")
        if new_enemy.health <= 0:
            fight = False
            player_win = True
        if player.health <= 0:
            game_over = True
            fight = False
    if player_win:
        print(f"{player.name} has defeated the {new_enemy.name}")
        loot_chance = random.randint(0, 5)
        armera_map[player.area][area_map][player.pos1][player.pos2] = 0
        if loot_chance == 1:
            in_inv = False
            dropped_item = random.choice(new_enemy.drops)
            for item in player.inventory:
                if item[0] == dropped_item:
                    item[1] += 1
                    in_inv = True
            if not in_inv:
                added_item = [dropped_item, 1]
                player.inventory.append(added_item)
            print(f"The {new_enemy.name} dropped {dropped_item}, {player.name} picks it up")


# managing movement/events
def action_manager():
    enemies = ["A", "B", "D"]
    possible_inputs = ["left", "right", "up", "down", "check", "menu"]
    if str(armera_map[player.area][area_map][player.pos1][player.pos2]) in enemies:
        enemy_spawner()
    input1 = input_manager(possible_inputs)
    if input1.lower() in ["left", "right", "up", "down"]:
        movement_manager(input1)
    elif input1.lower() == "check":
        check_manager()
    elif input1.lower() == "menu":
        menu()
    else:
        print("you have found a bug\nplease file a bug report at (insert github url)")


def movement_manager(direction):
    if direction == "left":
        if player.pos2 == 0:
            if player.area[1] == "0":
                print("Cant go that way")
            else:
                player.area = player.area[0] + str(int(player.area[1]) - 1)
                player.pos2 = 8
        else:
            player.pos2 -= 1

    if direction == "right":
        if player.pos2 == 8:
            if player.area[1] == "2":
                print("Cant go that way")
            else:
                player.area = player.area[0] + str(int(player.area[1]) + 1)
                player.pos2 = 0
        else:
            player.pos2 += 1

    if direction == "up":
        if player.pos1 == 0:
            if player.area[0] == "0":
                print("Cant go that way")
            else:
                player.area = str(int(player.area[0]) - 1) + player.area[1]
                player.pos1 = 8
        else:
            player.pos1 -= 1

    if direction == "down":
        if player.pos1 == 8:
            if player.area[0] == "2":
                print("Cant go that way")
            else:
                player.area = str(int(player.area[0]) + 1) + player.area[1]
                player.pos1 = 0
        else:
            player.pos1 += 1
    return map_printer()


def menu():
    sprite_renderer([90, 91, 92, 93, 94, 95, 96])
    input1 = input_manager([1, 2, 3, 4])
    if input1 == 1:
        print(
            f"Name:{player.name}\n"
            f"Gender:{player.gender}\n"
            f"Sturdiness:{player.sturdiness}\n"
            f"Endearment:{player.endearment}\n"
            f"Acuity:{player.acuity}\n"
            f"Luck:{player.luck}\n"
            f"Hard Defence:{items[player.armor][armor_stats][0]}\n"
            f"Soft Defence:{items[player.armor][armor_stats][1]}\n"
            f"Weapon:{items[player.weapon][item_name]}\n"
            f"Armor:{items[player.armor][item_name]}\n"
        )
        map_printer()
        action_manager()
    elif input1 == 2:
        inventory_display()
    elif input1 == 3:
        map_print = ""
        counter1 = 0
        for row in armera_map[player.area][area_map]:
            counter1 += 0
            counter2 = 0
            map_print += "\n"
            for spot in row:
                map_print += " " + str(spot)
                counter2 += 1
        print(map_print)
        action_manager()
    elif input1 == 4:
        map_printer()
        action_manager()


def inventory_display():
    inv_print = ""
    inv_place = 1
    inputs_available = [0]
    for item in player.inventory:
        inputs_available.append(inv_place)
        inv_print += f"|{inv_place}:{items[item[0]][item_name]} * {item[1]}"
        inv_place += 1
    if inv_print == "":
        print("inventory is empty")
    else:
        print(f"Inventory \n0:Back\n{inv_print}")
        input1 = input_manager(inputs_available)
        if input1 == 0:
            map_printer()
        else:
            inventory_use(player.inventory[input1 - 1])


def inventory_use(item_used):
    word = "use"
    if items[item_used[0]][item_type] == "weapon" or items[item_used[0]][item_type] == "armor":
        if player.weapon == item_used[0] or player.armor == item_used[0]:
            word = "unequip"
        else:
            word = "equip"
    print(f"Would you like to {word} {items[item_used[0]][item_name]} \n1:Yes\n2:No")
    input1 = input_manager([1, 2])
    if input1 == 1:
        if items[item_used[0]][item_type] == "weapon":
            if word == "unequip":
                player.weapon = "008"
            else:
                player.weapon = item_used[0]
        elif items[item_used[0]][item_type] == "armor":
            if word == "unequip":

                player.armor = "009"
            else:
                player.armor = item_used[0]
        elif items[item_used[0]][item_type] == "aid":
            aid_applier(item_used[0])
            item_used[1] -= 1
        else:
            pass
    else:
        pass
    for item in player.inventory:
        if item[1] == 0:
            player.inventory.remove(item)
    map_printer()


def aid_applier(item_id):
    stats = items[item_id][aid_stats]
    if item_id == "002":
        player.health += stats[0]
        if player.health > player.max_health:
            player.health = player.max_health
    elif item_id == "003":
        player.health += stats[0]
        player.max_health += stats[1]
        if player.health > player.max_health:
            player.health = player.max_health
    elif item_id == "004":
        player.sturdiness += stats[0]
        player.acuity -= stats[0]
    elif item_id == "005":
        player.sturdiness -= stats[0]
        player.acuity += stats[0]
    elif item_id == "006":
        player.endearment += stats[0]
        player.luck -= stats[0]
    elif item_id == "007":
        player.endearment -= stats[0]
        player.luck += stats[0]
    else:
        pass


def check_manager():
    if str(armera_map[player.area][area_map][player.pos1][player.pos2]) == "0":
        print("Nothing of interest")
    elif str(armera_map[player.area][area_map][player.pos1][player.pos2]) == "!":
        loot_manager()
    elif str(armera_map[player.area][area_map][player.pos1][player.pos2]) == "?":
        quest_manager()


def loot_manager():
    loot_table = armera_map[player.area][loot_pool]
    probability_int = 10 - round(player.luck / 2)
    picker1 = random.randint(0, probability_int)
    in_inventory = False
    if picker1 == 1:
        picker2 = random.randint(0, len(loot_table[1]) - 1)
        chosen_item = str(loot_table[1][picker2])
    else:
        picker2 = random.randint(0, len(loot_table[0]) - 1)
        chosen_item = str(loot_table[0][picker2])
    for item in player.inventory:
        if item[0] == chosen_item:
            item[1] += 1
            in_inventory = True
    if not in_inventory:
        new_entry = [chosen_item, 1]
        player.inventory.append(new_entry)
    armera_map[player.area][area_map][player.pos1][player.pos2] = 0
    print(f"{player.name} found somthing! \n{items[chosen_item][item_name]} added to inventory ")


def quest_manager():
    pass


def game_end():
    lines = [99, 100, 101, 102, 103, 104, 106]
    sprite_renderer(lines)
    input1 = input_manager([1, 2])
    if input1 == 1:
        continue_manager()
    else:
        title()


# main game loop
def game_loop():
    global game_over

    map_printer()
    while not game_over:
        action_manager()


title()
