from logic.cards import create_cards, swap_cards
from logic.board import creat_card_boards

if __name__=="__main__":
    cards=swap_cards(create_cards())
    print(cards)
    print(creat_card_boards(cards,create_cards()))