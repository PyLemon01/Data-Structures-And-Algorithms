class TheObject:
    #PUBLIC ObjectType: STRING
    #PUBLIC Amount : INTEGER

    def __init__(self, ObjectTypeP , AmountP):
        self.ObjectType = ObjectTypeP
        self.Amount = AmountP

class Path:
    #PUBLIC BoardArray:Array[0 :99] OF TheObject
    #PUBLIC NumberOfSpaces : INTEGER
    def __init__(self, NumberOfSpacesP):
        self.NumberOfSpaces = NumberOfSpacesP
        self.BoardArray = []
        myobject = TheObject("",-1)
        for x in range(100):
            self.BoardArray.append(myobject)

    def GetNumberOfSpaces(self):
        return self.NumberOfSpaces

    def InitialiseData(self , array):
        arrlength = len(array)
        if arrlength > self.NumberOfSpaces:
            return False
        for x in range(arrlength):
            self.BoardArray[x] = array[x]
        return True

    def ReturnPath(self):
        for x in self.BoardArray:
            if x.ObjectType != "" and x.Amount != -1:
                print(x.ObjectType ,  x.Amount)

    def GetPathObject(self, index):
        return self.BoardArray[int(index)]
    
ArrayOfObjects = []
object1 = TheObject("money",50)
object2 = TheObject("experience",100)
object3 = TheObject("money" , 200)
object4 = TheObject("money" , 20)
object5 = TheObject("experience" , 30)

ArrayOfObjects.append(object1)
ArrayOfObjects.append(object2)
ArrayOfObjects.append(object3)
ArrayOfObjects.append(object4)
ArrayOfObjects.append(object5)

Path1 = Path(5)
Path1.InitialiseData(ArrayOfObjects)
Path1.ReturnPath()



                




             