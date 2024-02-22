import pygame

width, height = 800, 800
window = pygame.display.set_mode((width, height))

friend_lb = pygame.image.load('frendly-light-tank-body.png')
friend_lt = pygame.image.load('frendly-light-tank-turret.png')
friend_mb = pygame.image.load('frendly-medium-tank-body.png')
friend_mt = pygame.image.load('frendly-medium-tank-turret.png')
grass_tile = pygame.image.load('grass-tile.png').convert()
grass_tile = pygame.transform.scale(grass_tile,(width//10,height//10))
black = (0, 0, 0)
