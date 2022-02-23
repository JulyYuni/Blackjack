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

    # Defining decks and players
    discard_deck = Deck()
    my_deck = Deck(8)
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
        new_turn = Functions.answer("Do you want a new turn?", "Answer with [Y] for yes and [N] for no.", ["Y", "N"])
    


