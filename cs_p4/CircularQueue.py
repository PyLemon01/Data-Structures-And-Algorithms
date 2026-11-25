# CIRCULAR QUEUE

#DECLARE QueueArray : ARRAY [0, 9] OF STRING
global HeadPointer 
global TailPointer 
global NumOfItems 


QueueArray = [""] * 10
HeadPointer = 0
TailPointer = 0
NumOfItems = 0

#Data cannot be taken by ref so i have declared the varables as global
def Enqueue(DataToAdd):
    global HeadPointer
    global TailPointer
    global NumOfItems
    global QueueArray

    if NumOfItems >= 10:
        return False
    QueueArray[TailPointer] = DataToAdd
    if TailPointer >= 9:
        TailPointer = 0
    else:
        TailPointer = TailPointer + 1
    
    NumOfItems = NumOfItems + 1
    return True

def Dequeue():
    global QueueArray
    global HeadPointer
    global TailPointer
    global NumOfItems

    if NumOfItems == 0:
        return False
    else:
        value = QueueArray[HeadPointer]
        HeadPointer = HeadPointer + 1
        if HeadPointer > 9:
            HeadPointer = 0
        NumOfItems = NumOfItems - 1
        return value









    
Enqueue("Manal")
Enqueue("Umair")
Enqueue("Uzair")
Enqueue("Asim")
Enqueue("Sarah")
Enqueue("Po")
print(QueueArray)
print(NumOfItems)