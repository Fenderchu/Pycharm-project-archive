from opensimplex import OpenSimplex
from .constants import *
import random, math, pygame

screen_surface = pygame.Surface((width, height))


class Tilemap():
    def __init__(self):
        self.tile_map = []
        self.map_made = False
        self.make_map()
        self.display_map()

    def make_map(self):
        seed_gen = random.randint(1, 10000)
        map_gen = OpenSimplex(seed=seed_gen)
        counter1 = 0
        col_count = 0
        row_count = 0
        for counter1 in range(0, height//10):
            self.tile_map.append([])
            counter1 += 1
        for row in self.tile_map:
            for row_count in range(0, width//10):
                row.append(abs(math.trunc(map_gen.noise2d(row_count, col_count) * 10)))
                row_count += 1

            col_count += 1

    def display_map(self):
        col_count = 0
        row_count = 0
        if not self.map_made:
            for row in self.tile_map:
                for _ in row:
                    screen_surface.blit(grass_tile, ((width//10)*row_count, (width//10)*col_count))
                    row_count += 1
                col_count += 1
                row_count = 0

        window.blit(screen_surface, (0, 0))
        pygame.display.update()
