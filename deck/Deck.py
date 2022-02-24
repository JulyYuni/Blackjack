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
        return self.__cards.append(card)

    # To discard all Cards in the Deck
    def discard (self):
        discard_deck = Deck()
        while len(self.__cards) > 0:
            discard_deck.receive(self.__cards.pop())
        return discard_deck
    
    # To shuffle Deck
    def shuffle(self):
        for i in range(0, 4):
            shuffle(self.__cards)

    # Somating decks
    def somating_decks(self, my_deck): 
        while len(self.__cards) > 0:
            my_deck.receive(self.__cards.pop())
        return my_deck

    # To sort Deck  
    def sort(self):
        self.__cards.sort()

    # Return the lenght of the Deck
    def lenght(self, lenght = None):
        if lenght == None:
            lenght = len(self.__cards)
        self.__cards = self.__cards[0:lenght]
        return len(self.__cards)

    # Return all cards in a list
    def deck_list(self):
        return self.__cards

    # Return the Deck in words
    def __str__(self):
        return "   |".join([str(card) for card in self.__cards])

    # Required to serialize Deck inside list in dict objects
    __repr__ = __str__