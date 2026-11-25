
class Card:
    #PRIVATE Colour : STRING
    #PRIVATE Number : INTEGER
    def __init__(self, NumberP, ColourP):
        self.__Colour = ColourP
        self.__Number = NumberP
    
    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour
    
Onered = Card( 1 , "red")
Twored = Card( 2 , "red")
Threered = Card( 3 , "red")
Fourred = Card( 4 , "red") 
Fivered = Card(5 , "red")
Oneyellow = Card( 1 , "yellow")
Twoyellow = Card( 2 , "yellow")
Threeyellow = Card( 3 , "yellow")
Fouryellow = Card( 4 , "yellow") 
Fiveyellow = Card(5 , "yellow")
Oneblue = Card( 1 , "blue")
Twoblue = Card( 2 , "blue")
Threeblue = Card( 3 , "blue")
Fourblue = Card( 4 , "blue") 
Fiveblue = Card(5 , "blue")

class Hand:
    #PRIVATE Cards :ARRAY [0, 9] OF CARD
    #PRIVATE FirstCard : INTEGER
    #PRIVATE NumberCard : INTEGER
    
    def __init__(self, card1, card2, card3, card4, card5, ):
        self.__Cards = []
        self.__Cards.append(card1)
        self.__Cards.append(card2)
        self.__Cards.append(card3)
        self.__Cards.append(card4)
        self.__Cards.append(card5)
        self.__FirstCard = 0
        self.__NumberCard = 5

    def GetCard(self,index):
        return self.__Cards[index]


Player1= Hand(Onered, Twored, Threered, Fourred, Oneyellow)
Player2 = Hand(Twoyellow, Threeyellow, Fouryellow, Fiveyellow, Oneblue)

def CalculateValue(Player):
    score = 0
    for x in range(5):
        playercard = Player.GetCard(x)
        color = playercard.GetColour()
        number = playercard.GetNumber()
        if color == "red":
            score = score + 5
        elif color == "blue":
            score = score + 10
        elif color == "yellow":
            score = score + 15
    return score

score1 = CalculateValue(Player1)
score2 = CalculateValue(Player2)
if score1 > score2:
    print("Player 1 wins!!")
elif score2 > score1:
    print("Player 2 wins!!")
else:
    print("Draw")