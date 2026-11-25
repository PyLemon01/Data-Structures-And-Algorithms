class Train:
    #PRIVATE TrainIDNumber : STRING
    #PRIVATE Route : INTEGER

    def __init__(self, TrainIDNumberP , RouteP):
        self.__TrainIDNumber = TrainIDNumberP
        self.__Route = RouteP
    
    def GetRoute(self):
        return self.__Route

    def GetTrainIDNumber(self):
        return self.__TrainIDNumber

train1 = Train("12ADV" , 134 )
train2 = Train("33ART" , 20)
train3 = Train("9FKF" , 3)
train4 = Train("21VBC" , 24)

class Station():
    #PRIVATE NumberPlatforms , NumberTrains : INTEGER
    #PRIVATE StationID : STRING
    #DECLARE Trains:ARRAY[0:9] OF Train

    def __init__(self , StationIDP , NumberPlatformsP):
        self.__StationID = StationIDP
        self.__NumberPlatforms = NumberPlatformsP
        self.__NumberTrains = 0
        self.__Trains = [] 


    def AddTrain(self , trainobj):
        if self.__NumberTrains >= self.__NumberPlatforms:
            return False
        else:
            self.__Trains.append(trainobj)
            self.__NumberTrains = self.__NumberTrains + 1 
            return True
        
    def GetTrains(self):
        if self.__NumberTrains == 0:
            print ("There are no trains")
        else:
            print("The trains at station" , self.__StationID , "are:")
            for x in self.__Trains:
                print(x.GetTrainIDNumber() ,"on route", x.GetRoute())

station1 = Station("STH" , 2)
station2 = Station("NTH" , 1)

result1 = station1.AddTrain(train1)
if result1 == False:
    print("Station is full")
result2 = station1.AddTrain(train2)
if result2 == False:
    print("Station is full")

result3 =station1.AddTrain(train3)
if result3 == False:
    print("Station is full")

result4 =station2.AddTrain(train4)
if result4 == False:
    print("Station is full")
        
station1.GetTrains()
station2.GetTrains()