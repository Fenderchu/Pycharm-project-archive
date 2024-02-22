from opensimplex import OpenSimplex
import pygame, random
import animator

width, height = 500, 500
run = True
save = True
screen_active = True

board = []
sun_stripes = []
sky_stripes = []
sky_brightness = 1
window = pygame.display.set_mode((width, height))
display_surface = pygame.surface.Surface((width, height))
display_surface.set_colorkey((0, 0, 0))

# effectively adds more layers of noise
octaves = 0

# thickness of dividing lines, also makes the in between stuff thinner
thickness = 0.1

# the size of each pixel, bigger values drastically improve load time
# higher values also effectively zooms in
square_size = 5
horizon_line = 0
sunrise = False
rise_rate = 0
sun_x, sun_y = width // 2, horizon_line
# basically zooms in and out
scale_x = 0.1
scale_y = 0.1

# rough adjustment to brightness
brightness = 170

# pairs the chosen colour with its complementary
dual_colour = True

# random colour gives a grain artifact effect. more noticeable with bigger square size
random_colour = True
rand_val = 80085
# warning, rainbow is very slow
# like hour long processing times for big resolutions
rainbow = False

# creates more of a pattern with rainbow
noise_unity = True

# animates noise
# warning: this is experimental and frame rate differs wildly
# I suggest using very low resolution, with rainbow off
animate = True
frames = 100
frame_advanced = 0.05
z = 0

sun_r = 300
sun_g = 150
sun_b = 150
colour_r = 100
colour_g = 75
colour_b = 200

gen_seed = int(random.random())


def striping():
    row_count = 0
    for row_count in range(-1, height // square_size):
        sun_stripes.append(random.randint(-1, 5) * 0.05)
        sky_stripes.append(sky_brightness * (random.randint(-1, 5) * 0.001))
        row_count += 1


def build_board():
    global board, octaves, sun_y, sun_x, sky_brightness
    board = []

    grad = 0.01
    noise = OpenSimplex(gen_seed)
    row_count = 0

    while square_size * row_count in range(0, height):
        board.append([])
        row_count += 1

    if not animate:
        print(f"{width // square_size},{row_count}")
        print(row_count * (width // square_size))
    col_count = 0
    row_count = col_count
    for row in board:
        while square_size * col_count in range(0, width):
            if row_count in range(0, horizon_line // square_size):
                sun_col = grad + sun_stripes[row_count]
                sky_col = grad + sky_stripes[row_count]
                if ((col_count - sun_x // square_size) ** 2) + ((row_count - sun_y // square_size) ** 2) <= (
                        50 ** 2) / square_size:
                    row.append(sun_col)
                else:
                    row.append(sky_col)
            else:
                row.append(noise.noise3d(col_count * scale_x, row_count * scale_y, z) * thickness)
            col_count += 1
        row_count += 1
        col_count = 0
        grad += 0.005 * sky_brightness

        if animate and sunrise: #and sun_y > 125:
            sun_y -= rise_rate
            sky_brightness += 0.0005

        if grad > 0.3:
            grad = 0.3
    col_count = 0
    row_count = 0
    noise = OpenSimplex(random.randint(0, 1000))
    while octaves > 0:
        for row in board:
            for col in row:
                if row_count not in range(0, horizon_line):
                    col += noise.noise3d(col_count * scale_x, row_count * scale_y, z) * thickness
                    row[col_count] = col
                col_count += 1
            row_count += 1
            col_count = 0
        octaves -= 1
        print(octaves)


def board_print():
    line = ""
    for row in board:
        for col in row:
            line += str(col)
        print(line)
        line = ""


def surface_build():
    square_surface = pygame.surface.Surface((square_size, square_size))
    row_count = 0
    col_count = 0

    r_seed = random.randint(0, 1000)
    g_seed = random.randint(1000, 2000)
    b_seed = random.randint(2000, 3000)

    for row in board:
        for col in row:
            if not rainbow:
                if random_colour:
                    colour_val_r = (random.randint(0, rand_val) + brightness) * col
                    colour_val_g = (random.randint(0, rand_val) + brightness) * col
                    colour_val_b = (random.randint(0, rand_val) + brightness) * col
                elif dual_colour:
                    colour_val_r = colour_r + brightness * col
                    colour_val_g = colour_g + brightness * col
                    colour_val_b = colour_b + brightness * col
                elif row_count // square_size <= horizon_line-3 // square_size:
                    colour_val_r = (sun_r + brightness) * col
                    colour_val_g = (sun_g + brightness) * col
                    colour_val_b = (sun_b + brightness) * col
                else:
                    colour_val_r = (colour_r + brightness) * col
                    colour_val_g = (colour_g + brightness) * col
                    colour_val_b = (colour_b + brightness) * col

                if random_colour:
                    if colour_val_r < 0:
                        if dual_colour:
                            colour_val_r = abs(random.randint(0, rand_val) + brightness * col)
                        else:
                            colour_val_r = abs((random.randint(0, rand_val) + brightness) * col)

                    if colour_val_g < 0:
                        if dual_colour:
                            colour_val_g = abs(random.randint(0, rand_val) + brightness * col)
                        else:
                            colour_val_g = abs((random.randint(0, rand_val) + brightness) * col)

                    if colour_val_b < 0:
                        if dual_colour:
                            colour_val_b = abs(random.randint(0, rand_val) + brightness * col)
                        else:
                            colour_val_b = abs((random.randint(0, rand_val) + brightness) * col)
                else:
                    if colour_val_r < 0:
                        if dual_colour:
                            colour_val_r = abs(colour_r + brightness * col)
                        else:
                            colour_val_r = abs((colour_r + brightness) * col)

                    if colour_val_g < 0:
                        if dual_colour:
                            colour_val_g = abs(colour_g + brightness * col)
                        else:
                            colour_val_g = abs((colour_g + brightness) * col)

                    if colour_val_b < 0:
                        if dual_colour:
                            colour_val_b = abs(colour_b + brightness * col)
                        else:
                            colour_val_b = abs((colour_b + brightness) * col)

                if colour_val_r > 255 or colour_val_r < -255:
                    colour_val_r = 250

                if colour_val_g > 255 or colour_val_g < -255:
                    colour_val_g = 250

                if colour_val_b > 255 or colour_val_b < -255:
                    colour_val_b = 250
            else:
                if noise_unity:
                    noise_r = noise_g = noise_b = OpenSimplex(gen_seed).noise3d(col_count, row_count, z)
                else:
                    noise_r = OpenSimplex(r_seed).noise3d(col_count, row_count, z)
                    noise_g = OpenSimplex(g_seed).noise3d(col_count, row_count, z)
                    noise_b = OpenSimplex(b_seed).noise3d(col_count, row_count, z)
                if dual_colour:
                    colour_val_r = colour_r + brightness * noise_r
                    colour_val_g = colour_g + brightness * noise_g
                    colour_val_b = colour_b + brightness * noise_b
                else:
                    colour_val_r = (colour_r + brightness) * noise_r
                    colour_val_g = (colour_g + brightness) * noise_g
                    colour_val_b = (colour_b + brightness) * noise_b
                if colour_val_r < 0:
                    if dual_colour:
                        colour_val_r = abs(noise_r + brightness * col)
                    else:
                        colour_val_r = abs((noise_r + brightness) * col)

                if colour_val_g < 0:
                    if dual_colour:
                        colour_val_g = abs(noise_g + brightness * col)
                    else:
                        colour_val_g = abs((noise_g + brightness) * col)

                if colour_val_b < 0:
                    if dual_colour:
                        colour_val_b = abs(noise_b + brightness * col)
                    else:
                        colour_val_b = abs((noise_b + brightness) * col)

                if colour_val_r > 255 or colour_val_r < -255:
                    colour_val_r = 250

                if colour_val_g > 255 or colour_val_g < -255:
                    colour_val_g = 250

                if colour_val_b > 255 or colour_val_b < -255:
                    colour_val_b = 250
            # used for debugging
            # print(f"{colour_val_r} {colour_val_g} {colour_val_b}")\
            colour = (colour_val_r, colour_val_g, colour_val_b)

            square_surface.fill(colour)
            display_surface.blit(square_surface, (col_count, row_count))
            col_count += square_size
        row_count += square_size
        if not animate:
            print(f"{round((row_count / square_size) / (width / square_size) * 100, 2)}/100")
        col_count = 0

    if screen_active:
        window.blit(display_surface, (0, 0))

    if not animate:
        print("Process Successful")
        if save:
            file_name = input("Filename>>>")
            pygame.image.save(display_surface, file_name + ".png")
    pygame.display.update()


if animate and run:
    striping()
    animator.frame_animator()
elif run:
    striping()
    build_board()

    surface_build()
