from game_handling.constants import *
from game_handling.tilemap import Tilemap,screen_surface
from game_handling.player import Player


pygame.display.set_caption('TREADS')


def main_loop():
    run = True
    window.fill(black)
    tiles = Tilemap()
    player = Player()
    fps = 60

    while run:
        pygame.time.Clock().tick(fps)
        window.blit(screen_surface,(0,0))
        player.spawn_player()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        player.update()
        pygame.display.update()

    pygame.quit()


main_loop()
