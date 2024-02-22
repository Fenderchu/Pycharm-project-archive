from constants import speed, run, board
import time, pyfirmata




def step_motor():

    # A B C D
    step = 0
    steps = [[1, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 1],
            [1, 0, 0, 1]]
    while run:
        for _ in steps:
            board.digital[2].write(steps[step][0])
            board.digital[3].write(steps[step][1])
            board.digital[4].write(steps[step][2])
            board.digital[5].write(steps[step][3])

            time.sleep((speed/4))

            step += 1
            if step > 3:
                step = 0
step_motor()