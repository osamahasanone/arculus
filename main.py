import sys
from ping_pong.enums import TabelSide
import argparse


parser = argparse.ArgumentParser()

# Add these options to create paddles on target sides
parser.add_argument("-l", "--left", action="store_true", help="Add left paddel")
parser.add_argument("-r", "--right", action="store_true", help="Add right paddel")
parser.add_argument("-b", "--bottom", action="store_true", help="Add bottom paddel")
parser.add_argument("-t", "--top", action="store_true", help="Add top paddel")

# parse command arguments
args = parser.parse_args()

sides = []
if args.left:
    sides.append(TabelSide.LEFT)
if args.right:
    sides.append(TabelSide.RIGHT)
if args.bottom:
    sides.append(TabelSide.BOTTOM)
if args.top:
    sides.append(TabelSide.TOP)

if not sides:
    print("Please add one paddel at least.")
    sys.exit()

# play
from ping_pong.game import Game

game = Game(sides=sides)
game.start()
