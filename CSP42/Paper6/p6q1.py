class BoardObject:
    #PRIVATE Code : STRING
    #PRIVATE Value : INTEGER

    def __init__(self , CodeP , ValueP):
        self.__Code = CodeP
        self.__Value = ValueP

    def GetCode(self):
        return self.__Code

    def GetValue(self):
        return self.__Value

Object1 = BoardObject("A", 2)
Object2 = BoardObject("B", 3)
Object3 = BoardObject("C", 5)
Object4 = BoardObject("D", 2)
Object5 = BoardObject("E", 7)
 
class Board:
    #PRIVATE TheBoard:ARRAY[0:9,0:9] OF Boardbject
    def __init__(self):

        self.__TheBoard = [[BoardObject("-",0)] *10 for x in range(10)]

    def GetObject(self, rownum , colnum):
        return self.__TheBoard[rownum][colnum]

    def SetObject(self, BoardObj , rownum , colnum):
        self.__TheBoard[rownum][colnum] = BoardObj

    def DisplayBoard(self):
        for x in range(10):
            output = " "
            for y in range(10):
                output = output + str(self.__TheBoard[x][y].GetCode()) + "  "
            print (output)
        
Board1 = Board()
Board1.SetObject(Object1 , 0 , 0)
Board1.SetObject(Object2 , 9, 9)
Board1.SetObject(Object3, 4, 5)
Board1.SetObject(Object4, 2 , 2)
Board1.SetObject(Object5 , 8 , 7)
Board1.DisplayBoard()


found = False
while found == False:
    Row = int(input("Enter the row number:"))
    if Row > -1 and Row < 10:
        found =  True

found = False
while found == False:
    Col = int(input("Enter the column number:"))
    if Col > -1 and Col < 10:
        found =  True

myobject = Board1.GetObject(Row , Col)
if myobject.GetCode == "-" and myobject.GetValue() == 0:
    print("Miss")
else:
    print("Code is:" , myobject.GetCode() , "Value is:" , myobject.GetValue())



