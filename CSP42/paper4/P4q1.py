#DECLARE DataArray: Array[0:14] OF STRING
DataArray = [""]*15

def CreateArray():
    for x in range(15):
        dataP = str(input("Enter data to be added to the string:").lower())
        DataArray[x] = dataP

def OutputArray():
    Output = ""
    for x in range(15):
        Output = Output + str(DataArray[x]) + " "
    print(Output)

CreateArray()
OutputArray()

def FindWords():
    mystr = str(input("Enter the word:").lower())
    count = 0
    for x in range(15):
        if DataArray[x] == mystr:
            count = count + 1
    print("The number of times word appeared in the array:" , count)

def SortLength():
    #DECLARE Temp , i , j , Last: INTEGER
    #DECLARE swap : BOOLEAN
    Last = len(DataArray)
    i = 0
    swap = True 
    while swap == True and i < (Last -1):
        swap = False
        for j in range(Last - i -1):
            if len( DataArray[j + 1]) < len(DataArray[j]):
                Temp = DataArray[j+1]
                DataArray[j + 1] = DataArray[j]
                DataArray[j] = Temp
                swap = True
        i = i + 1

FindWords()
SortLength()
OutputArray()






