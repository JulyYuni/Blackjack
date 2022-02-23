from card import Card
from deck import Deck
from player import Player
from plays import Plays

def turn(player, dealer, my_deck):
    player_bet = make_bet()
    for i in range (0, 2):
        player.player_hit(my_deck)
        dealer.player_hit(my_deck)
    
    print(player)
    print(dealer)

    player_value = player.card_calculator(player)
    dealer_value = dealer.card_calculator(dealer)

    print ("\n{} hand total: {}".format(player.name(), player_value))
    print ("Dealer hand total: {}".format(dealer_value))

    plays.hit_plays(will, my_deck)
    dealer_value = dealer.dealer_calculator(dealer, my_deck)

    pass