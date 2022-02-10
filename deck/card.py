# Definição da classe
class Card:

    # Membros estáticos (coletivos) da classe
    # Todos os objetos podem acessá-los
    __names = {1 : "Ace",
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
    
    __suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

    # Construtor
    def __init__(self, value, suit):
        self.__value = value
        self.__suit = suit

        # Verificando o argumento 'value'
        if type(self.__value) == int:
            if self.__value < 1 or self.__value > 13: 
                raise ValueError("'value' need to be an integer between 1 and 13")
        else:
                raise TypeError("'value' need to be an integer not {}".format(type(self.__value)))

        # Verificando o argumento 'suit'
        if suit not in self.__suits:
            raise ValueError("'suit' need to be one of this strings: Hearts, Diamonds, Clubs or Spades")

    def __str__(self):
        return "{} of {}".format(self.__names.get(self.__value), self.__suit)

    def value(self):
        return self.__value

    def suit(self):
        return self.__suit

    def name(self):
        return self.__str__().capitalize()