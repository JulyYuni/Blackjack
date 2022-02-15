from card import Card

from random import randint, shuffle

# Class to represent a deck of Cards
class Deck:

    # Constructor
    def __init__(self, number_of_decks = 0):

        # Defining suits
        suits =  ("Hearts", "Diamonds", "Clubs", "Spades")

        # Defining the colors of the other side
        colors = ("Blue", "Red")

        # Defining a list for the Cards of the Deck
        self.__cards = []

        # Defining the number os Decks
        self.__number_of_decks = number_of_decks

        # Generating Cards and adding on the Deck (self.__cards)
        for i in range (0, self.__number_of_decks):
            for color in colors:
                for suit in suits:
                    for value in range(1, 14):
                        self.__cards.append(Card({"Value": value,
                                                "Suit": suit,
                                                "Color Side": color}))
        
        # Shuffling the Deck                                        
        self.shuffle()

    # To hit a Card from Deck
    def hit (self):
        taken_card = None
        if len(self.__cards) > 0:
            taken_card = self.__cards[-1]
            self.__cards.pop(-1)
        return taken_card

    # To add a Card in Deck
    def receive(self, card):
        self.__cards.append(card)

    # To discard all Cards in the Deck
    def discard (self):
        discard_list = []
        discard_list.extend(self.__cards)
        self.__cards.clear()
        return discard_list

    # To shuffle Deck
    def shuffle(self):
        for i in range(0, 4):
            shuffle(self.__cards)

    # To sort Deck  
    def sort(self):
        self.__cards.sort()

    # Return the lenght of the Deck
    def lenght(self):
        return len(self.__cards)

    # Return the Deck in words
    def __str__(self):
        return "   |".join([str(card) for card in self.__cards])

    # Required to serialize Deck inside list in dict objects
    __repr__ = __str__


if __name__ == "__main__":
    player_hand = Deck(0)
    dealer_hand = Deck(0)
    my_deck = Deck(8)
    deck_with_52_cards = Deck(1)
    
    for i in range (0, 2):
        taken_card = my_deck.hit()
        player_hand.receive(taken_card)

        dealer_hand.receive(my_deck.hit())

    print("Player hand: {}".format(player_hand))
    print("Dealer hand: {}".format(dealer_hand))

    cards_discarded = player_hand.discard()
    cards_discarded.extend(dealer_hand.discard())

    print("Discard pile: {}".format(cards_discarded))
    print(player_hand) # Should print an empty string