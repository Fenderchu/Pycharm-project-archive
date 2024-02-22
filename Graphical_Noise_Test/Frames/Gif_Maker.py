import glob
import os
from PIL import Image

# '/Users/haydenb/PycharmProjects/Graphical_Noise_Test/'


def make_gif():
    gif_name = input("Filename?\n>>>")

    # file paths
    fp_in = "/Users/haydenb/PycharmProjects/Graphical_Noise_Test/Frames/*.png"
    fp_out = "/Users/haydenb/PycharmProjects/Graphical_Noise_Test/" + gif_name + ".gif"

    img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
    img.save(fp=fp_out, format='GIF', append_images=imgs,
             save_all=True, duration=1, loop=0)

    for f in glob.glob(fp_in):
        os.remove(f)


