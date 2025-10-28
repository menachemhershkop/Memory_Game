from logic.board import *
from logic.cards import create_cards, swap_cards
from logic.logic import lets_gases, show_hide


def start_game(num : int =4):
    main_board=create_board(num)
    cards=swap_cards(create_cards(num))
    hide_board=create_card_boards(cards,main_board)
    print(main_board)
    column=int(input("Enter column number: "))
    row=int(input("Enter row number: "))
    first_gases=lets_gases(column,row,hide_board)
    column = int(input("Enter column number: "))
    row=int(input("Enter row number: "))
    second_gases=lets_gases(column,row,hide_board)
    show_hide(column,row,hide_board,main_board)
    print(hide_board)
    if first_gases == second_gases:
        print(first_gases,second_gases)



