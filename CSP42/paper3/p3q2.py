filedata = []
def ReadData():
    filename = str(input("Enter the filename:"))
    try:
        file = open(filename, "r")
        for line in file:
            filedata.append(line)
        file.close()
        return filedata
    except:
        print("File not found.")



def StoreData(DataToStore , fileN):
    try:
        file = open(fileN , "a")
        for x in range(len(DataToStore)):
            file.write(DataToStore[x] + "\n")
        file.close()
    except:
        print("File not found")



def SplitData(DataArray):
    red = []
    blue = []
    green = []
    yellow = []
    orange = []
    pink = []
    for x in range(len(DataArray)):
        txt = DataArray[x].split(",")
        if txt[1].strip() == "red":
            red.append(txt[0])
        elif txt[1].strip() == "blue":
            blue.append(txt[0])
        elif txt[1].strip() == "green":
            green.append(txt[0])
        elif txt[1].strip() == "yellow":
            yellow.append(txt[0])
        elif txt[1].strip() == "orange":
            orange.append(txt[0])
        else:
            pink.append(txt[0])
    StoreData(red , "Red.txt")
    StoreData(blue , "Blue.txt")
    StoreData(green , "Green.txt")
    StoreData(orange , "Orange.txt")
    StoreData(yellow , "Yellow.txt")
    StoreData(pink , "Pink.txt")

ReadData()
SplitData(filedata)
