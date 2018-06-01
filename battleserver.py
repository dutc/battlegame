#Python 3
import pdb, traceback, sys
from random import randint
import argparse
import numpy as np

# example input to CMD 
# python battleserver.py --size=5,5 --carrier=1,1,v --show

def get_args():
    '''This function parses and return arguments passed in'''
    # Assign description to the help doc
    parser = argparse.ArgumentParser(
		description='Loads battleship board')
    # Add arguments
    parser.add_argument('--show', action='store_true')
    parser.add_argument(
		'--size', type=str, help='Board size', required=True, nargs='+')
    parser.add_argument(
		'--carrier', type=str, help='Carrier position', required=False, nargs='+', default=None)
    parser.add_argument(
		'--battleship', type=str, help='Battleship position', required=False, nargs='+', default=None)

    '''implement other ships later'''
	
    # Array for all arguments passed to script
    args = parser.parse_args()
    # Assign args to variables
    show = args.show
    size = args.size[0].split(",")

    ships = {}
    try:
    	carrier = [int(e) if e.isdigit() else e for e in args.carrier[0].split(",")]
    	ships["c"] = carrier
    except TypeError:
    	print("No carrier (or invalid coordinates) given")
    	carrier = None

    try:
    	battleship = [int(e) if e.isdigit() else e for e in args.battleship[0].split(",")]
    	ships["b"] = battleship
    except TypeError:
    	print("No battleship (or invalid coordinates) given")
    	battleship = None
    # Return all variable values
    return show, size, ships


def place_ships(size, ships):
	board_matrix = np.zeros(size)
	"""takes ship and place at initial position x and y"""
	for k,v in ships.items():
		if v == ['r']:
			ships[k] = randint(0,size[0]-1), randint(0,size[1]-1)
	return board_matrix


def main():
	game_end = False
	
	# # Match return values from get_arguments()
	# # and assign to their respective variables
	show, size, ships = get_args()
	size = [int(e) for e in size]
	board_matrix = place_ships(size, ships)

	print("\nThis is battleship.")
	print('\n')
	
	if show is True:
		print(board_matrix)
	print("\nGame Over.")


if __name__ == '__main__':
	try:
		main()
	except:
		type, value, tb = sys.exc_info()
		traceback.print_exc()
		pdb.post_mortem(tb)