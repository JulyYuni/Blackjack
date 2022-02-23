from card import Card
from deck import Deck

# Class to represent class of players
class Player:
    
    # Constructor
    def __init__(self, name, money, bet):
        self.__name = name
        self.__hand = Deck()
        self.__bet = bet
        self.__money = money
        self.__discard_deck = Deck()

    # Hitting a card from my_deck to self.__hand deck
    def player_hit(self, my_deck):
        return self.__hand.receive(my_deck.hit())

    # Discarding the player hand on the discard list
    def player_discard(self, discard_pile):
        discard_deck = self.__hand.discard()
        discard_pile.receive(discard_deck)
        return discard_pile, self.__hand

    # To calculate the total player hand value
    def card_calculator(self, player):
        hand_value = 0

        for card in player.hand().deck_list():
            hand_value += card.true_cards_value()

        return hand_value

    # Dealer calculate how much cards it need to hit
    def dealer_calculator(self, dealer, my_deck):
        dealer_value = dealer.card_calculator(dealer)
        while dealer_value < 17:
            dealer.player_hit(my_deck)
            print(dealer)
            dealer_value = dealer.card_calculator(dealer)
        return dealer_value

    # Do the things when the player loses
    def lose(self):
        self.__money = self.__money - self.__bet
        self.__conclusion = print("\nYou Lose!\n\n")
        print("<" + ("-" * 150) + ">")
        return self.__money, self.__conclusion

     # Do the things when the player wins
    def win(self):
        self.__money = self.__money + self.__bet
        self.__conclusion = print("\nYou Win!\n\n")
        print("<" + ("-" * 150) + ">")
        return self.__money, self.__conclusion

    # Player can double it own bet
    def double(self, player):
        return self.__bet *2 

    # Returning all the variables
    def money(self):
        return self.__money

    def bet(self):
        return self.__bet

    def name(self):
        return self.__name

    def hand(self):
        return self.__hand

    def discard_deck(self):
        return self.__discard_deck
 
    # Return the player_hand in words
    def __str__(self):
        return "\n\n{}: {}".format(self.__name, self.__hand)

    # Required to serialize Deck inside list in dict objects
    __repr__ = __str__