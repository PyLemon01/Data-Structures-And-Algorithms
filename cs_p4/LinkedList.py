class node:
    #Declare Data :INTEGER
    #Declare nextNode : INTEGER
    def __init__(self,DataP, nextNodeP):
        self.Data = DataP
        self.nextNode = nextNodeP

#Declare LinkedList : ARRAY[0:9] of node


linkedList = [node(1, 1), node(5, 4), node(6, 7), node(7,-1),node(2, 2),node(0, 6), node(0, 8), node(56, 3), node(0, 9), node(0, -1)]

startPointer = 0
EmptyList = 5

def addNode(currentPointer): # start pointer initially
    global linkedList
    global EmptyList
    Data = int(input("Enter your data:"))

    if EmptyList< 0 or EmptyList> 9:
        return False
    else:
        FreeList = EmptyList
        EmptyList = linkedList[EmptyList].nextNode

        newNode = node(Data , -1)
        linkedList[FreeList] = newNode

        PreviousPointer = 0
        while currentPointer != -1:
            PreviousPointer = currentPointer
            currentPointer = linkedList[currentPointer].nextNode 
        linkedList[PreviousPointer] = FreeList
        return True

    
def DeleteNode():
    global linkedList
    global EmptyList

    currentPointer = startPointer
    nodetoremove = int(input("enter the node to remove:"))

    previousPointer = 0
    while currentPointer != -1 and linkedList[currentPointer].Data != nodetoremove:
        previousPointer = currentPointer
        currentPointer = linkedList[currentPointer].nextNode

    if currentPointer == -1:
        return False
    
    else:
        if startPointer == currentPointer:
            startPointer = linkedList[currentPointer].nextNode
        else:
            linkedList[previousPointer].nextNode = linkedList[currentPointer].nextNode
            
        linkedList[currentPointer].data = 0
        linkedList[currentPointer].nextNode = EmptyList
        EmptyList = currentPointer
        return True



def OutputNodes():
    global linkedList
    global startPointer
    currentPointer = startPointer

    while currentPointer != -1:
        print (str(linkedList[currentPointer].Data))
        currentPointer = linkedList[currentPointer].nextNode



def FindValue(currentPointer, searchval):
    global linkedList
    while currentPointer != -1:
        if linkedList[currentPointer].Data == searchval:
            return currentPointer
        else:
            currentPointer = linkedList[currentPointer].nextNode
    
    currentPointer = -1
    return currentPointer 

def OrderedInsertion(currentPointer):
    global linkedList
    global EmptyList
    global startPointer

    valueToInsert = int(input("Enter the data value to insert:"))
    currentPointer = startPointer

    if EmptyList < 0 or EmptyList > 9:
        return False
    else:
        
        freeList = EmptyList
        EmptyList = linkedList[EmptyList].nextNode

        newnode = node(valueToInsert, -1)
        linkedList[freeList] = newnode
            
        previousPointer = 0
        while currentPointer != -1 and linkedList[currentPointer].Data < valueToInsert:
            previousPointer = currentPointer
            currentPointer = linkedList[currentPointer].nextNode

        if startPointer == currentPointer:
            linkedList[freeList].nextNode = currentPointer
            startPointer = freeList

        else:
            linkedList[freeList].nextNode = linkedList[previousPointer].nextNode
            linkedList[previousPointer].nextNode = freeList
        return True


    


        


        
        
        















    