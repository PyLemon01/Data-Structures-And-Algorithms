#DECLARE TreeArray:ARRAY[0:49] OF INTEGER
#DECLARE RootPointer, FreeNode: INTEGER
TreeArray = [[-1 , 0 , -1] for x in range(50)]
global RootPointer
global FreeNode
RootPointer = -1
FreeNode = 0

def AddNode(data):
    # cannot take variable byref hence taking them as global
    global RootPointer
    global TreeArray
    global FreeNode
    

    if FreeNode < 50:
        TreeArray[FreeNode][1] = data
        if RootPointer == -1:
            RootPointer = 0
        else:
            placed = False
            CurrentPointer = RootPointer
            while placed == False:
                if data > TreeArray[CurrentPointer][1]:
                    if TreeArray[CurrentPointer][2] == -1:
                        TreeArray[CurrentPointer][2] = FreeNode
                        placed = True
                    else:
                        CurrentPointer = TreeArray[CurrentPointer][2]
                else:
                    if TreeArray[CurrentPointer][0] == -1:
                        TreeArray[CurrentPointer][0] = FreeNode
                        placed = True
                    else:
                        CurrentPointer = TreeArray[CurrentPointer][0]
        FreeNode = FreeNode + 1    
    else:
        print("Tree is Full")        

try:
    file = open("TreeData.txt","r")
    for x in range(50):
        value = int(file.readline())
        AddNode(value)
    file.close()
except:
    print("File not found")

def WriteAllToFile():
    try:
        file2 = open("Tree.txt", "w")
        for x in range(50):
            line = str(TreeArray[x][0]) + "," + str(TreeArray[x][1]) + "," + str(TreeArray[x][2]) + "\n"
            file2.write(line)
        file2.close()
    except:
        print ("cannot write to file")

treefile = WriteAllToFile()






