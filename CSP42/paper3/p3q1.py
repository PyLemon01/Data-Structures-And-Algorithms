#DECLARE Queue:ARRAY OF INTEGER
#DECLARE HeadPointer, TailPointer, NumberOfItems: INTEGERS

Queue = [-1]*20
HeadPointer = -1
TailPointer = -1
NumberOfItems = 0

def Enqueue(value):
    #Cannot take variables BYREF so taking them as global
    global HeadPointer
    global TailPointer
    global Queue
    global NumberOfItems

    if NumberOfItems == 20:
        return False
    else:
        TailPointer =  TailPointer + 1
        if TailPointer > 20:
            TailPointer = 0
        if HeadPointer == -1:
            HeadPointer = 0
        Queue[TailPointer] = value
        NumberOfItems = NumberOfItems + 1
        return True
        

for x in range(1 , 26):
    result = Enqueue(x)
    if result == True:
        print( x , "Successful")
    elif result == False:
        print(x , "Unsuccessful")
    
def Dequeue():
    # Cannot take BYREF so taking them as global.abs
    global HeadPointer
    global TailPointer
    global Queue
    global NumberOfItems

    if NumberOfItems == 0:
        HeadPointer = -1
        TailPointer = -1
        return -1
    else:
        dataremoved = Queue[HeadPointer]
        if HeadPointer == 20:
            HeadPointer = 0
            return dataremoved
        HeadPointer = HeadPointer + 1
        NumberOfItems = NumberOfItems - 1
        return dataremoved

print(Dequeue())
print(Dequeue())

