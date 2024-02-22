from Main_scripts.constants import *
from Main_scripts import map_builder as mb
import Main_scripts.constants as const
import random


class Player:
    def __init__(self):
        self.pos = [25, 25, 5]
        self.sub_pos = [0, 0]
        self.hp = 100
        self.direction = ["N", "N"]
        self.prev_direction = ["N", "N"]
        self.speed = 1
        self.state = "move"
        self.inventory = []
        self.image = Bright_F
        self.rect = self.image.get_rect()
        self.frame_count = 20
        self.inv_frames = 30
        self.hit_bool = False

    def find_spawn(self):
        invalid = True
        while invalid:
            if world_map[self.pos[2]][self.pos[1]][self.pos[0]] < 2:
                self.pos[0] = random.randint(0,map_width)
                self.pos[1] = random.randint(0,map_height)
                if self.pos[0] > map_width:
                    self.pos[0] = 0
                    self.pos[1] += 1
            else:
                invalid = False

    def update_image(self):

        if self.state == "idle":
            if self.prev_direction[1] == "N":
                pass
            elif self.prev_direction[1] == "F":
                self.image = Bright_F
            elif self.prev_direction[1] == "B":
                self.image = Bright_B

            if self.prev_direction[0] == "N":
                pass
            elif self.prev_direction[0] == "R":
                self.image = Bright_R
            elif self.prev_direction[0] == "L":
                self.image = Bright_L

        elif self.state == "move":

            if self.direction[1] == "N":
                pass
            elif self.direction[1] == "F":
                if self.frame_count > 10:
                    self.image = Bright_Run_F_1
                else:
                    self.image = Bright_Run_F_2

            elif self.direction[1] == "B":
                if self.frame_count > 10:
                    self.image = Bright_Run_B_1
                else:
                    self.image = Bright_Run_B_2

            if self.direction[0] == "N":
                pass
            elif self.direction[0] == "R":
                if self.frame_count > 10:
                    self.image = Bright_Run_R_1
                else:
                    self.image = Bright_Run_R_2

            elif self.direction[0] == "L":
                if self.frame_count > 10:
                    self.image = Bright_Run_L_1
                else:
                    self.image = Bright_Run_L_2

            self.frame_count -= 1
            if self.frame_count <= 0:
                self.frame_count = 20

    def move(self):
        f_sub_pos = [self.sub_pos[0], self.sub_pos[1]]
        f_pos = [self.pos[0], self.pos[1], self.pos[2]]
        col_flag = False

        if self.direction[0] == "N" and self.direction[1] == "N" and not self.hit_bool:
            self.state = "idle"
        else:
            self.state = "move"
            if self.direction[0] == "N" or self.direction[1] == "N":
                if self.direction[0] == "R":
                    if not self.hit_bool:
                        f_sub_pos[0] += self.speed
                    else:
                        f_sub_pos[0] -= self.speed
                elif self.direction[0] == "L":
                    if not self.hit_bool:
                        f_sub_pos[0] -= self.speed
                    else:
                        f_sub_pos[0] += self.speed
                if self.direction[1] == "F":
                    if not self.hit_bool:
                        f_sub_pos[1] += self.speed
                    else:
                        f_sub_pos[1] -= self.speed
                elif self.direction[1] == "B":
                    if not self.hit_bool:
                        f_sub_pos[1] -= self.speed
                    else:
                        f_sub_pos[1] += self.speed

            else:
                if self.direction[0] == "R":
                    if not self.hit_bool:
                        f_sub_pos[0] += self.speed * (2 ** 0.5)
                    else:
                        f_sub_pos[0] -= self.speed * (2 ** 0.5)
                elif self.direction[0] == "L":
                    if not self.hit_bool:
                        f_sub_pos[0] -= self.speed * (2 ** 0.5)
                    else:
                        f_sub_pos[0] += self.speed * (2 ** 0.5)
                if self.direction[1] == "F":
                    if not self.hit_bool:
                        f_sub_pos[1] += self.speed * (2 ** 0.5)
                    else:
                        f_sub_pos[1] -= self.speed * (2 ** 0.5)
                elif self.direction[1] == "B":
                    if not self.hit_bool:
                        f_sub_pos[1] -= self.speed * (2 ** 0.5)
                    else:
                        f_sub_pos[1] += self.speed * (2 ** 0.5)

            if f_sub_pos[0] > 15:
                f_sub_pos[0] = 0
                f_pos[0] += 1

            elif f_sub_pos[0] < 0:
                f_sub_pos[0] = 15
                f_pos[0] -= 1

            if f_sub_pos[1] > 15:
                f_sub_pos[1] = 0
                f_pos[1] += 1

            elif f_sub_pos[1] < 0:
                f_sub_pos[1] = 15
                f_pos[1] -= 1

            if f_pos[0] >= map_width:
                f_pos[0] = 0
                f_sub_pos[0] = 0
            elif f_pos[1] >= map_height:
                f_pos[1] = 0
                f_sub_pos[0] = 15

            if f_pos[0] < 0:
                f_pos[0] = map_width - 1
                f_sub_pos[1] = abs(f_sub_pos[1] - 15)

            elif f_pos[1] < 0:
                f_pos[1] = map_height - 1
                f_sub_pos[1] = abs(f_sub_pos[1] - 15)

            if world_map[f_pos[2]][f_pos[1]][f_pos[0]] < 2:
                col_flag = True

            if not col_flag:
                f_sub_pos = [round(f_sub_pos[0]), round(f_sub_pos[1])]
                self.pos = f_pos
                self.sub_pos = f_sub_pos

            if self.hit_bool:
                if self.inv_frames > 0:
                    self.inv_frames -= 1
                else:
                    self.hit_bool = False
                    self.hp -= 1

    def shift(self, direct):
        if 5 < world_map[self.pos[2]][self.pos[1]][self.pos[0]] < 10:
            if direct == -1:
                if self.pos[2] - 1 > 0:
                    self.pos[2] -= 1
                    mb.draw_map(self.pos[2])
            if direct == 1:
                if self.pos[2] + 2 <= map_depth:
                    self.pos[2] += 1
                    mb.draw_map(self.pos[2])
        else:
            pass
        const.active_z = self.pos[2]

    def place_bridge(self):
        check_pos = [self.pos[0], self.pos[1], self.pos[2]]

        if self.prev_direction[0] == "R":
            check_pos[0] += 1
        elif self.prev_direction[0] == "L":
            check_pos[0] -= 1
        elif self.prev_direction[1] == "F":
            check_pos[1] += 1
        elif self.prev_direction[1] == "B":
            check_pos[1] -= 1

        if check_pos[0] < 0:
            check_pos[0]  =-1
        if check_pos[1] < 0:
            check_pos[1] = -1
        if check_pos[0] + 1 > map_width:
            check_pos[0] = 0
        elif check_pos[1] + 1 > map_height:
            check_pos[1] = 0

        if world_map[check_pos[2]][check_pos[1]][check_pos[0]] < 2:
            tile_map[check_pos[2]][check_pos[1]][check_pos[0]] = Bridge_sprite
            world_map[check_pos[2]][check_pos[1]][check_pos[0]] = 11
            mb.draw_map(self.pos[2])

    def harvest(self):
        pos = world_map[self.pos[2]][self.pos[1]][self.pos[0]]

    def hit(self):
        self.inv_frames = 5
        self.hit_bool = True

    def draw_self(self):
        position = ((self.pos[0] * 16) + self.sub_pos[0] - 8, (self.pos[1] * 16) + self.sub_pos[1] - 16)
        entity_surface.blit(self.image, position)
        self.rect.topleft = position
        if self.inv_frames > 0:
            self.inv_frames -= 1

    def update(self):
        self.move()
        self.update_image()
        self.draw_self()
