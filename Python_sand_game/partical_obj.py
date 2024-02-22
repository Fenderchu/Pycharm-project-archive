from tkinter import FALSE
import pygame, pymunk, random, math




class Partical():
    def __init__(self, rotate, w_mod, h_mod, col_id, type = pymunk.Body.DYNAMIC, is_circle = False):
        if h_mod < 0:
            h_mod = 0
        if w_mod < 0:
            w_mod = 0
        
        if is_circle:
            w_mod = h_mod
        elif rotate:
            w_mod, h_mod = h_mod, w_mod

        self.is_circle = is_circle

        self.size = (5 + w_mod, 5 + h_mod) 
        
        self.body = pymunk.Body(body_type=type)
        
        self.colour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

        self.surface = pygame.Surface(self.size)
        self.surface.set_colorkey((0, 0, 0, 0))
        
        self.image = 0

        self.col_id = col_id

        self.is_selected = False
        self.pinning = False
        
        if is_circle:
            pygame.draw.circle(self.surface ,self.colour ,(self.size[0]//2, self.size[1]//2), self.size[1]//2)
            self.shape = pymunk.Circle(self.body, self.size[1]//2)
        else:
            self.shape = pymunk.Poly.create_box(self.body, self.size)
            self.surface.fill(self.colour)

        self.shape.mass = 10 + (h_mod * w_mod)/10
        self.shape.friction = 1
        self.shape.elasticity = 0.1
        self.shape.collision_type = col_id
        self.rect = self.surface.get_rect()


    def update(self, cords):

        if self.is_circle:
            self.size = (self.size[1], self.size[1])

        self.image =  pygame.transform.rotate(self.surface, math.degrees(self.body.angle))
       
        self.rect = self.image.get_rect(center = (cords + self.body.center_of_gravity))
    
    def selected(self, arbiter, space, data):

        self.is_selected = True

        self.shape.collision_type = 2
        return False

    def deselected(self):
        self.is_selected = False

        self.shape.collision_type = self.col_id

    def pin_selected (self, arbiter, space, data):
        self.pinning = True
        self.shape.collision_type = 3
        return False
    
    
    def disable_col(self, arbiter, space, data):
        return False
        