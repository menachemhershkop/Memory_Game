def lets_gases(location1, location2, board: list):
    return board[location1][location2]

def show_hide(location1, location2, board:list, cards:list):
        if lets_gases(location1, location2, board):
            cards[location1][location2], board[location1][location2]=board[location1][location2],cards[location1][location2]
            print(board)

def result(cls):
    pass
