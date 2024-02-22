from .constants import *
from .tilemap import screen_surface
import pygame

vector = pygame.Vector2


class Player():
    def __init__(self):
        self.surface = pygame.Surface((20, 20))
        self.position = vector(width / 2, height / 2)
        self.body = friend_mb
        self.turret = friend_mt
        self.body_rect = friend_mb.get_rect()
        self.turret_rect = friend_mt.get_rect()
        self.body_rotation = 0
        self.turret_rotation = 0
        self.rotation = 0
        self.rotation_speed = 0
        self.reverse = 0
        self.speed = vector(1, 0)
        self.acceleration = vector(0, -0.2)
        self.deceleration = 0
        self.x = 100
        self.y = 100
        self.surface.set_colorkey((0, 0, 0))
        self.spawn_player()

    def spawn_player(self):
        self.surface.blit(self.body, (0, 0))
        self.surface.blit(self.turret, (0, 0))
        screen_surface.blit(self.surface, (self.x, self.y))

    def update(self):
        self.move()
        self.rotate()

    def rotate(self):
        # Rotate the acceleration vector.
        self.acceleration.rotate_ip(self.rotation_speed)
        self.rotation += self.rotation_speed
        if self.rotation > 360:
            self.rotation -= 360
        elif self.rotation < 0:
            self.rotation += 360
        self.surface = pygame.transform.rotate(self.body, -self.rotation)
        self.body_rect = self.surface.get_rect(center=self.body_rect.center)

    def move(self):
        for event in pygame.event.get():
            if event == pygame.K_w:
                self.speed += self.acceleration
                print("here")
            elif event.type == pygame.K_s:
                self.speed -= self.acceleration
        self.position += self.speed
        self.body_rect.center += self.position
        self.turret_rect.center += self.position
