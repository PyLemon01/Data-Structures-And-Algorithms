class Node:
    #PRIVATE NodeData: INTEGER
    #PRIVATE LeftNode : Node
    #PRIVATE RightNode : Node
    def __init__(self, NodeDataP):
        self.__NodeData = NodeDataP
        self.__RightNode = None
        self.__LeftNode = None

    def GetLeft(self):
        return self.__LeftNode

    def GetRight(self):
        return self.__RightNode
    
    def GetData(self):
        return self.__NodeData

    def SetLeft(self, NodeL):
        self.__LeftNode = NodeL
    
    def SetRight(self,NodeR):
        self.__RightNode = NodeR

Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(5)
Node4 = Node(15)
Node5 = Node(7)

class Tree:
    #PRIVATE FirstNode : Node
    def __init__(self , FirstNodeP):
        self.__FirstNode = FirstNodeP

    def GetRootNode(self):
        return self.__FirstNode

    def Insert(self , NodeP):
        flag = False
        CurrentNode = self.__FirstNode
        while flag == False:
            if CurrentNode.GetData() > NodeP.GetData():
                if CurrentNode.GetLeft() == None:
                    CurrentNode.SetLeft(NodeP)
                    flag = True
                else:
                    CurrentNode = CurrentNode.GetLeft()
            else:
                if (CurrentNode.GetRight()) == None:
                    CurrentNode.SetRight(NodeP)
                    flag = True
                else:
                    CurrentNode = CurrentNode.GetRight()
        
def OutputInOrder( RootNode):
    if RootNode.GetLeft() != None:
        OutputInOrder(RootNode.GetLeft())

    print(RootNode.GetData())

    if RootNode.GetRight() != None:
        OutputInOrder(RootNode.GetRight())

Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(5)
Node4 = Node(15)
Node5 = Node(7)
treeobject = Tree(Node1)
treeobject.Insert(Node2)
treeobject.Insert(Node3)
treeobject.Insert(Node4)
treeobject.Insert(Node5)
OutputInOrder(treeobject.GetRootNode())






    