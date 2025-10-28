from logic.board import *
from logic.cards import create_cards, swap_cards


def start_game(num : int =4):
    main_board=create_board(num)
    cards=swap_cards(create_cards(num))
    hide_board=create_card_boards(cards,main_board)
    print(hide_board)