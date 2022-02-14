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

    # Constructor
    def __init__(self, atribute):
        # Checking if atribute is a dict
        if type(atribute) != dict:
            raise TypeError("'atribute' need to be a dict.")
        self.__atribute = atribute

    def __str__(self):
        text = ""
        for atrr in self.__atribute:
            text = text + "{}: {}\n".format(atrr, self.__atribute[atrr])
        return text

    def atribute(self, atribute):
        return self.__atribute[atribute]

if __name__ == "__main__":
    #atributes_ace_of_hearts = {"value" : 1,
    #                           "suit"  : "Hearts"} 
    #c1 = Card(atributes_ace_of_hearts)

    atributes_in_c1 = {"value": 1,
                       "suit": "Hearts"}
    c1 = Card(atributes_in_c1)
    c1.__atribute = {"value": 1000, "suit": "pirocas"}
    print(c1)
    