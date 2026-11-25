#DECLARE Queue:ARRAY[0:9] OF INTEGER
#DECLARE HeadPointer , TailPointer : INTEGER
Queue = [-1] * 10 
HeadPointer = -1
TailPointer = -1

def Enqueue(Val):
    #Cannot take BYREF so taking them as global
    global HeadPointer
    global TailPointer
    global Queue
    if TailPointer >= 10:
        return False
    else:
        if HeadPointer  == -1:
            HeadPointer = 0
            TailPointer = 0
        
        Queue[TailPointer] = Val
        TailPointer = TailPointer + 1
    return True




def Dequeue():
    #Cannot take BYREF so taking them as global
    global HeadPointer
    global Queue
    global TailPointer

    if HeadPointer == TailPointer:
        HeadPointer = -1
        TailPointer = -1
        return -1
    else:
        data = Queue[HeadPointer]
        HeadPointer = HeadPointer + 1
        return data
    


for x in range(6):
    myint = int(input("Enter an integer value:"))
    result = Enqueue(myint)
    if result == False:
        print('Queue is full')
        break

for x in range(4):
    result = Dequeue()
    if result == -1:
        print ("Queue is empty.")
    else:
        print(result)
