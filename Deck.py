from Card import Card

class Deck:
    def __init__(self):
        self.__cards = []
        suits =  ["Hearts", "Diamonds", "Clubs", "Spades"]
        ind = 0
        while ind < 4:
            cards = [Card(1, suits[ind]),
                    Card(2, suits[ind]),
                    Card(3, suits[ind]),
                    Card(4, suits[ind]),
                    Card(5, suits[ind]),
                    Card(6, suits[ind]),
                    Card(7, suits[ind]),
                    Card(8, suits[ind]),
                    Card(9, suits[ind]),
                    Card(10, suits[ind]),
                    Card(11, suits[ind]),
                    Card(12, suits[ind]),
                    Card(13, suits[ind])]
            self.__cards.extend(cards)
            ind+=1
    
    def __str__(self):
        return "\n".join([str(card) for card in self.__cards])

if __name__ == "__main__":
    my_deck = Deck()
    print(my_deck)