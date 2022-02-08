# Definição da classe
class Card:

    # Membros estáticos (coletivos) da classe
    # Todos os objetos podem acessá-los
    __names = {1 : "ace",
               2 : "two",
               3 : "three",
               4 : "four",
               5 : "five",
               6 : "six",
               7 : "seven",
               8 : "eight",
               9 : "nine",
               10 : "ten",
               11 : "queen",
               12 : "jack",
               13 : "king"}

    # Construtor
    def __init__(self, value, suit):
        self.__value = value
        self.__suit = suitaaaa

        # Verificando o argumento 'value'
        if type(self.__value) == int:
            if self.__value < 1 or self.__value > 13: 
                raise ValueError("'value' need to be an integer between 1 and 13")
        else:
                raise TypeError("'value' need to be an integer not {}".format(type(self.__value)))

    def __str__(self):
        return "{} of {}".format(self.__names.get(self.__value), self.__suit)

    def value(self):
        return self.__value

    def suit(self):
        return self.__suit

    def name(self):
        return self.__str__().capitalize()

