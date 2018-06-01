def displayBoard(w,h,dicBoats):
    board = []
    for y in range(h):
        row = []
        for x in range(w):
            row.append("-")
        board.append(row)

    for boat, info in dicBoats.items():
        if not info:
            continue

        boatOtherInfo = {
            "carrier":(5,"c"),
            "battleship":(4,"b"),
            "cruiser":(3,"r"),
            "submarine":(3,"s"),
            "destroyer":(2,"d")
        }
        x = info[0]
        y = info[1]
        d = info[2]

        if (d == "h"):
            for i in range(boatOtherInfo[boat][0]):
                board[y][x] = boatOtherInfo[boat][1]
                x+=1
        if (d == "v"):
            for i in range(boatOtherInfo[boat][0]):
                board[y][x] = boatOtherInfo[boat][1]
                y+=1

    flattenBoard = []
    for row in board:
        flattenBoard.append(" ".join(row))

    finalBoard = "\n".join(flattenBoard)
    print(finalBoard)
