class Record:
    #PUBLIC Key: INTEGER
    #PUBLIC Data: STRING

    def __init__(self , KeyP , DataP):
        self.Key = KeyP
        self.Data = DataP


def InitialiseHashTable():
    global HashTable
    HashTable = [[-1] *10 for x in range(1000)]

def Hash( mykey):
    hashresult = mykey % 100
    return hashresult

def InsertData(recobj):
    hashedkey = Hash(recobj.Key)
    placed = False
    x = 0
    while placed == False and x < 10:
        if HashTable[hashedkey][x] == -1:
            HashTable[hashedkey][x] = recobj
            placed = True
        else:
            x = x + 1

def ReadData():
    try:
        file = open("HashTableData.txt" , "r")
        for line in file:
            splitdata = line.split(",")
            myobject = Record(int(splitdata[0]), splitdata[1].strip())
            InsertData(myobject)
        file.close()
    except:
        print("could not read/open the file")


def GetRecord(userkey):
    keyindex = Hash(userkey)
    for x in range(10):
        if HashTable[keyindex][x] != -1:
            if HashTable[keyindex][x].Key == userkey:
                return HashTable[keyindex][x].Data
    return "Not found"


HashTable = []
InitialiseHashTable()
ReadData()
for x in range(5):
    finalkey = int(input("Enter a key number."))
    print(GetRecord(finalkey))





