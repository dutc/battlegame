#!/usr/bin/env python
from collections import namedtuple
from enum import Enum, auto
from argparse import ArgumentParser
from ast import literal_eval
from random import randrange, choice

class ShipDef(namedtuple('ShipDef', 'size char')):
    def __str__(self):
        return self.char

SHIPS = {
    'carrier':    ShipDef(5, 'c'),
    'battleship': ShipDef(4, 'b'),
    'cruiser':    ShipDef(3, 'r'),
    'submarine':  ShipDef(3, 's'),
    'destroyer':  ShipDef(2, 'd'),
}

class Size(namedtuple('Size', 'x y')):
    @classmethod
    def from_cli(cls, s):
        x, y = s.split(',')
        return cls(int(x), int(y))

class Orientation(Enum):
    Horizontal = auto()
    Vertical = auto()
    Random = auto()

class Space(namedtuple('Space', 'x y')):
    def __add__(self, other):
        return Space(*(sum(coord) for coord in zip(self, other)))
    def __radd__(self, other):
        return Space(*(sum(coord) for coord in zip(self, other)))
    def __mul__(self, scale):
        return Space(*(coord*scale for coord in self))

class Pos(namedtuple('Pos', 'x y o')):
    @classmethod
    def from_cli(cls, s):
        if s.strip() == 'r':
            return cls(None, None, Orientation.Random)
        x, y, d = s.split(',')
        return cls(int(x), int(y), {'h': Orientation.Horizontal, 'v': Orientation.Vertical}[d])

class Board:
    def __init__(self, size, ships=None):
        self.size = size
        if ships is None:
            ships = {}
        self.ships = {
            name: [
                Space(pos.x, pos.y) + (Space(0, 1) if pos.o is Orientation.Horizontal else Space(1, 0)) * i
                for i in range(SHIPS[name].size)
            ]
            for name, pos in ships.items()
            if pos.o is not Orientation.Random
        }
        pos = [xy for pos in self.ships.values()
                  for xy in pos]
        if len(pos) != len(set(pos)):
            raise Exception('overlapping ships!')
        for name, start in {name:start for name, start
                                       in ships.items()
                                       if start.o is Orientation.Random}.items():
            for _ in range(100):
                start  = Space(randrange(1, self.size.x+1), randrange(1, self.size.y+1))
                orient = choice([Orientation.Horizontal, Orientation.Vertical])
                candidate = [start + (Space(0, 1) if orient is Orientation.Horizontal else Space(1, 0)) * i
                             for i in range(SHIPS[name].size)]
                if all(c not in self.board and 1 <= c.x <= self.size.x and 1 <= c.y <= self.size.y for c in candidate):
                    break
            if not all(c not in self.board and 1 <= c.x <= self.size.x and 1 <= c.y <= self.size.y for c in candidate):
                raise Exception(f'could not place {name} in 100 tries')
            self.ships[name] = candidate
            self.board

    @property
    def board(self):
        return {
            (coord.x, coord.y): name
            for name, pos in self.ships.items()
            for coord in pos
        }

    def __call__(self, x, y):
        if (x, y) in self.board:
            name = self.board[x, y]
            ship = self.ships[name]
            if Space(x, y) in ship:
                ship.remove(Space(x, y))
                if all(not ship for ship in self.ships.values()):
                    return 'you win!'
                if not ship:
                    return f'sunk {name}'
                return f'hit {name}'
        return 'miss'

    def pformat(self):
        return '\n'.join(
            ''.join('-' if (x, y) not in self.board else SHIPS[self.board[x, y]].char
                for x in range(1, self.size.x + 1)
            )
            for y in range(1, self.size.y + 1)
        )


parser = ArgumentParser()
parser.add_argument('--size', default=Size(5,5), type=Size.from_cli)
for ship in SHIPS:
    parser.add_argument(f'--{ship}', type=Pos.from_cli)
parser.add_argument('--show', action='store_true', default=False)
parser.add_argument('--play', action='store_true', default=False)

if __name__ == '__main__':
    args = parser.parse_args()
    board = Board(args.size, ships={ship: getattr(args, ship) for ship in SHIPS if getattr(args, ship) is not None})
    if args.show:
        print(board.pformat())
    if args.play:
        while True:
            line = input('> ')
            if line.strip() == 'show':
                print(board.pformat())
                continue
            x, y = line.split()
            x, y = int(x), int(y)
            result = board(x, y)
            print(result)
            if result == 'you win!':
                break
