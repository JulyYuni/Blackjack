from card import Card
from deck import Deck
from player import Player

# Class to represent class of functions
class Functions:

    # Constructor
    def __init__(self, player):

        self.__hand_value = int
        self.__conclusion = ""
        self.__player_money = player.money()
        self.__player_bet = player.bet()
    
    # Function to ask something to the player and get a valid answer from it
    def answer(computer_answer, computer_choices, right_answer):
        player_answer = input("\n{} \n{}\n\nAnswer: ".format(computer_answer, computer_choices))
        player_answer = player_answer.upper()
        while not player_answer in right_answer:
            player_answer = input("\n{} \n{}\n\n Answer: \n\n".format(computer_answer, computer_choices))
            player_answer = player_answer.upper()
        return player_answer

    # Player chooses how much cards it want to hit
    def hit_plays(self, player, my_deck):
        player_value = player.card_calculator(player)
        player_answer = Functions.answer("Do you want to hit a card?", "Answer with [Y] for yes and [N] for No.", ["Y", "N"])
        while player_answer == "Y":
            player.player_hit(my_deck)
            print("")
            print(player)
            player_value = player.card_calculator(player)
            print ("{} hand total: {}\n\n".format(player.name(), player_value))
            if player_value >= 21:
                break
            
            player_answer = Functions.answer("Do you want to hit a card?", "Answer with [Y] for yes and [N] for No", ["Y", "N"])
            
        if player_answer == "N":
            pass
        return player

    # Calculating the result of the turn, if player won or lost
    def turn_calculator(self, player, player_hand_value, dealer_hand_value):

        if dealer_hand_value > 22:
            self.__player_money, self.__conclusion = player.win()

        elif player_hand_value < 22:
            if player_hand_value > dealer_hand_value:
                self.__player_money, self.__conclusion = player.win()

            elif player_hand_value == dealer_hand_value:
                self.__conclusion = print("\nA tie\n\n")
                print("<" + ("-" * 150) + ">")

            elif player_hand_value < dealer_hand_value:
                self.__player_money, self.__conclusion = player.lose()

        else:
            self.__player_money, self.__conclusion = player.lose()

        print("Money: {}".format(self.__player_money))

        return self.__player_money, self.__conclusion

    # Player chooses it own bet
    def make_bet(self):
        self.__player_bet = Functions.answer("Make your bet!","Choice a value: 5, 25, 50, 125, 250, 500", ["5", "25", "50", "125", "250", "500"])
        self.__player_bet = int(self.__player_bet)
        return self.__player_bet

    #def __str__(self, player):
        #return "Money: {}, Conclusion: {}, Hand value: {}".format(player.money(), self.__conclusion, self.__hand_value)

    #__repr__ = __str__ 


    # List of plays the player can choose
        #plays_words = ["Hit", "Pass", "Double", "Surrender"]
        #plays = [1, 2, 3, 4]
    """
    player_value = player.card_calculator(player)
    dealer_value = dealer.card_calculator(dealer)

        for card in player.hand().deck_list():
            index1 = 0
            list = []
            card_value = card.true_cards_value()
            list.append(card_value)
            hand_value = hand_value + list[index1]

            index1 + 1


    def stand():
        pass

    def split():
        #if deck[1] = self.__attributes.get(self.__VALUE_ATTR) == deck[2] = self.__attributes.get(self.__VALUE_ATTR):
        plays_words = ["Hit", "Pass", "Double", "Surrender", "Split"]
        plays = [1, 2, 3, 4, 5]
        pass

    def surrender():
        print("Are you sure you want to end the game?\n")
        answer("\nAnswer [S] for yes and [N] for no.\n\n")

        user_answer.capitalize()

        if user_answer == "S":
            turn()
        if user_answer == "N":
            pass
        else:
            print ("\nYour answer need to be [S] or [N].\n\n")


languages = ["Português", "Inglês"]
language = languages[2]
if language == languages[2]
    if self.__player_name != "Dealer":
        print_player_name = "Player"
else:
    print_player_name = "Jogador
    
def user_answer():
    self.__user_answer = input("\nChoose your play! \n\n")
    while self.__user_answer not in plays:
        print ("\nYour anwer need to be a number between 1 and 4.\n")
        self.__user_answer = input("\nChoose your play! \n\n")

if __name__ == "__main__":
    player_hand = Deck(0)
    dealer_hand = Deck(0)
    my_deck = Deck(8)
    deck_with_52_cards = Deck(1)
    
    for i in range (0, 2):
        taken_card = my_deck.hit()
        player_hand.receive(taken_card)

        dealer_hand.receive(my_deck.hit())

    print("Player hand: {}".format(player_hand))
    print("Dealer hand: {}".format(dealer_hand))

    cards_discarded = player_hand.discard()
    cards_discarded.extend(dealer_hand.discard())

    print("Discard pile: {}".format(cards_discarded))
    print(player_hand) # Should print an empty string
"""
