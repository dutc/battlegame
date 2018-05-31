INTRODUCTION
============

Your mission, if you choose to accept it, is to write a Battleship game. 

In detail, we want YOU:
- to write a Battleship board program called `battleserver.py`:
    - it must create a board for a game of Battleship
    - with the `--show` flag, it should print out the board
    - with the `--play` flag, it should allow the user to play a "one player" game interactively
- to write a Battleship playing robot called `battleplayer.py`:
    - it needs to use `battleserver.py` to play a game of Battleship automatically
    - ideally, it should implement some algorithm or heuristic to play a game of Battleship optimally
- to write tests to validate the correct operation of the above two programs. Good code should come with some guarantee that it does what it claims (no Djikstra quotes accepted at this time)

We'll be working in teams, to share knowledge!

_Submit your solutions via pull request on Github!_

_Include a file called `AUTHORS` with information about your team!_

AGENDA
======

The goal is to get as much done in the time alotted. 
Three sprints are scheduled, with designated break times to ask the 
proctors for help, or just stretch/grab tea/give your eyes a rest.

| time      | activity
|-----------|-----------------------------
|6:00 - 6:15| Setup
|6:15 - 6:30| Break into groups
|6:30 - 7:00| Sprint #1
|7:00 - 7:15| Q&A Session #1
|7:15 - 7:45| Sprint #2
|7:45 - 8:00| Q&A Session #2
|8:00 - 8:30| Final sprint
|8:30       | Deadline for pull requests!

RECOMMENDED COURSE of ACTION
============================

If you are unsure where to start, we recommend you follow these steps:

1. write `battleserver.py` which can create a board with units at specified positions.
2. extend `battleserver.py` to display the board.
3. extend `battleserver.py` to support random positioning of units.
4. extend `battleserver.py` to support interactive play.
5. write `battleplayer.py` to use a simple, brute-force strategy
6. improve `battleserver.py` to use better strategies

SCORING
=======

To help you judge how well you've done, we have a scoring rubric. 
The point distributions designate how complex and important each feature is.

`battleserver.py` and `battleplayer.py` are scored as follows (50 points):

`battleserver.py`: (total 20 points)
- unit placement functionality (10 pts total)
    - manual placement (2 pts)
    - random placement (3 pts)
    - allows user to specify size (1 pt)
    - error handling (what if the board is too small? etc.) (3 pts)
    - displays board (1 pt)
- supports interactive play (10 pts total)

`battleplayer.py`: (total 20 points)
- supports automatic play (20 pts total)
    - simple, brute-force strategy (8 pts)
    - more advanced strategy (8 pts)
    - best strategy among participants (4 pts)

Misc: (total 10 points with 10 bonus points)
- quality and exhaustiveness of tests (10 pts)
- "elegance" (up to +10 bonus points)

CREATING a BOARD with `battleserver.py`
=======================================

Here are the rules:

Battleship has a board with ships on it. The board can be of any
size. The board can have up to five different ships, one of each type.

The ships are:

| ship       | size |
|------------|------|
| carrier    |  5   |
| battleship |  4   |
| cruiser    |  3   |
| submarine  |  3   |
| destroyer  |  2   |

Ships must be placed in a straight line, either horizontally or vertically.

Ships must FIT onto the board.

Specify the size of the board in `battleserver.py` and `battleplayer.py` on the
command line with the `--size` flag.

e.g.,
`$ python battleserver.py --size=5,5 # create a board of size 5x5`

A Battleship game may include **at most** one of each unit. 
In other words, you don't need to have every unit on the board.

Place the units on the board by passing the following flags to `battleserver.py`:
`--carrier` `--battleship` `--cruiser` `--submarine` `--destroyer`

The argument these flags should take should be of the form (using the carrier as an example):
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

VIEWING THE BOARD CREATED WITH `battleserver.py`
===============================================

Use the `--show` flag with `battleserver.py` to view the board.

**This is a useful debug tool and you should implement it early, and 
use it frequently!**

The output should be a textual representation of the board.

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

PLAYING INTERACTIVELY AGAINST `battleserver.py`
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

PLAYING AUTOMATICALLY AGAINST `battleserver.py`
===============================================

How `battleserver.py` and `battleplayer.py` will interact, and what the 
output looks like, are up to you! Let your creativity run wild!

The one hard requirement is: You must track how many moves it takes for your 
bot to win! Try to write the smartest bot possible!

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

MORE EXAMPLES
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
