from Main_scripts.constants import *
import random


class Gather_Node:
    def __init__(self, ty, z):
        self.type = ty
        self.pos = [random.randint(0, map_width), random.randint(0, map_height), z]
        self.sub_pos = [random.randint(0, 15), random.randint(0, 15)]
        self.image = Shrub_sprite
        self.resource = ty
        self.stored_resource = 50
        self.spawned = False
        self.rect = self.image.get_rect()
        self.position = ((self.pos[0] * 16) + self.sub_pos[0] - 8, (self.pos[1] * 16) + self.sub_pos[1] - 16)

        if self.type == 1:
            self.image = Shrub_sprite
        else:
            self.image = Flowers

    def find_spawn(self):
        invalid = True

        while invalid:
            if world_map[self.pos[2]][self.pos[1]][self.pos[0]] < 2:
                self.pos[0] = random.randint(0, map_width)
                self.pos[1] = random.randint(0, map_height)
            else:
                invalid = False
                self.position = ((self.pos[0] * 16) + self.sub_pos[0] - 8, (self.pos[1] * 16) + self.sub_pos[1] - 16)

    def draw_self(self):
        entity_surface.blit(self.image, self.position)

    def update(self):

        if not self.spawned:
            self.find_spawn()
            self.rect.topleft = (self.pos[0], self.pos[1])
            self.spawned = True
        self.draw_self()
