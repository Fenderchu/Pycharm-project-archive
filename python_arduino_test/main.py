import random
import time
from constants import *
import pyfirmata
from multiprocessing import Process
from opensimplex import OpenSimplex
from Stepper_Control import step_motor

a = 0
x = 1


def main_loop():
    global x
    noise_gen(g_seed)
    while run:
        while x in range(0, length):
            get_a()
            pin9.write(a)
            time.sleep(speed)

            x += 1


def get_a():
    global a
    if 0 < x <= length:
        a = 90 + plane[x - 1]
    else:
        a = 90


def gen_seed():
    global g_seed
    g_seed = random.randint(1, 100000)


def noise_gen(s):
    global x, plane
    noise = OpenSimplex(seed=s)
    for i in range(0, length):
        plane.append(noise.noise2d(i, 0) * 50)

    print(plane)


Process(target=step_motor()).start()
Process(target=main_loop()).start()

