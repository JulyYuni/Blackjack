import random

# Abstract class to card
class AbstractCard:

    # Constructor
    def __init__(self):
        pass
    
    # Return the card in words
    def __str__(self):
        pass

    # Return the value from a given attribute
    def value_of(self, attribute):
        pass

    # Return the card's keys (attributes) 
    def keys(self):
        pass
    
# Class to represent a card from a common Deck
class Card(AbstractCard):

    # Defining names of the values of the Cards
    __NAMES = {1 : "Ace",
               2 : "Two",
               3 : "Three",
               4 : "Four",
               5 : "Five",
               6 : "Six",
               7 : "Seven",
               8 : "Eight",
               9 : "Nine",
               10 : "Ten",
               11 : "Queen",
               12 : "Jack",
               13 : "King"}
    
    # Defining suits
    __SUITS = ("Hearts", "Diamonds", "Clubs", "Spades")

    # Defining the colors of the other side
    __COLORS = ("Blue", "Red")

    # Defining keys for the attributes
    __VALUE_ATTR = "Value"
    __SUIT_ATTR = "Suit"
    __COLOR_ATTR = "Color Side"

    # Constructor
    def __init__(self, attributes):

        # Checking if attribute is a dict
        if type(attributes) != dict:
            raise TypeError("'attribute' need to be a dict.")

        self.__attributes = attributes

        # Checking if attributes are "Value", "Suit" and "Color Side"
        for attribute in self.keys():
            if self.__attributes.get(attribute) is None:
                raise ValueError("The card doesn't have attribute {}".format(attribute))

        # Removing other keys that should be passed in dict
        attributes_to_be_removed = []
        for attribute in self.__attributes:
            if not attribute in self.keys():
                attributes_to_be_removed.append(attribute)
        for attribute in attributes_to_be_removed:
            self.__attributes.pop(attribute, None)

        # Checking the argument 'value'
        value = self.__attributes.get(self.__VALUE_ATTR)
        if type(value) == int:
            if value < 1 or value > 13:
                raise ValueError("'value' need to be an integer between 1 and 13")
        else:
            raise TypeError("'value' need to be an integer not {}".format(type(value)))

        # Checking the argument 'suit'
        suit = self.__attributes.get(self.__SUIT_ATTR)
        if not suit in self.__SUITS:
            raise ValueError("'suit' need to be one of this strings: Hearts, Diamonds, Clubs or Spades")
        
        # Checking the color of the Card
        color = attributes.get(self.__COLOR_ATTR)
        if not color in self.__COLORS:
            raise ValueError("color need to be one of this strings: Blue or Red")

    # Return the Card in words
    def __str__(self):
        return "{} of {} of {}".format(self.__NAMES.get(self.__attributes.get(self.__VALUE_ATTR)), self.__attributes.get(self.__SUIT_ATTR), self.__attributes.get(self.__COLOR_ATTR))

    # Required to serialize Card inside list in dict objects
    __repr__ = __str__

    # Return the value from a given attribute
    def value_of(self, attribute):
        return self.__attributes.get(attribute)

    # Return the Card's keys (attributes)
    def keys(self):
        return [self.__VALUE_ATTR, self.__SUIT_ATTR, self.__COLOR_ATTR]

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
        discard_list = Deck()
        while len(self.__cards) > 0:
            discard_list.receive(self.__cards.pop())
        return discard_list

    # To shuffle Deck
    def shuffle(self):
        for i in range(0, 4):
            random.shuffle(self.__cards)

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


# Class to represent class of players
class Player:
    
    # Constructor

    def __init__(self, name, money):
        self.__name = name
        self.__hand = Deck()
        self.__bet = 0
        self.__money = money
        self.__discard_list = Deck()

    def hit1(self, my_deck):
        return self.__hand.receive(my_deck.hit())

    def discard1(self):
        cards_discarded = self.__hand.discard()
        return self.__discard_list.receive(cards_discarded)

    def __str__(self):
        return "{}: {}".format(self.__name, self.__hand)


if __name__ == "__main__":
    my_deck = Deck(8)
    print("1")
    will = Player("Willian", 500)
    print("2")
    dealer = Player("Dealer", 500)
    print("3")

    for i in range (0, 2):
        print("4")
        will.hit1(my_deck)
        print("5")
        dealer.hit1(my_deck)
        print("6")
        will.discard1()
        print("7")

    print(will)
    print(dealer)

print("a")

