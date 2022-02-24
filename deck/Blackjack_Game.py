from card import Card
from deck import Deck
from player import Player
from functions import Functions
from turn import Turn

# Executing the game
if __name__ == "__main__":
    # Initial massages and getting player's nickname
    print("\nHello! This is Blackjack!\n\n")
    print("Insert your nickname!\n\n")
    player_name = input("Nickname: ")
    player_name = player_name.capitalize()

    # Defining decks and players
    discard_deck = Deck()
    my_deck = Deck(4)
    player = Player(player_name, 500, 0)
    dealer = Player("Dealer", 500, 0)

    # Running a turn
    player_money, discard_deck = Turn(player, dealer, my_deck, discard_deck)

    # Player chooses if wnat a new turn
    new_turn = Functions.answer("Do you want a new turn?", "Answer with [Y] for yes and [N] for no.", ["Y", "N"])

    # Running a new turn while player want it
    while new_turn == "Y":
        player = Player(player_name, player_money, 0)

        player_money, discard_deck = Turn(player, dealer, my_deck, discard_deck)

        my_deck_list = my_deck.deck_list()
        my_deck_lenght = my_deck.lenght()
        discard_deck_lenght = discard_deck.lenght()

        print("\n\nmy_deck.__cards: {} ".format(my_deck_list[0:25:1]))
        print("\n\n\n my_deck_lenght: {}".format(my_deck_lenght))
        my_deck_lenght = my_deck.lenght(208)
        print("\n\n\n my_deck_lenght: {}".format(my_deck_lenght))
        print("\n\ndiscard_deck: {}".format(discard_deck_lenght))

        if my_deck_lenght == 208:
            print("The lenght of my_deck is 208")
            print("\n\ndiscard_deck: {}".format(discard_deck_lenght))
            print("\n\nmy_deck.__cards: {} ".format(my_deck_list[0:25:1]))
            print("\n\n\n my_deck_lenght: {}".format(my_deck_lenght))

            my_deck = discard_deck.somating_decks(my_deck)
            print("\n\ndiscard_deck: {}".format(discard_deck_lenght))
            print("\n\nmy_deck.__cards: {} ".format(my_deck_list[0:25:1]))
            print("\n\n\n my_deck_lenght: {}".format(my_deck_lenght))

            my_deck = my_deck.shuffle()
            print("\n\ndiscard_deck: {}".format(discard_deck_lenght))
            print("\n\nmy_deck.__cards: {} ".format(my_deck_list[0:25:1]))
            print("\n\n\n my_deck_lenght: {}".format(my_deck_lenght))
        new_turn = Functions.answer("Do you want a new turn?", "Answer with [Y] for yes and [N] for no.", ["Y", "N"])
    


