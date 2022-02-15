from abstract_card import AbstractCard

# TODO: Comenta a classe
class Card(AbstractCard):

    # Defining names of the values of the cards
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
    __COLORS = ("Blue", "Red")

    # Defining keys for the attributes
    __VALUE_ATTR = "Value"
    __SUIT_ATTR = "Suit"
    __COLOR_ATTR = "Color"

    # Constructor
    def __init__(self, attributes):

        # Checking if attribute is a dict
        if type(attributes) != dict:
            raise TypeError("'attribute' need to be a dict.")

        self.__attributes = attributes

        # Checking if attributes are "Value" and "Suit"
        for attribute in [self.__VALUE_ATTR, self.__SUIT_ATTR]:
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
        
        #Checking the color of the card
        color = attributes.get(self.__COLOR_ATTR)
        if not color in self.__COLORS:
            raise ValueError("color need to be one of this strings: Blue or Red")

    # Return the card in words
    def __str__(self):
        return "{} of {}".format(self.__NAMES.get(self.__attributes.get(self.__VALUE_ATTR)), self.__attributes.get(self.__SUIT_ATTR))

    # Return the value of the attribute
    def value_of(self, attribute):
        return self.__attributes.get(attribute)

    # Return the keys of this class
    def keys(self):
        return self.__attributes.keys()

    # TODO: Adiciona um método pra obter a cor da carta


if __name__ == "__main__":
    
    attributes_in_c1 = {"Value": 1,
                        "Suit": "Hearts",
                        "Color": "Blue"}
    c1 = Card(attributes_in_c1)
    print(c1)
    print(c1.value_of("Value"))
    print(c1.value_of("Suit"))
    print(c1.value_of("Color"))

    print(c1.keys())
    