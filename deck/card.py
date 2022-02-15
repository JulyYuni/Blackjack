from abstract_card import AbstractCard

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
        for attribute in [self.__VALUE_ATTR, self.__SUIT_ATTR, self.__COLOR_ATTR]:
            if self.__attributes.get(attribute) is None:
                raise ValueError("The card doesn't have attribute {}".format(attribute))

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
        return self.__attributes.keys()

    # Return the Card color
    def color(self):
        return self.__attributes.get(self.__COLOR_ATTR)