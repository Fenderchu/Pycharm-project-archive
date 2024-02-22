
import renderer, pygame, os, Frames.Gif_Maker




def frame_animator():
    print(str(renderer.frames / renderer.frame_advanced))
    while renderer.animate:
        if renderer.z < renderer.frames:
            renderer.z += renderer.frame_advanced

            renderer.build_board()

            renderer.surface_build()
            if renderer.save:
                print(round(renderer.z * renderer.frames / renderer.frames, 2))
                file_name = str(round(renderer.z, 2)) + ".png"
                pygame.image.save(renderer.display_surface, file_name)
                os.rename("/Users/haydenb/PycharmProjects/Graphical_Noise_Test/" + file_name, "/Users/haydenb/PycharmProjects/Graphical_Noise_Test/Frames/" + file_name)
        elif renderer.save:
            renderer.animate = False

            Frames.Gif_Maker.make_gif()

        else:
            renderer.z = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                renderer.animate = False
                renderer.run = False
                break
