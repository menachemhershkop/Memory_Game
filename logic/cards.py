import random
def create_cards(num_of_cards:int=5):
    ALPHABET_LIST = [chr(i) for i in range(65, 90)]
    cuple_cards=[]
    for i in range(num_of_cards):
        cuple_cards.append(ALPHABET_LIST[i])
        cuple_cards.append(ALPHABET_LIST[i])
    return cuple_cards
def swap_cards(card_list):
    for i in range(1000):
        card_1=random.randint(0,len(card_list)-1)
        card_2=random.randint(0,len(card_list)-1)
        card_list[card_1], card_list[card_2] = card_list[card_2], card_list[card_1]
    return card_list
