
def findnode(SearchItem):
    global RootPointer
    global ArrayNode
    currentPointer = RootPointer

    while currentPointer != -1 and ArrayNode[CurrentPointer][1] != SearchItem:
        if SearchItem > ArrayNode[CurrentPointer][1]:
            CurrentPointer = ArrayNode[CurrentPointer][2]
        else:
            CurrentPointer = ArrayNode[CurrentPointer][0]
            

    print (CurrentPointer)


# Concept of winding and unwinding
RootPointer = 0
FreeNode = 6
BinaryTree = [[1, 20, 5],[2, 15, -1],[-1, 3, 3],[-1, 9, 4],[-1, 10, -1],[-1, 59, -1],[-1, -1, -1]]

def InOrder(Root):
    global BinaryTree
    if BinaryTree[Root][0] != -1:
        InOrder(BinaryTree[Root][0])
    print (BinaryTree[Root][1])
    if BinaryTree[Root][2] != -1:
        InOrder(BinaryTree[Root][2])

def PreOrder(Root):
    global BinaryTree
    print(BinaryTree[Root][1])
    if BinaryTree[Root][0] != -1:
        PreOrder(BinaryTree[Root][0])
    if BinaryTree[Root][2] != -1:
        PreOrder(BinaryTree[Root][2])

def PostOrder(Root):
    global BinaryTree
    if BinaryTree[Root][0] != -1:
        PostOrder(BinaryTree[Root][0])
    if BinaryTree[Root][2] != -1:
        PostOrder(BinaryTree[Root][2])
    print(BinaryTree[Root][1])

    
