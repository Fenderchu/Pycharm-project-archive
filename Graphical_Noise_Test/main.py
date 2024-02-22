import pygame
import renderer
from renderer import animate, window


def main_loop():

    pygame.display.set_caption("map gen")

    while renderer.run and not animate:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                renderer.run = False

                break
    if renderer.save and not animate:
        if input("save?\ny\nn\n>>>") == "y":

            file_name = input("Filename\n>>>")
            pygame.image.save(window, file_name + '.png')

    pygame.quit()


renderer.striping()


main_loop()
