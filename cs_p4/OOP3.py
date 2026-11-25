class Vehicle:
    #PRIVATE ID : STRING
    #PRIVATE MaxSpeed : INTEGER
    #PRIVATE CurrentSpeed : INTEGER
    #PRIVATE IncreaseSpeed : INTEGER
    #PRIVATE HorizontalPosition : INTEGER
    def __init__(self, ID , MaxSpeed , IncreaseAmount):
        self.__ID = ID
        self.__MaxSpeed = MaxSpeed
        self.__CurrentSpeed = 0
        self.__IncreaseAmount = IncreaseAmount
        self.__HorizontalPosition = 0

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
    
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    
    def SetCurrentSpeed(self , speed):
        self.__CurrentSpeed = speed

    def SetHorizontalPosition(self, position):
        self.__HorizontalPosition = position

    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        
        self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed 
    
    def OutputInfo(self):
        print("Horizontal Position value:", self.__HorizontalPosition)
        print("Current Speed value:" , self.__CurrentSpeed)

class Helicopter(Vehicle):
    #PRIVATE VerticalPosition : INTEGER
    #PRIVATE VerticalChange : INTEGER 
    #PRIVATE MaxHeight :INTEGER
    def __init__(self, ID , MaxSpeed , IncreaseAmount , VerticalChange , MaxHeight ):
        super().__init__( ID, MaxSpeed, IncreaseAmount )
        self.__VerticalPosition = 0
        self.__MaxHeight = MaxHeight
        self.__VerticalChange = VerticalChange
        
    def GetVerticalPosition(self):
        return self.__VerticalPosition 
    def IncreaseSpeed(self):
        self.__VerticalPosition = self.__VerticalPosition + self.__VerticalChange
        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight
        super().IncreaseSpeed()
    
    def OutputInfo(self):
        super().OutputInfo()
        print("Vertical Position value:", self.__VerticalPosition)

car = Vehicle("Tiger", 100 , 20)
helicopter = Helicopter("Lion", 350 , 40 , 3 , 100)
car.IncreaseSpeed()
car.IncreaseSpeed()
car.OutputInfo()
helicopter.IncreaseSpeed()
helicopter.IncreaseSpeed()
helicopter.OutputInfo()
        




    
         
         
