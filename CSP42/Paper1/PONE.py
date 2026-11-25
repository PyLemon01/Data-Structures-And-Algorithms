class Bird:
    #PRIVATE DistancePerHour : REAL
    #PRIVATE Species : STRING
    #PRIVATE XPosition : REAL
    #PRIVATE YPosition : REAL
    def __init__(self, SpeciesP , DistancePerHourP ):
        self.__Species = SpeciesP
        self.__DistancePerHour = DistancePerHourP
        self.__XPosition = 500.0
        self.__YPosition = 500.0

    def GetPosition(self):
        return "X =" , self.__XPosition , "Y =" , self.__YPosition

    def GetSpecies(self):
        return self.__Species

    def Move(self , Direction , minutes):
        #PRIVATE Direction : STRING
        #PRIVATE minutes: REAL
        DistanceTravelled = (self.__DistancePerHour)/60*minutes
        
        if Direction == "N":
            self.__YPosition = self.__YPosition + DistanceTravelled
        elif Direction == "S":
            self.__YPosition = self.__YPosition - DistanceTravelled
        
        elif Direction == "E":
            self.__XPosition = self.__XPosition + DistanceTravelled
        
        else:
            self.__XPosition = self.__XPosition - DistanceTravelled

#Declare bird1 , bird2: Bird

bird1 = Bird("Cockatiel" , 71.0)
bird2 = Bird("Macaw", 56.0)

print ("bird1 is a" , bird1.GetSpecies() , "and its current position is" , bird1.GetPosition() )
print ("bird2 is a" , bird2.GetSpecies() , "and its current position is" , bird2.GetPosition() )

flag = False
while flag == False:
    BirdSelected = str(input("Enter the Bird of your choice:(bird1 or bird2)").lower())
    if BirdSelected == "bird1":
        direction = str(input("Enter the direction the bird travels: E , W , S , N:").upper())
        timeM = float(input("Enter the time to the nearest minute the bird has been travelling"))
        if direction == "E" or direction == "W" or direction == "N" or direction == "S":
            bird1.Move(direction , timeM)
            print(bird1.GetPosition())
            flag = True
        

    elif BirdSelected == "bird2":
        direction= str(input("Enter the direction the bird travels: E , W , S , N:").upper())
        timeM = float(input("Enter the time to the nearest minute the bird has been travelling"))
        if (direction == "E" or direction == "W" or direction == "N" or direction == "S") :
            bird2.Move(direction , timeM)
            print(bird2.GetPosition())
            flag = True
    
    else:
        flag = False











