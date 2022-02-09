from Card import Card

from random import randint, shuffle

class Deck:
    def __init__(self):
        self.__cards = []
        suits =  ["Hearts", "Diamonds", "Clubs", "Spades"]
        for suit in suits:
            for value in range(1, 14):
                self.__cards.append(Card(value, suit))

    def  shuffle(self):
        for i in range (0,len(self.__cards)*4):
            index1 = randint(0,len(self.__cards))-1
            card1 = self.__cards[index1]
            index2 = randint(0,len(self.__cards))-1
            while index2 == index1:
                index2 = randint(0,len(self.__cards))-1
            card2 = self.__cards [index2]
            self.__cards.remove(card1)
            self.__cards.insert(index1,card2)
            self.__cards.remove(card2)
            self.__cards.insert(index2,card1)

    def shuffle_pythonic(self):
        shuffle(self.__cards)
    
    def sort_pythonic(self):
        self.__cards.sort()
    
    def __str__(self):
        return "   |".join([str(card) for card in self.__cards])

if __name__ == "__main__":
    my_deck = Deck()
    #print(my_deck)
    my_deck.shuffle()
    my_deck.sort_pythonic()
    print(my_deck)