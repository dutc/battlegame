# arg parse for battlegame
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--size', type=str, help="declare size of board", required=True)
parser.add_argument('--play', action='store_true', help="allow the user to play a 'one player' game interactively")
parser.add_argument('--show', action='store_true', help="print out the board")
parser.add_argument('--carrier', type=str, help="boat Carrier")
parser.add_argument('--battleship', type=str, help="boat Battleship")
parser.add_argument('--cruiser', type=str, help="boat cRuiser")
parser.add_argument('--submarine', type=str, help="boat Submarine")
parser.add_argument('--destroyer', type=str, help="boat Destroyer")