import pygame

win_width, win_height = 800, 800

win = pygame.display.set_mode((win_width, win_height))
Loading_image = pygame.image.load("Abridged_sprites/Loading_temp.png").convert()

main_surface = pygame.surface.Surface((win_width, win_height))

# map values
map_scale = 1
map_width, map_height, map_depth = round(win_width / 16*map_scale), round(win_height / 16*map_scale), 10
world_map = []
tile_map = []
tile_map_surface = pygame.surface.Surface((win_width, win_height))
entity_surface = pygame.surface.Surface((win_width, win_height))
entity_surface.set_colorkey((0, 0, 0))

active_z = 5


Land1 = pygame.image.load("Abridged_sprites/Land1.png").convert()
Land2 = pygame.image.load("Abridged_sprites/Land2.png").convert()
Land3 = pygame.image.load("Abridged_sprites/Land3.png").convert()
Land4 = pygame.image.load("Abridged_sprites/Land4.png").convert()
Land5 = pygame.image.load("Abridged_sprites/Land5_rev2.png").convert()
Sea1 = pygame.image.load("Abridged_sprites/Sea1.png").convert()
Sea2 = pygame.image.load("Abridged_sprites/Sea2.png").convert()

# player values

Bright_B = pygame.image.load("Abridged_sprites/Bright_B.png")
Bright_F = pygame.image.load("Abridged_sprites/Bright_F.png")
Bright_R = pygame.image.load("Abridged_sprites/Bright_R.png")
Bright_L = pygame.image.load("Abridged_sprites/Bright_L.png")

Bright_Run_R_1 = pygame.image.load("Abridged_sprites/Animations/Bright_Run_R_1.png")
Bright_Run_R_2 = pygame.image.load("Abridged_sprites/Animations/Bright_Run_R_2.png")

Bright_Run_L_1 = pygame.image.load("Abridged_sprites/Animations/Bright_Run_L_1.png")
Bright_Run_L_2 = pygame.image.load("Abridged_sprites/Animations/Bright_Run_L_2.png")

Bright_Run_F_1 = pygame.image.load("Abridged_sprites/Animations/Bright_Run_F_1.png")
Bright_Run_F_2 = pygame.image.load("Abridged_sprites/Animations/Bright_Run_F_2.png")

Bright_Run_B_1 = pygame.image.load("Abridged_sprites/Animations/Bright_Run_B_1.png")
Bright_Run_B_2 = pygame.image.load("Abridged_sprites/Animations/Bright_Run_B_2.png")

Bridge_sprite = pygame.image.load("Abridged_sprites/Bridge.png")

# enemy sprites

Slime_R = pygame.image.load("Abridged_sprites/Animations/Slime_R.png")
Slime_L = pygame.image.load("Abridged_sprites/Animations/Slime_L.png")

Slime_idle_R_1 = pygame.image.load("Abridged_sprites/Animations/Slime_idle_R_1.png")
Slime_idle_L_1 = pygame.image.load("Abridged_sprites/Animations/Slime_idle_L_1.png")

Slime_move_R_1 = pygame.image.load("Abridged_sprites/Animations/Slime_move_R_1.png")
Slime_move_L_1 = pygame.image.load("Abridged_sprites/Animations/Slime_move_L_1.png")

Shrub_sprite = pygame.image.load("Abridged_sprites/Shrub1.png")

Flowers = pygame.image.load("Abridged_sprites/Flowers.png")

passive_surface = pygame.surface.Surface((map_width, map_height))
