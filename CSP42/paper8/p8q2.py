class Avatar:
    #PRIVATE TheName, Hair : STRING
    #PRIVATE Glasses: BOOLEAN
    #PRIVATE Age: INTEGER

    def __init__(self , TheNameP , HairP , GlassesP , AgeP):
        self.__TheName = TheNameP
        self.__Hair = HairP
        self.__Glasses = GlassesP
        self.__Age = AgeP

    def GetName(self):
        return self.__TheName

    def GetAge(self):
        return self.__Age

    def MeetCriteria(self , haircolour , glasses):
        print("File glasses:", repr(self.__Glasses), "User glasses:", repr(glasses))
        print("File hair:", repr(self.__Hair), "User hair:", repr(haircolour))
        if self.__Glasses == glasses.strip() and self.__Hair == haircolour.strip():
            return True
        else:
            return False

def LoadAvatars():
    global AvailableAvatars
    try:
        file = open("AvatarFile.txt" , "r")
        for line in file:
            splitdata = line.split()
            object1 = Avatar(splitdata[0].strip(),splitdata[1].strip(),splitdata[2].strip(),splitdata[3].strip())
            AvailableAvatars.append(object1)
    except:
        print("Cannot open or read the file")

AvailableAvatars = []
LoadAvatars()

def EnterChoices():
    global userarray
    flag1 = False
    haircolour = ["black", "blonde" , "brown" , "pink" , "red" , "green"]
    while flag1 == False:
        avahair = input("Enter your avatars hair colour it can be:(black, blonde , brown, pink, red, green)")
        if avahair.lower() == "black" or avahair.lower() == "blonde" or avahair.lower() == "brown" or avahair.lower() == "pink" or avahair.lower() == "red" or avahair.lower() == "green" :
            flag1 = True
    flag2 = False
    while flag2 == False:
        avaglasses  = input("Enter 'yes' if your avatar has glasses else enter 'no'" )
        if avaglasses.lower() == "yes" or avaglasses.lower() == "no":
            flag2 = True
    if avaglasses.lower() == "yes":
        avaglasses = "True"
    elif avaglasses.lower() == "no":
        avaglasses = "False"
            
    for x in AvailableAvatars:
        valid = x.MeetCriteria(avaglasses,avahair)
        if valid == True:
            userarray.append(x)

userarray = []
EnterChoices()
print("number of avatars that match your criteria" , len(userarray))
for x in userarray:
    print("Avatar name:" , x.GetName() , "Avatar age:" , x.GetAge())

