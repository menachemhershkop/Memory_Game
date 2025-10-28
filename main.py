from logic.cards import create_cards, swap_cards
from logic.board import create_card_boards, create_board


if __name__=="__main__":
    cards=swap_cards(create_cards(8))
    print(cards)
    print(create_card_boards(cards,create_board()))
