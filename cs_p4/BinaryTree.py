ArrayNode = [[0] * 3 for x in range [20]]
FreeNode = 0
RootPointer = -1

def AddNode():
    global RootPointer
    global ArrayNode
    global FreeNode

    DataNode = int(input("Enter your data:"))

    if FreeNode <= 19:
        ArrayNode[FreeNode[0]] = -1
        ArrayNode[FreeNode[1]] = DataNode
        ArrayNode[FreeNode[2]] = -1

        if RootPointer == -1:
            RootPointer = 0
        else:
            Placed = False
            CurrentPointer = RootPointer
            
            while Placed == False:
                if DataNode < ArrayNode[CurrentPointer][1]:
                    if ArrayNode[CurrentPointer][0] == -1:
                        ArrayNode[CurrentPointer][0] = FreeNode
                        Placed = True
                    else:
                        CurrentPointer = ArrayNode[CurrentPointer][0]
                else:
                    if ArrayNode[CurrentPointer][2] == -1:
                        ArrayNode[CurrentPointer][2] = FreeNode
                        Placed = True
                    else:
                        CurrentPointer = ArrayNode[CurrentPointer][2]
        FreeNode = FreeNode + 1
    else:
        print("Tree is full")

