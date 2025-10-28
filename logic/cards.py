import random

# from board import create_card_boards, create_board


def create_cards(num_of_cards:int=4):
    ALPHABET_LIST = [chr(i) for i in range(65, 91)]
    cuple_cards=[ALPHABET_LIST[i] for i in range(num_of_cards)] * 2
    return cuple_cards
def swap_cards(card_list:list[str]) -> list[str]:
    random.shuffle(card_list)
    return card_list
