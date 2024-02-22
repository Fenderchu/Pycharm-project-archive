import random
import os
import pygame
from pygame import transform

pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("GAME ver 4.3")

x = 250
y = 400
width = 20
height = 40
velocity = 0
velocity_cap = 12
screan_width = 500
screan_height = 500
window = pygame.display.set_mode((500, 500))
isjumping = False
jump_size = 10
jump_count = jump_size

left = False
right = True
idle = True
walk_count = 0

walking = [
    pygame.image.load("Luigi - Walk1-R.gif"),
    pygame.image.load("Luigi - Walk2-R.gif"),
    pygame.image.load("Luigi - Walk3-R.gif")
]

idle_sprite = [
    pygame.image.load("Luigi-idle-R.gif")
]
jump = [
    pygame.image.load("Luigi - Jump-R.gif")
]
bg = pygame.transform.scale(pygame.image.load("Backround-Mario.png"), (1000, 500))


def redraw():
    global walk_count
    global x
    global velocity
    window.blit(bg, (0, 0))

    if walk_count + 1 >= 3:
        walk_count = 0
    if isjumping:
        if right:
            x += velocity
            if velocity < velocity_cap - 10:
                velocity += 1
            else:
                velocity = 0
            window.blit(jump[0], (x, y))
        elif left:
            x -= velocity
            if velocity < velocity_cap - 10:
                velocity -= 1
            else:
                velocity = 5
            window.blit(transform.flip(jump[0], True, False), (x, y))
    elif idle:
        if right:
            x += velocity
            if velocity > 0:
                velocity -= 3
            elif velocity < 0:
                velocity += 3
            window.blit(idle_sprite[0], (x, y))
        elif left:
            x -= velocity
            if velocity > 0:
                velocity -= 3
            elif velocity < 0:
                velocity += 3
            window.blit(transform.flip(idle_sprite[0], True, False), (x, y))
    elif right:

        window.blit(walking[walk_count], (x, y))
        walk_count += 1
    elif left:
        window.blit(transform.flip(walking[walk_count], True, False), (x, y))
        walk_count += 1
    pygame.display.update()



run = True
while run:
    keys = pygame.key.get_pressed()
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if keys[pygame.K_LEFT]:
        x -= velocity
        left = True
        right = False
        idle = False
        if velocity < velocity_cap:
            velocity += 1

    elif keys[pygame.K_RIGHT] and x < screan_width - width :
        x += velocity
        left = False
        right = True
        idle = False
        if velocity < velocity_cap:
            velocity += 1

    else:
        walkcount = 0
        idle = True
    if isjumping:
        if jump_count >= (-1 * jump_size):
            neg = 1
            if jump_count < 0:
                neg = -1

            y -= ((jump_count ** 2) * 0.5) * neg
            jump_count -= 1
        else:
            isjumping = False
            jump_count = jump_size

    if keys[pygame.K_UP]:
        isjumping = True

    redraw()

pygame.quit()
