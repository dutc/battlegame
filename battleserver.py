import random
import numpy as np
import sys
import ast

## First row and columns indexed at 0, first coordinate representive of row number, second coordinate representive of column number
## ! python battleserver.py --size=5,5 --carrier=0,0,h --battleship=r --cruiser=2,0,v --submarine=r --destroyer=3,1,h --show

## Generates dictionary of options from command line
tags = list(map(lambda x: tuple((x + ("=" if "=" not in x else "")).split("=")) , sys.argv[1:]))
tags = {k[2:]: tuple(v.split(',')) for k, v in dict(tags).items()}

## Constructs empty board with specified dimensions
row, column = tuple(map(int,tags['size']))
board = np.chararray((row, column))
board[:] = "-"

## Function to convert board into strings for friendly printing
def stringify(board):
    if sys.version_info[:2][0] == 2:
        return '\n'.join(list(map(lambda x: ''.join(x), [lis for lis in board])))
    else:
        return '\n'.join(list(map(lambda x: ''.join(list(map(lambda y: y.decode("utf-8"), x))), [lis for lis in board])))

## Retrieve all ships and ship information
ships = list(filter(lambda x: x in tags.keys(), ['carrier', 'battleship', 'cruiser', 'submarine', 'destroyer']))
ship_size = {'battleship': 4, 'carrier': 5, 'cruiser': 3, 'destroyer': 2, 'submarine': 3}
ship_symbol = {'battleship': 'b', 'carrier': 'c', 'cruiser': 'r', 'destroyer': 'd', 'submarine': 's'}

## Seperate ships into randomly placed ships and manually placed ships
cache = set()
bad_board = False

## Manual ship placement first
manual_ships = list(filter(lambda x: len(tags[x]) == 3, ships))
try:
    while len(manual_ships) != 0:
        ship = manual_ships.pop(0)
        pos = set()
        ## Retrieve orientiation and first coordinates of ship
        m, n, position = tuple(map(lambda x: int(x) if all([digit in '1234567890' for digit in x]) else x, tags[ship]))
        ## Store all positions in temp pos set
        for length in range(ship_size[ship]):
            if position == 'v':
                pos.add((m + length, n))
            else: 
                pos.add((m, n + length))
        ## Check if coordinates are not populated
        if set.intersection(cache, pos) == set():
            cache = cache | pos
        else:
            raise IndexError
        ## Place pieces on the boards
        for h, k in pos:
            board[h, k] = ship_symbol[ship]
except IndexError:
    bad_board = True

## Randomized ship placement next
auto_ships = list(filter(lambda x: len(tags[x]) == 1, ships))
try:
    while len(auto_ships) != 0:
        ship = auto_ships.pop(0)
        pos = set()
        ## Retrieve orientiation and first coordinates of ship
        position = random.choice(['h','v'])
        if position == "v":
            m, n = random.choice(range(0, row - ship_size[ship] + 1)), random.choice(range(0, column))
        else:
            m, n = random.choice(range(0, row)), random.choice(range(0, column - ship_size[ship] + 1))
        ## Store all positions in temp pos set
        for length in range(ship_size[ship]):
            if position == 'v':
                pos.add((m + length, n))
            else: 
                pos.add((m, n + length))
        ## Check if coordinates are not populated
        if set.intersection(cache, pos) == set():
            cache = cache | pos
        else:
            auto_ships.append(ship)
            continue
        ## Place pieces on the boards
        for h, k in pos:
            board[h, k] = ship_symbol[ship]
except IndexError:
    bad_board = True

if 'show' in tags.keys() and not bad_board:
    ## Print board with ship contents in desired locations
    print(stringify(board))
elif 'play' in tags.keys() and not bad_board:
    ## Keeps track of ship status and create new cache for already hit positions
    hits = {ship: ship_size[ship] for ship in ships}
    hitcache = set()
    while set(hits.values()) != {0}:
        coord = raw_input("Insert coordinate: ") if sys.version_info[:2][0] == 2 else input("Insert coordinate: ")
        try:
            entry = board[ast.literal_eval(coord)] if sys.version_info[:2][0] == 2 else board[ast.literal_eval(coord)].decode('utf-8')
            if coord not in hitcache:
                try:
                    ## Retrieves name of ship, decrement hits by 1 if valid, add coordinate to cache
                    name = {v:k for k, v in ship_symbol.items()}[entry]
                    hits[name] -= 1
                    hitcache.add(coord)
                    if entry != "-":
                        print("Good job! " + ("Hit " if hits[name] > 0 else "Sunk ") + name + ".")
                except KeyError:
                    print("Missed.")
            else:
                print("Already hit, try again.")
        except IndexError:
            print("Index out of range, try again.")
        except:
            print("Invalid entry, try again.")
    print("You win!")
else:
    if any([x in tags.keys() for x in ['play', 'show']]):
        print("Invalid board created.")
    else:
        print("Insert --show on to show board or --play to play game.")



