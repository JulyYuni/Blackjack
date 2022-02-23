from card import Card
from deck import Deck
from player import Player
from functions import Functions

    # Showing turn's info and calculating dealer hand and player hand
def print_turn(player, dealer, my_deck):
    print(player)
    print(dealer)
    player_value = player.card_calculator(player)
    dealer_value = dealer.card_calculator(dealer)
    print ("\n{} hand total: {}".format(player.name(), player_value))
    print ("Dealer hand total: {}".format(dealer_value))
    return player_value, dealer_value

    # Defining what is a turn
def Turn(player, dealer, my_deck, discard_deck):
    functions = Functions(player)
    player_hand = player.hand()
    player_name = player.name()
    player_bet = functions.make_bet()
    player_money = player.money()
    dealer_hand = dealer.hand()
    player = Player(player_name, player_money, player_bet)

    # Giving the primary two cards for each player
    for i in range (0, 2):
        player.player_hit(my_deck)
        dealer.player_hit(my_deck)

    # Showing turn's info
    player_value, dealer_value = print_turn(player, dealer, my_deck)

    # Player chooses how much cards it want to hit
    functions.hit_plays(player, my_deck)

    # Dealer calculate how much cards it need to hit
    dealer_value = dealer.dealer_calculator(dealer, my_deck)

    # Showing turn's info
    player_value, dealer_value = print_turn(player, dealer, my_deck)

    # Calculating if player won or lose
    player_money, turn_conclusion = functions.turn_calculator(player, player_value, dealer_value)

    # Discarding player's deck
    discard_deck, player_hand = player.player_discard(discard_deck)
    discard_deck, player_hand = dealer.player_discard(discard_deck)

    # Discarding print test
    print("\nDiscard pile: {}".format(discard_deck))

    return player_money, discard_deck
