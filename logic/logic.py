def reveal_card(row: int, col: int, board: list[list[str]], cards: list[list[str]]) -> None:
    if board[row][col] != "X":
        raise ValueError("Card already revealed.")
    board[row][col] = cards[row][col]
def hide_cards(location: list[tuple[int, int]], board: list[list[str]]) -> None:
    for row, col in location:
        board[row][col] = "X"
def check_match(location1: tuple[int, int], location2: tuple[int, int], cards: list[list[str]]) -> bool:
    r1, c1 = location1
    r2, c2 = location2
    return cards[r1][c1] == cards[r2][c2]
def result(board: list[list[str]]) -> bool:
    for row in board:
        if "X" in row:
            return False
    return True
