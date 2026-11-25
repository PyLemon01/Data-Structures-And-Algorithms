#DECLARE Queue:ARRAY[0:49] OF INTEGER
#DECLARE HeadPointer : INTEGER
#DECLARE TailPointer : INTEGER
Queue = [-1] * 50
HeadPointer = -1
TailPointer = -1

def Enqueue(value):
    #Cannot take the variables BYREF so taking them as global.
    global Queue
    global HeadPointer
    global TailPointer

    if TailPointer < 50:
        TailPointer = TailPointer + 1
        Queue[TailPointer] = value
        if HeadPointer == -1:
            HeadPointer = 0    

        return True
    else:
        return False

def Dequeue():
    #Cannot take variables BYREF so taking them as global
    global HeadPointer
    global TailPointer 
    global Queue

    if HeadPointer == -1:
        return -1
    else: 
        value = Queue[HeadPointer]

        if HeadPointer == TailPointer:
            TailPointer = -1
            HeadPointer = -1
        else: 
            HeadPointer = HeadPointer + 1

    return value
         

def CreateQueue():
    try:
        file = open("QueueData.txt" , "r")
        for line in file:
            myint = int(line)
            result = Enqueue(myint)
            if result == False:
                break
        print("Queue is full.")
        file.close()
    except:
        print("File is not found.")

        


CreateQueue()
Output = 0
for x in range(50):
    number = Dequeue()
    if number != -1:
        Output = Output + number

print("The total sum of numbers is " , Output)
    