class ToyRecord:
    #PRIVATE  NumberBricks : INTEGER
    #PRIVATE Difficulty , Category,ToyName  : STRING
    def __init__(self, ToyNameP, NumberOfBricksP , DifficultyP , CategoryP):
        self.ToyName = ToyNameP
        self.NumberOfBricks = NumberOfBricksP
        self.Difficulty = DifficultyP
        self.Category = CategoryP

def ReadData( array):
    try:
        file = open("Toys.txt" , "r")
        for line in file:
            txt = line.split(",")
            newrecord = ToyRecord(txt[0] , txt[1] ,txt[2],txt[3])
            array.append(newrecord)
        file.close()
        return array
    except:
        print("Cannot open/read the file ")

def OutputToys(array):
    for x in array:
        print(x.ToyName , x.NumberOfBricks , x.Difficulty , x.Category)

#DECLARE ToyArray:ARRAY[0:15] OF ToyRecord
ToyArray = []
ReadData(ToyArray)
OutputToys(ToyArray)

def SearchToys(array):
    userarr = []
    flag = False
    while flag != True:
        userchoice = input("Enter choice of your difficulty level (Medium , Easy , Expert)")
        if userchoice.lower() == "easy":
            for x in array:
                if x.Difficulty.strip() == "Easy":
                    userarr.append(x)
            flag = True
        elif userchoice.lower() == "medium":
            for x in array:
                if x.Difficulty.strip() == "Medium":
                    userarr.append(x)
            flag = True

        elif userchoice.lower() == "expert":
            for x in array:
                if x.Difficulty.strip() == "Expert":
                    userarr.append(x)
            flag = True 
        else:
            flag = False
    return userarr


def WriteToys(array):
    file = open("SelectedToys.txt" , "w")
    for x in array:
        file.write(x.ToyName + "," + str(x.NumberOfBricks) +","+ x.Difficulty +","+ x.Category + "\n")
        


myarr = SearchToys(ToyArray)
WriteToys(myarr)








