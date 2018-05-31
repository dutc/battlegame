INTRODUCTION
============

Your goal:
- to write a program called `battleserver.py`:
    - creates a board for a game of Battleship
    - with the `--show` flag, just prints out the board
    - with the `--play` flag, allows the user to play a game interactively
- to write a program called `battleplayer.py`:
    - interacts with `battleserver.py` to play a game of Battleship automatically
    - implements some algorithm or heuristic to play a game of Battleship optimally
- to write tests to validate the correct operation of the above two programs

_Submit your solutions via pull-request on Github!_

_Include a file called *AUTHORS* with information about your team!_

GUIDANCE
========

Follow these steps:
1. write `battleserver.py` which can create a board with units at specified positions.
2. extend `battleserver.py` to display the board.
3. extend `battleserver.py` to support random positioning of units.
4. extend `battleserver.py` to support interactive play.
5. write `battleplayer.py` to use a simple, brute-force strategy
6. improve `battleserver.py` to use better strategies

SCORING
=======

`battleserver.py` and `battleplayer.py` are scored as follows (50 points):

- unit placement functionality (10 pts total)
    - manual placement (2 pts)
    - random placement (3 pts)
    - allows user to specify size (1 pt)
    - error handling (what if the board is too small? etc.) (3 pts)
    - displays board (1 pt)
- supports interactive play (10 pts total)
- supports automatic play (20 pts total)
    - simple, brute-force strategy (8 pts)
    - more advanced strategy (8 pts)
    - best strategy among participants (4 pts)
- quality and exhaustiveness of tests (10 pts)
- "elegance" (up to +10 bonus points)

CREATING a BOARD with `battleserver.py`
=======================================

A Battleship board can be of any size. Specify the size of the board in
`battleserver.py` and `battleplayer.py` on the command line with the `--size` flag.

e.g.,
`$ python battleserver.py --size=5,5 # create a board of size 5x5`

A Battleship game may include at most one of each unit. You may omit units.
Place the units on the board by passing the following flags to `battleserver.py`:
`--carrier` `--battleship` `--cruiser` `--submarine` `--destroyer`

The argument these flag should take should be of the form (using the carrier as an example):
- `--carrier=x,y,h` to place the carrier horizontally starting at (x, y)
- `--carrier=x,y,v` to place the carrier vertically starting at (x, y)
- `--carrier=r` to place the carrier randomly anywhere on the board

e.g.,
```
$ python battleserver.py --size=5,5 --carrier=1,1,h # create a board of size 5x5
                                                    # placing the carrier horizontally
                                                    # starting at (1, 1)
```

```
# create a board of size 5x5, placing the carrier vertically starting at (1, 1)
#                         and placing the submarine horizontally starting at (8, 10)
$ python battleserver.py --size=10,10 --carrier=1,1,v --submarine=8,10,h
```
                              
For reference:
- a carrier is *5* squares in size
- a battleship is *4* squares in size
- a cruiser is *3* squares in size
- a submarine is *3* squares in size
- a destroyer is *2* squares in size

Ships must be placed in a straight line, either horizontally or vertically.

Ships must FIT onto the board.

VIEWING the BOARD CREATED with `battleserver.py`
===============================================

Use the `--show` flag with `battleserver.py` to view the board.

The output should be an ASCII representation of the board.

Use the following characters to denote spaces occupied by units:
- *c* for the Carrier
- *b* for the Battleship
- *r* for the cRuiser
- *s* for the Submarine
- *d* for the Destroyer

e.g.,
```
$ python battleserver.py --size=5,5 --carrier=1,1,v --show
c----
c----
c----
c----
c----
```

PLAYING INTERACTIVELY against `battleserver.py`
===============================================

Use the `--play` flag with `battleserver.py` to play interactively.

Read actions from the console. Actions should be of the form `x, y` to indicate
firing a missile at the square at (x, y).

`battleserver.py` should respond with one of the following messages:
- `miss` if the missile missed
- `hit UNIT` if the missile hit a unit
- `sunk UNIT` if the missile hit and sunk a unit
- `you win!` if all units are sunk

NOTE: what should you do if the user fires a missile against a square twice?

e.g.,
```
$ python battleserver.py --size=5,5 --carrier=1,1,v --play
> 1 1
hit carrier
> 2 1
miss
> 2 2
miss
> 1 2
hit carrier
> 2 2
miss
> 1 3
hit carrier
> 1 4
hit carrier
> 1 5
sunk carrier
you win!
```

PLAYING AUTOMATICALLY against `battleserver.py`
===============================================

NOTE: you have to decide how `battleserver.py` and `battleplayer.py` will interact!

NOTE: you have to decide what the output looks like!

NOTE: you must track how many moves it takes for your bot to win! Try to write the smartest bot possible!

e.g.,
```
$ python battleplayer.py --server-command='battleserver.py --size=5,5 --carrier=1,1v'
bot: 1 1
board: hit carrier
bot: 2 1
board: miss
bot: 1 2
board: hit carrier
bot: 1 3
board: hit carrier
bot: 1 4
board: hit carrier
bot: 1 5
board: sunk carrier
board: you win in 6 moves!
```

More Examples
=============

(Hint: use these as your starting tests.)

Create a board of size (5, 5) with the carrier, battleship, cruiser, submarine, and destroyer placed horizontally on each row.

```
$ python battleserver.py --size=5,5 --carrier=1,1,h --battleship=1,2,h --cruiser=1,3,h --submarine=1,5,h --destroyer=1,4,h --show
```

Expected output (c = Carrier, b = Battleship, r = cRuiser, s = Submarine, d = Destroyer):
```
ccccc
bbbb-
rrr--
sss--
dd---
```

Create a board of size (5, 5) with the carrier, battleship, cruiser, submarine, and destroyer placed vertically on each column.
```
$ python battleserver.py --size=5,5 --carrier=1,1,v --battleship=2,1,v --cruiser=3,1,v --submarine=5,1,v --destroyer=4,1,v --show
```

Expected output:
```
cbrsd
cbrsd
cbrs-
cb---
c----
```

Create a board of size (5, 5) with the carrier, cruiser, submarine, and destroyer placed vertically on each column and the battleship placed randomly.

```
$ python battleserver.py --size=5,5 --carrier=1,1,v --battleship=r --cruiser=3,1,v --submarine=5,1,v --destroyer=4,1,v --show
```

Expected output (battleship is placed randomly):
```
c?rsd
c?rsd
c?rs?
c????
c????
```

Create a board of size (10, 10) with the carrier, battleship, cruiser, submarine, and destroyer placed randomly.

```
$ python battleserver.py --size=10,10 --carrier=r --battleship=r --cruiser=r --submarine=r --destroyer=r --show
```

Expected output (every unit is placed randomly):
```
??????????
??????????
??????????
??????????
??????????
??????????
??????????
??????????
??????????
??????????
```
