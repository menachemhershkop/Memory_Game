from logic.board import *
from logic.cards import *
from logic.logic import *

def start_game(num : int =4):
    main_board=create_board(num)
    cards=swap_cards(create_cards(num*num // 2))
    hide_board=create_card_boards(cards,main_board)
    print(f"Board size: {size}x{size}\n")

    while True:
        list_printed(main_board)
        print("\nChoice 2 cards by rwo and col")

        r1 = int(input("Row 1: ")) - 1
        c1 = int(input("Column 1: ")) - 1
        reveal_card(r1, c1, main_board,hide_board)
        list_printed(main_board)

        r2 = int(input("Row 2: ")) - 1
        c2 = int(input("Column 2: ")) - 1
        reveal_card(r2, c2, main_board,hide_board)
        list_printed(main_board)

        if check_match((r1, c1), (r2, c2), hide_board):
            print("got gestes \n")
        else:
            print("bad gestes. the card will be hiding \n")
            hide_cards([(r1, c1), (r2, c2)], main_board)


        if result(main_board):
            print("you win!!!")
            break




if __name__=="__main__":
   start_game(int(input("Enter number of cards: ")))