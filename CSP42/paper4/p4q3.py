#DECLARE BinaryTree:ARRAY[0:99] OF INTEGER
#DECLARE TreeRootPointer , FirstFreeNodePointer : INTEGER
BinaryTree = [[0 ]*3 for x in range(100)]
TreeRootPointer = -1
FirstFreeNodePointer = 0

def AddNode(data):
    #Cannot take BYREF so taking them as global 
    global BinaryTree
    global TreeRootPointer
    global FirstFreeNodePointer
    if FirstFreeNodePointer <= 99:
        BinaryTree[FirstFreeNodePointer][0] = -1
        BinaryTree[FirstFreeNodePointer][1] = data
        BinaryTree[FirstFreeNodePointer][2] = -1
        if TreeRootPointer == -1:
            TreeRootPointer = 0

        else:
            CurrentPointer = TreeRootPointer
            found = False
            while CurrentPointer != -1 and found == False:
                if data > BinaryTree[CurrentPointer][1]:
                    if BinaryTree[CurrentPointer][2] == -1:
                        BinaryTree[CurrentPointer][2] = FirstFreeNodePointer
                        found = True
                    else: 
                        CurrentPointer = BinaryTree[CurrentPointer][2]
                else:
                    if BinaryTree[CurrentPointer][0] == -1:
                        BinaryTree[CurrentPointer][0] = FirstFreeNodePointer
                        found =True
                    else:
                        CurrentPointer = BinaryTree[CurrentPointer][0]
        FirstFreeNodePointer = FirstFreeNodePointer + 1
    else:
        print("Tree is Full")

        
def OutputArray ():
    #Cannot take BYREF so taking them as global
    global BinaryTree
    
    for CurrentPointer in range(10):
        print( BinaryTree[CurrentPointer][0] , BinaryTree[CurrentPointer][1] , BinaryTree[CurrentPointer][2])


for x in range(10):
    data = int(input("Enter data to add to the binary tree."))
    AddNode(data)

OutputArray()

def InOrder(rootpointer):
    if BinaryTree[rootpointer][0] != -1:
        InOrder(BinaryTree[rootpointer][0])
    print(BinaryTree[rootpointer][1])
    if BinaryTree[rootpointer][2] != -1:
        InOrder(BinaryTree[rootpointer][2])

InOrder(0)


        









