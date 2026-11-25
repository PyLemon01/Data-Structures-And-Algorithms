class node():
    #Declare Data : INTEGER
    #Declare nextNode : INTEGER
    def __init__(self,DataP, nextNodeP):
        self.Data = DataP
        self.nextNode = nextNodeP

#DECLARE linkedList : ARRAY[0:9] OF node
linkedList = [node(1, 1), node(5, 4), node(6, 7), node(7,-1),node(2, 2),node(0, 6), node(0, 8), node(56, 3), node(0, 9), node(0, -1)]
StartPointer = 0
EmptyList = 5

def Addnode(currentPointer):
    global linkedList
    global EmptyList
    Data = int(input("Enter your Data:"))

    if EmptyList < 0 and EmptyList > 9:
        return False
    else:
        FreeList = EmptyList
        linkedList[EmptyList].nextNode = EmptyList

        PreviousPointer = 0
        while currentPointer != -1:
            PreviousPointer = currentPointer
            currentPointer = linkedList[currentPointer].nextNode

        linkedList[currentPointer] = FreeList
        return True


