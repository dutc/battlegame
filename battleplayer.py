#!/usr/bin/env python3
from itertools import product
from argparse import ArgumentParser
from os import fork, execv, read, write, pipe, dup2

parser = ArgumentParser()
parser.add_argument('--command')

if __name__ == '__main__':
    args = parser.parse_args()

    r1, w1 = pipe()
    r2, w2 = pipe()
    pid = fork()

    if not pid:
        for x, y in product(range(1, 6), range(1, 6)):
            line = read(r2, 1024)
            if not line:
                break
            line = line.decode()
            print(line, end='')
            action = f'{x} {y}\n'
            print(action, end='')
            write(w1, action.encode())
    else:
        dup2(r1, 0)
        dup2(w2, 1)
        execv('/bin/sh', ['/bin/sh', '-c', args.command])

