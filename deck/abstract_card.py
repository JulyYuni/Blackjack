class AbstractCard:

    def __init__(self):
        pass
    
    def __str__(self):
        pass

    def value_of(self, attribute):
        pass

    def keys(self):
        pass

#########################################################################################################################

class SuperTrunfoCard(AbstractCard):
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

    card_ace_of_hearts = {"Value": 1,
                          "Suit": "Hearts"}

    card_snow_white = {"Name": "Branca de Neve",
                       "Simpathy": 49,
                       "Determination": 45}
    
    c1 = Card(card_ace_of_hearts)
    c2 = SuperTrunfoCard(card_snow_white)

    print (c1)
    print (c2)
