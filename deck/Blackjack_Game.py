from card import Card
from deck import Deck
from player import Player
from plays import Plays


if __name__ == "__main__":
    my_deck = Deck(8)
    will = Player("Willian", 500, 250)
    dealer = Player("Dealer", 500, 0)

    plays = Plays()

    for i in range (0, 2):
        will.hit1(my_deck)
        dealer.hit1(my_deck)

    print(will)
    print(dealer)

    will_value = plays.card_calculator(will)
    dealer_value = plays.card_calculator(dealer)

    print (will_value)
    print (dealer_value)

    turn_conclusion = plays.turn_calculator(will, will_value, dealer_value, will.name, dealer.name)


    print (turn_conclusion)





