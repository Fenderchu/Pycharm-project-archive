import random, opensimplex
from Main_scripts.constants import *



noise = opensimplex.OpenSimplex(int(random.randint(0,100000)))
scail = 0.1

def build_map():
    z = y = x = 0
    for i in range(0, map_depth):
        world_map.append([])

    for plain in world_map:

        for i in range(0, map_height+2):
            plain.append([])
        for row in plain:
            for i in range(0, map_width+2):
                row.append(abs(round(noise.noise3d(x * scail, y * scail, z * scail) * 10)))
                x += 1
            y += 1
            x = 0
        z += 1
        y = 0
        x = 0
    build_tile_map()


def build_tile_map():
    z = y = x = 0
    for i in range(0, map_depth):
        tile_map.append([])

    for plain in tile_map:
        for i in range(0, map_height):
            plain.append([])
        for row in plain:
            for i in range(0, map_width):
                pos = world_map[z][y][x]
                if pos == 0:
                    image = Sea1
                elif pos == 1:
                    image = Sea2
                elif pos == 2:
                    image = Land5
                elif pos == 3:
                    image = Land4
                elif pos == 4:
                    image = Land3
                elif pos == 5:
                    image = Land2
                else:
                    image = Land1
                row.append(image)

                x += 1
            y += 1

            x = 0

        z += 1
        y = 0
        x = 1


def draw_map(z):
    x = y = 0
    for row in tile_map[z]:
        for image in row:
            tile_map_surface.blit(image, (x * 16, y * 16))
            x += 1
        y += 1
        x = 0









