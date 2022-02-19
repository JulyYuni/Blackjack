from card import Card
from deck import Deck

# Class to represent class of players
class Player:
    
    # Constructor

    def __init__(self, name, money, bet):
        self.__name = name
        self.__hand = Deck()
        self.__bet = bet
        self.__money = money
        self.__discard_list = Deck()

    def hit1(self, my_deck):
        return self.__hand.receive(my_deck.hit())

    def discard1(self):
        cards_discarded = self.__hand.discard()
        return self.__discard_list.receive(cards_discarded)

    def card_calculator(player1, dealer):
        pass

    def money(self):
        return self.__money

    def bet(self):
        return self.__bet

    def name(self):
        return self.__name

    def hand(self):
        return self.__hand
        
    def __str__(self):
        return "{}: {}".format(self.__name, self.__hand)

    __repr__ = __str__

    



if __name__ == "__main__":
    ju = Player("Júlia", 1000)
    will = Player("Willian", 500)
