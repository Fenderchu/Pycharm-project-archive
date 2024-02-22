from Main_scripts.constants import *
import random, pygame
import Main_scripts.constants as const


class Enemy:

    def __init__(self, type, pos_z):
        self.type = type
        if type == 1:
            self.name = "slime"
            self.hp = 10
            self.image = Bridge_sprite
        else:
            self.name = "null"
            self.hp = 1
            self.image = Slime_R
        self.sub_pos = [0, 0]
        self.pos = [random.randint(0, map_width), random.randint(0, map_height), pos_z]
        self.rect = self.image.get_rect()
        self.direction = ["N", "N"]
        self.prev_direction = "N"
        self.speed = 2
        self.frame_count = 30
        self.animation_frames = 30
        self.inv_frames = 5
        self.state = "idle"
        self.spawned = False
        random.seed(pygame.time.get_ticks())

    def find_spawn(self):
        invalid = True

        while invalid:
            if self.frame_count > 0:
                self.pos[0] = random.randint(0, map_width)
                self.pos[1] = random.randint(0, map_height)
                self.frame_count -= 5

            elif not world_map[self.pos[2]][self.pos[1]][self.pos[0]] < 2:
                invalid = False
                self.spawned = True
            else:
                self.frame_count = 10

    def random_direction(self):
        num1 = random.randint(0, 13)
        num2 = random.randint(0, 13)

        if 6 < num1 < 8:
            self.direction[0] = "R"
        elif 8 < num1 < 10:
            self.direction[0] = "L"
        elif 10 < num1 < 12:
            self.direction[0] = "F"
        elif num1 > 12:
            self.direction[0] = "B"
        else:
            self.direction[0] = "N"

        if 6 < num2 < 8:
            self.direction[1] = "R"
        elif 8 < num2 < 10:
            self.direction[1] = "L"
        elif 10 < num2 < 12:
            self.direction[1] = "F"
        elif num2 > 12:
            self.direction[1] = "B"
        else:
            self.direction[1] = "N"

    def move(self):
        f_sub_pos = [self.sub_pos[0], self.sub_pos[1]]
        f_pos = [self.pos[0], self.pos[1], self.pos[2]]

        col_flag = False

        if random.randint(0, 4) == 1:
            self.random_direction()

        if self.direction[0] == "N" and self.direction[1] == "N":
            self.state = "idle"

            self.frame_count += 5
        else:
            self.state = "move"
            if self.direction[0] == "N" or self.direction[1] == "N":
                if self.direction[0] == "R":
                    f_sub_pos[0] += self.speed
                elif self.direction[0] == "L":
                    f_sub_pos[0] -= self.speed
                if self.direction[1] == "F":
                    f_sub_pos[1] += self.speed
                elif self.direction[1] == "B":
                    f_sub_pos[1] -= self.speed

            else:
                if self.direction[0] == "R":
                    f_sub_pos[0] += self.speed * (2 ** 0.5)
                elif self.direction[0] == "L":
                    f_sub_pos[0] -= self.speed * (2 ** 0.5)
                if self.direction[1] == "F":
                    f_sub_pos[1] += self.speed * (2 ** 0.5)
                elif self.direction[1] == "B":
                    f_sub_pos[1] -= self.speed * (2 ** 0.5)

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
                if self.direction[0] == "N":
                    self.prev_direction = "R"
                else:
                    self.prev_direction = self.direction[0]

            else:
                self.random_direction()

    def update_image(self):

        if self.state == "idle":

            if self.prev_direction == "N":
                pass
            elif self.prev_direction == "R":
                if self.animation_frames > 10:
                    self.image = Slime_R
                else:
                    self.image = Slime_idle_R_1

            elif self.prev_direction == "L":
                if self.animation_frames > 10:
                    self.image = Slime_L
                else:
                    self.image = Slime_idle_L_1

        elif self.state == "move":

            if self.direction[0] == "R" or self.direction[1] == "F":
                if self.animation_frames > 10:
                    self.image = Slime_R
                else:
                    self.image = Slime_move_R_1

            elif self.direction[0] == "L" or self.direction[1] == "B":
                if self.animation_frames > 10:
                    self.image = Slime_L
                else:
                    self.image = Slime_move_L_1

        self.animation_frames -= 5
        if self.animation_frames <= 0:
            self.animation_frames = 20

    def draw_self(self):
        position = ((self.pos[0] * 16) + self.sub_pos[0] - 8, (self.pos[1] * 16) + self.sub_pos[1] - 16)
        entity_surface.blit(self.image, position)
        self.rect.topleft = position

    def update(self):


        if not self.spawned:
            self.find_spawn()
            self.spawned = True

        self.frame_count -= 1
        if self.frame_count <= 0:
            self.move()
            self.frame_count = 5
        self.update_image()
        self.draw_self()
