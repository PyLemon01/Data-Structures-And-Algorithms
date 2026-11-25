def RecursiveCount(ArrayCopy , NumberElements , DataToFind):
    if NumberElements <= 0:
        return 0
    firstele = ArrayCopy[NumberElements -1 ]
    if firstele == DataToFind:
        NumberElements = NumberElements - 1
        return RecursiveCount(ArrayCopy , NumberElements, DataToFind) + 1
    else:
        NumberElements = NumberElements - 1
        return RecursiveCount(ArrayCopy, NumberElements , DataToFind)

    
myarr = [0 ,5,1,2,5,9,9,6,5,0]
print(RecursiveCount(myarr , 10 , 0))

mystr = "x=0;y=1;x=x+y;y++;"

def SplitData(stringP):
    array = []
    mystr = ""
    for x in range(len(stringP)):
        char = stringP[x]
        if char != ";":
            mystr = mystr + char
        else:
            array.append(mystr)
            mystr = ""
    return array

arr = SplitData(mystr)
for x in range(4):
    print(arr[x])

