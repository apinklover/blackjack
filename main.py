import random

suits = ["♠", "♣", "♥", "♦"]
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
deck = []
dealer_hand = []
player_hand = []
split_hand = []
first_hit = False
split = False
dealer_sum = 0
player_sum = 0
split_sum = 0


def generate_deck(num):
    for i in range(num):
        for suit in suits:
            for number in numbers:
                deck.append(str(suit) + str(number))
    random.shuffle(deck)


generate_deck(1)

for i in range(2):
    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())

print(deck, dealer_hand, player_hand)


def hit():
    global split
    global first_hit
    if not split:
        player_hand.append(deck.pop())
        first_hit = True
    else:
        player_hand.append(deck.pop())
        split_hand.append(deck.pop())


def stand():
    global dealer_sum
    for dcard in dealer_hand:
        if dcard.substring(1) in ["J", "Q", "K"]:
            dealer_sum += 10
        elif dcard.substring(1) in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
            dealer_sum += dcard.substring(1)
        else:
            pass
            # TODO: Sort Hands by numeric value of cards and calculate

    if not split:
        pass


def double_down():
    global first_hit
    if not first_hit:
        hit()
        stand()
    else:
        print("You can no longer double down; you have already hit.")


def split(): 
    global first_hit
    if not first_hit:
        split_hand.append(player_hand.pop())
    else:
        print("You can no longer split; you have already hit.")
        

def insurance():  # WIP!
    pass


def surrender():  # WIP!
    pass
