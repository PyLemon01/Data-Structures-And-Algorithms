class Character():

    #PRIVATE name : STRING
    #PRIVATE xcord : INTEGER
    #PRIVATE ycord : INTEGER
    def _init_(self,nameP, xcordP, ycordP):
        self.__name = nameP
        self.__xcord = xcordP
        self.__ycord = ycordP

    def getname(self):
        return self.__name
    
    def Getx(self):
        return self.__xcord
    
    def GetY(self):
        return self.__ycord
    
    def ChangePosition(self,Xchange, Ychange):
        self.__xcord = self.__xcord + Xchange
        self.__ycord = self.__ycord + Ychange

#DECLARE characters : ARRAY [0 : 9] OF Character
characters = []
try:
    file = open("Characters.txt", "r")
    for x in range(10):
        name = file.readline().strip()
        xcordi = int(file.readline().strip())
        ycordi = int(file.readline().strip())
        charobj = Character(name , xcordi, ycordi)
        characters.append(charobj)
except:
    print("File not Found")



flag = False
while flag == False:
    Username = input("Enter characters name:")
    for x in range(10):
        listname = characters[x].getname()
        if listname.lower() == Username.lower():
            charindex = x
            flag = True
Flag = True
while Flag == True:
    move = input("Enter any ONE W , D , S , A:")
    if move.upper() == "W":
        characters[charindex].ChangePosition(0,1) 
        Flag = False
    elif move.upper() == "A":
        characters[charindex].ChangePosition(-1,0)
        Flag = False
    elif move.upper() == "S":
        characters[charindex].ChangePosition(0,-1)
        Flag = False
    elif move.upper() == "D":
        characters[charindex].ChangePosition(1,0)
        Flag = False

print(Username  , "has changed co-ordinates to X =" , characters[charindex].GetX()  ,  "and Y =" , characters[charindex].GetY())

