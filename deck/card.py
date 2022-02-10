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
    def __init__(self, atribute):
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

    c1 = Card({"value" : 1, "suit"  : "Hearts"})
    print(c1)

    c1 = Card("banana")
    print(c1)
    