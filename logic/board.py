def creat_board(size : int = 4):
    board=[]
    for i in range(1,size+1):
        row=[]
        for j in range(1,size+1):
            row.append("X")
        board.append(row)
    return board
