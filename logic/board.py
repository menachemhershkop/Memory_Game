
def create_board(size : int = 4):
    board=[]
    for i in range(1,size+1):
        row=[]
        for j in range(1,size+1):
            row.append("X")
        board.append(row)
    return board
def create_card_boards(cards : list[str], board):
    num_columns = len(board)
    game_board = [cards[i:i + num_columns] for i in range(0, len(cards), num_columns)]
    # if len(cards) == len(board):
    return game_board
    # else:
    #     return "incorrect board"
def list_printed(mat:list[list]):
    for i in mat:
        print(i)