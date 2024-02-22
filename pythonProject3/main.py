import random


def size_choser():
    choice = ""
    while choice.lower() not in ["small", "medium", "large"]:
        choice = input("what size? [small, medium, or large]")
    if choice.lower() == "small":
        choice = 1
    elif choice == "medium":
        choice = 2
    else:
        choice = 3
    chunk_gen(choice)


def chunk_gen(size):
    save = open("save", "a")
    count = (100 * size) + (9 * size)
    spacer1 = 1
    spacer2 = 1
    save.truncate(0)
    while count > 0:
        numb = random.randint(0, 9)
        if spacer1 == (10 * size):
            save.write(f"\n{numb}")
            spacer1 -= (10 * size)
        else:
            save.write(str(numb))
        count -= 1
        spacer1 += 1
        spacer2 += 1
    save.write("\n|\n")
    save.close()
    map_print(size)


def map_print(size):
    save = open("save", "r")
    map_ = open("map", "a")
    map_.truncate(0)
    spacer = 1

    for character in save:
        for num in character:
            if num.isnumeric():
                if spacer <= 10 * size:
                    map_.write(f"[{num}]")
                    spacer += 1
                else:
                    map_.write("\n")
                    spacer -= 10 * size
    map_.close()
    save.close()
    map_read()


def map_read():
    Map = ""
    map_ = open("map", "r")
    counter = 0
    space1 = 0

    for line in map_:
        for character in line:
            if character.isnumeric():
                space1 += 1

    for line in map_:
        for character in line:
            if character.isnumeric() and counter < 20:
                Map += f"[{character}]"
                counter += 1
            elif counter == 20:
                Map += "\n"
                counter -= 20

    print(Map)


size_choser()
map_read()
