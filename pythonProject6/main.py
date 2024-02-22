import time

import pygame
import noise
import math
from numpy import *

current_frame = []
last_frame = []

pixel_w, pixel_h = 5, 5
w, h, d = 200, 100, 0
offset_x = random.randint(0, 100000)
offset_y = random.randint(0, 100000)

colour_bool = True
still = False


def main_loop():
    global current_frame, last_frame, d, r, g, b, colour_bool, still

    clock = pygame.time.Clock()

    win = pygame.display.set_mode((w * pixel_w, h * pixel_h))

    s1 = pygame.surface.Surface((pixel_w, pixel_h))
    main_s = pygame.surface.Surface((w * pixel_w, h * pixel_h))

    s1.set_colorkey((0, 0, 0))
    main_s.set_colorkey((0, 0, 0))

    for i in range(0, h + 1):
        last_frame.append([])

    for col in last_frame:
        for i in range(0, w + 1):
            col.append(0.1)

    run = True

    r, g, b = 0, 0, 0

    min_num, max_num = -10, 10

    while run:
        clock.tick(60)

        start = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    d += 1
                elif event.key == pygame.K_LEFT:
                    d -= 1
                if event.key == pygame.K_c:
                    if colour_bool:
                        colour_bool = False
                    else:
                        colour_bool = True

                    last_frame = []

                    for i in range(0, h + 1):
                        last_frame.append([])

                    for col in last_frame:
                        for i in range(0, w + 1):
                            col.append(0.1)

                if event.key == pygame.K_x:
                    if still:
                        still = False
                    else:
                        still = True

                    last_frame = []

                    for i in range(0, h + 1):
                        last_frame.append([])

                    for col in last_frame:
                        for i in range(0, w + 1):
                            col.append(0.1)

        noise_gen(d)
        if not last_frame == current_frame:
            for i in range(0, h):
                pos_y = i * pixel_h
                for j in range(0, w):

                    if not last_frame[i][j] == current_frame[i][j]:

                        num = current_frame[i][j]

                        pos_x = j * pixel_w

                        if colour_bool:
                            if num < min_num:
                                min_num = num
                            elif num > max_num:
                                max_num = num
                            segment = round((abs(min_num) + abs(max_num)) // 8)

                            med = round((max_num + min_num) // 2) + segment * 2.5
                            colour = 100
                            if med + (segment * 2) >= num >= med:
                                r = -35
                                g = 80
                                b = 20
                            elif med - segment <= num <= med:
                                r = 145
                                g = 120
                                b = 10
                            elif num <= med - segment:
                                r = -80
                                g = -35
                                b = 90
                            elif med + (segment * 4) >= num >= med + (segment * 2):
                                r = g = b = 45
                            elif num > med + (segment * 5):
                                r = g = b = 140
                            else:
                                r = g = b = 0

                            s1.fill((colour + r + random.randint(-10, 10), colour + g + random.randint(-10, 10),
                                     colour + b + random.randint(-10, 10)))

                        else:
                            colour = 100 + (current_frame[i][j] * 5)
                            s1.fill((colour, colour, colour))

                        main_s.blit(s1, (pos_x, pos_y))
            if not still:
                d += 1
            win.blit(main_s, (0, 0))

        pygame.display.update()
        last_frame = current_frame.copy()
        end = time.time()
        print("ping", end - start)

    pygame.quit()


def noise_gen(z=0):
    global current_frame, noise, last_frame

    scale = 0.06
    octaves = 10
    persistence = 0.5
    lacunarity = 2.0

    current_frame = []

    for y in range(0, h + 1):
        current_frame.append([])
        for x in range(0, w + 1):
            num = round(10 * (2 * noise.pnoise3(offset_y + y * scale, offset_x + x * scale, z * 0.01,
                                                octaves=octaves,
                                                persistence=persistence,
                                                lacunarity=lacunarity,
                                                repeatx=1024,
                                                repeaty=1024,
                                                base=0)))

            current_frame[y].append(num)


main_loop()
