from arg_parsed import parser
from displayBoard import displayBoard, createBoard

def main():
    args = parser.parse_args()

    width, height = get_size(args.size)

    boats = {
        'carrier': get_boat(args.carrier),
        'battleship': get_boat(args.battleship),
        'cruiser': get_boat(args.cruiser),
        'submarine': get_boat(args.submarine),
        'destroyer': get_boat(args.destroyer)
    }

    board = createBoard(width, height, boats)

    if args.show:
        displayBoard(board)

    if args.play:
        pass


def get_size(size_arg):
    try:
        sizes = [int(x.strip()) for x in size_arg.split(',')]
    except ValueError:
        raise Exception('Got invalid size value')
    assert all(size > 0 for size in sizes)
    assert len(sizes) == 2
    return sizes


def get_boat(boat_str):
    if not boat_str:
        return None

    boat = [x for x in boat_str.split(',')] # x, y, direction
    validate_boat(boat)
    boat[0] = int(boat[0])
    boat[1] = int(boat[1])
    return boat


def validate_boat(boat_tup):
    assert len(boat_tup) == 3
    assert isinstance(boat_tup[2], str)
    assert boat_tup[2] == 'v' or boat_tup[2] == 'h'
    try:
        int(boat_tup[0])
        int(boat_tup[1])
    except ValueError:
        raise Exception('Got invalid boat tuple')


if __name__ == '__main__':
    main()
