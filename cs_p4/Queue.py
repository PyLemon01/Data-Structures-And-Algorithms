# DECLARE Names : ARRAY [ 0 : 9] OF STRING
Names = [""] * 10
HeadPointer = -1
TailPointer = 0

def Enqueue(Data):
    global HeadPointer
    global Names
    global TailPointer

    if TailPointer < 10:
        Names[TailPointer] = Data
        TailPointer = TailPointer + 1

        if HeadPointer == -1:
            HeadPointer = 0 
    else:
        print ("Queue is full.")

def Dequeue():
    global Names
    global TailPointer
    global HeadPointer

    if HeadPointer == -1:
        print ("Queue is Empty.")
    
    else:
        print(Names[HeadPointer])
        HeadPointer = HeadPointer + 1

    if HeadPointer == TailPointer:
        HeadPointer = -1
        TailPointer = 0


Enqueue("manal")
Enqueue("Asim")
Dequeue()

