class Node:
    #PRIVATE TheData : INTEGER
    #PRIVATE NextNode : Node
    def __init__(self , TheDataP ):
        self.__TheData = TheDataP
        self.__NextNode = -1

    def GetData(self):
        return self.__TheData

    def GetNextNode(self):
        return self.__NextNode

    def SetNextNode(self,NodeP):
        self.__NextNode = NodeP

class LinkedList():
    #PRIVATE HeadNode : Node
    def __init__(self):
        self.__HeadNode = -1

    def InsertNode(self , value):
        NewNode = Node(value)
        NewNode.SetNextNode(self.__HeadNode)
        self.__HeadNode = NewNode

    def Traverse(self):
        CurrentNode = self.__HeadNode
        Output = ""
        while CurrentNode != -1:
            dataP = CurrentNode.GetData()
            Output = Output + str(dataP) + " "
            CurrentNode = CurrentNode.GetNextNode()
        return Output


    def RemoveNode(self, ItemToRemove):
        if self.__HeadNode == -1:
            return False
        else:
            if self.__HeadNode.GetData() == ItemToRemove:
                self.__HeadNode = self.__HeadNode.GetNextNode()
                return True
            
            else:
                CurrentNode = self.__HeadNode
                found = False
                while found == False and CurrentNode != -1:
                    if CurrentNode.GetNextNode().GetData() == ItemToRemove:
                        CurrentNode.SetNextNode(CurrentNode.GetNextNode().GetNextNode())
                        found = True
                        
                    else:
                        CurrentNode = CurrentNode.GetNextNode()
                        found = False
                return found

ObjectList = LinkedList()
ObjectList.InsertNode(10)
ObjectList.InsertNode(20)
ObjectList.InsertNode(30)
ObjectList.InsertNode(40)
ObjectList.InsertNode(50)
print(ObjectList.Traverse())
ObjectList.RemoveNode(30)
print(ObjectList.Traverse())
            



                





