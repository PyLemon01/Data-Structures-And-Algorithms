import datetime
class Character():
    #PRIVATE CharacterName : STRING
    #PRIVATE DateOfBirth : DATE
    #PRIVATE Intelligence : REAL
    #PRIVATE Speed : INTEGER
    def __init__(self, CharacternameP , DateOfBirthP, IntelligenceP , SpeedP):
        self.__CharacterName = CharacternameP
        self.__DateOfBirth = DateOfBirthP
        self.__Intelligence = IntelligenceP
        self.__Speed = SpeedP
    
    def SetIntelligence(self , Intellival):
        self.__Intelligence = Intellival

    def GetIntelligence (self):
        return self.__Intelligence
    
    def GetName(self):
        return self.__CharacterName
    
    def ReturnAge(self):
        charyear = self.__DateOfBirth
        age = 2023 - charyear.year
        return age

    def Learn(self):
        Val = self.__Intelligence * 0.1
        self.__Intelligence = self.__Intelligence + Val

    
class MagicCharacter(Character):
    #Private Element : STRING
    def __init__(self ,CharacternameP , DateOfBirthP, IntelligenceP , SpeedP, ElementP):
        super().__init__( CharacternameP , DateOfBirthP, IntelligenceP , SpeedP)
        self.__Element = ElementP
    
    def Learn(self):
        CharElement = self.__Element
        if CharElement == "Fire" or CharElement == "Water":
            newIntelligence = super().GetIntelligence() + ( super().GetIntelligence() * 0.2)
        elif CharElement == "Earth":
            newIntelligence = super().GetIntelligence() + ( super().GetIntelligence() * 0.3) 
        else:
            super().Learn()

        super().SetIntelligence(newIntelligence)

FirstCharacter = Character("Royal", datetime.datetime(2019 , 1 , 1) , 70.0 , 30)
FirstCharacter.Learn()
print("Character's name:", FirstCharacter.GetName() , "Character's age:" , FirstCharacter.ReturnAge() , " Character's Intelligence:" , FirstCharacter.GetIntelligence())

FirstMagic = MagicCharacter("Light", datetime.datetime(2018, 3, 3) , 75.0 , 22 , "Fire" )
FirstMagic.Learn()
print(FirstMagic.GetName() ,"is a character and his intelligence is", FirstMagic.GetIntelligence(), "And his Age is" , FirstMagic.ReturnAge() )

