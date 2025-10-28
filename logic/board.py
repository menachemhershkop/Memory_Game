
def creat_board(size : int = 4):
    board=[]
    for i in range(1,size+1):
        row=[]
        for j in range(1,size+1):
            row.append("X")
        board.append(row)
    return board
def creat_card_boards(cards : list[str], board):
    game_board=[]
    for i in range(1,len(cards)+1):
        row=[]
        for j in range(1,len(cards)+1):
            row.append(j)
        game_board.append(row)
    if len(game_board)== len(board):
        return game_board
    else:
        return "incorrect board"
