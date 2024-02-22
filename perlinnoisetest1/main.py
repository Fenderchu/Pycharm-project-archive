import pygame
import random
from perlin_noise import PerlinNoise

width, height = 100, 100
square_size = 2
scale = 1

window = pygame.display.set_mode((width, height))
display_surface = pygame.surface.Surface((width, height))

noise = PerlinNoise(octaves=10, seed=random.randint(1, 1000))


def board_1d():
    board = []
    square_surface = pygame.surface.Surface((square_size, square_size))
    square_surface.fill((255, 255, 255))
    for i in range(0, width):
        board.append(noise([i/width]))
        print(board[i])

    x = 0

    for num in board:

        display_surface.blit(square_surface, (x * square_size, (num * scale) + width/2))
        x += 1

    window.blit(display_surface, (0, 0))


def board_2d():
    board = []
    x, y = 0, 0

    square_surface = pygame.surface.Surface((square_size, square_size))

    for i in range(0, height):
        board.append([])

    for row in board:

        for i in range(0, width):
            row.append(noise([x, y]))

        for col in row:
            colour_val = abs(127.5 * col)
            square_surface.fill((colour_val, colour_val, colour_val))
            display_surface.blit(square_surface, (x*square_size, y*square_size))
            x += 1
        print(y/height)
        y += 1
        x = 0
    window.blit(display_surface, (0, 0))


def main_loop():
    run = True

    board_2d()

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        pygame.display.update()
    pygame.quit()


main_loop()
