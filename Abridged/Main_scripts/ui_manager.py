import pygame


class UI_Object:
    def __init__(self, ty, pos):
        self.pos = pos
        self.type = ty
        self.sanity = 100
        self.sanity_bar = pygame.surface.Surface((25, 50))
        self.sanity_bar_border = pygame.surface.Surface((25, 50))

    def update(self):
        pass
