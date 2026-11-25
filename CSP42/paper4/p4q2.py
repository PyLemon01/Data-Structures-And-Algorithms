class Character:
    #UBLIC CharacterName , Colour , SuperStrength , Fly , Invisible : STRING

    def __init__(self , CharacterNameP, ColourP , SuperStrengthP , FlyP , InvisibleP ):
        self.CharacterName = CharacterNameP
        self.Colour = ColourP
        self.SuperStrength = SuperStrengthP
        self.Fly = FlyP
        self.Invisible = InvisibleP

    def GetCharacterName(self):
        return self.CharacterName
    
    def GetColour(self):
        return self.Colour
    
    def GetSuperStrength(self):
        return self.SuperStrength

    def GetFly(self):
        return self.Fly

    def GetInvisible(self):
        return self.Invisible

def ReadData():
    CharList = []
    try:
        file = open("Characters.txt" , "r")
        for line in file:
            txt = line.split(",")
            ObjectN = Character(txt[0],txt[1],txt[2],txt[3],txt[4])
            CharList.append(ObjectN)
        return CharList
        file.close()
    except:
        print("Cannot read flie or file not found.")

def OutputCharacters(CharList):
    for x in range(len(CharList)):
        Char= CharList[x]
        print("Name:" , Char.GetCharacterName() , "Colour:" , Char.GetColour() , "SuperStrength:" , Char.GetSuperStrength() , "Fly:" , Char.GetFly() , "Invisible:" , Char.GetInvisible() , "\n")
        
arrayobj = ReadData()
OutputCharacters(arrayobj)

print("Enter the the criteria for your character:(choose any one of the available options say yes or no)")
c1= input("Superstrength and invisible").lower().strip()
c2 = input("superstrength and fly").lower().strip()
c3 = input("Invisible and fly").lower().strip()
c4 = input("colour and superstrength").lower().strip()
c5 = input("colour and fly").lower().strip()
c6 = input("colour and invisible").lower().strip()

matches = []
if c1 == "yes":
    for x in arrayobj:
        if x.GetSuperStrength() == "yes" and x.GetInvisible() == "yes":
            matches.append(x)

if c2 == "yes":
    for x in arrayobj:
        if x.GetSuperStrength() == "yes" and x.GetFly() == "yes":
            matches.append(x)


if c3 == "yes":
    for x in arrayobj:
        if x.GetFly() == "yes" and x.GetInvisible() == "yes":
            matches.append(x)


if c4 == "yes":
    for x in arrayobj:
        colour = input("Enter your characters colour")
        if x.GetSuperStrength() == "yes" and x.Getcolour() == colour.lower().strip():
            matches.append(x)


if c5 == "yes":
    for x in arrayobj:
        colour = input("Enter your characters colour")
        if x.GetFly() == "yes" and x.Getcolour() == colour.lower().strip():
            matches.append(x)




if c6 == "yes":
    for x in arrayobj:
        colour = input("Enter your characters colour")
        if x.GetInvisible() == "yes" and x.Getcolour() == colour.lower().strip():
            matches.append(x)

        


print("Numbers that meet both criteria:" , len(matches))
OutputCharacters(matches)





        

