import pyfirmata

board = pyfirmata.Arduino('/dev/tty.usbmodem411')

board.digital[9].mode = pyfirmata.OUTPUT
board.digital[3].mode = pyfirmata.INPUT
board.digital[2].mode = pyfirmata.OUTPUT
board.digital[3].mode = pyfirmata.OUTPUT
board.digital[4].mode = pyfirmata.OUTPUT
board.digital[5].mode = pyfirmata.OUTPUT

pin9 = board.get_pin('d:9:s')

plane = []

g_seed = 0

length = 1000

step = 0
run = True
# keep in range 0-1
speed = 0.005