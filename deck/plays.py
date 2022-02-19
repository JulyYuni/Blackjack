from card import Card
from deck import Deck
from player import Player

class Plays:

    def __init__(self):
        self.__conclusion = ""
        self.__hand_value = int

    plays_words = ["Hit", "Pass", "Double", "Surrender"]
    plays = [1, 2, 3, 4]
   
    def answer(computer_answer):
        return input("\n{} \n\n".format(computer_answer))

    #This should be modified and replaced inside the Deck class
    def card_calculator(self, player):
        hand_value = 0

        for card in player.hand().deck_list():
            index1 = 0
            list = []
            card_value = card.true_cards_value()
            list.append(card_value)
            hand_value = hand_value + list[index1]

            index1 + 1

        return hand_value


    #This might be on the Turn class
    def turn_calculator(self, player, player_hand_value, dealer_hand_value, player_name, dealer_name):
        player_money = player.money()
        player_bet = player.bet()
        if player_hand_value > dealer_hand_value:
            player_money = player_money + player_bet
            self.__conclusion = "{}'s Victory".format(player_name)

        if player_hand_value == dealer_hand_value:
            self.__conclusion = "A tie"

        if player_hand_value < dealer_hand_value:
            player_money = player_money - player_bet
            self.__conclusion = "{}'s Victory".format(dealer_name)

        return player_money, self.__conclusion 


    def __str__(self, player):
        return "Money: {}, Conclusion: {}, Hand value: {}".format(player.money(), self.__conclusion, self.__hand_value)

    __repr__ = __str__ 

        #def double():
        #return player.bet *2


    """def hit():
        pass

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
"""
