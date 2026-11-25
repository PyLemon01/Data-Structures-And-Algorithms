Names = [""] * 5
stackPointer = 0

def push(Value):
    global Names
    global stackPointer

    if stackPointer > 4:
        print(" List is full.")
    else:
        Names[stackPointer] = Value
        stackPointer = stackPointer +1

def pop():
    global Names
    global stackPointer

    if stackPointer == 0:
        print("Stack is Empty.")
    else:
        stackPointer = stackPointer -1
        print(Names[stackPointer])

push("Manal")
push ("Asim")
print (Names)
pop()
push("Olive")
print(Names)
 

Names = [""] * 5
StackPointer = -1

def push(Val):
    global Names
    global StackPointer

    if StackPointer == 4:
        print("List is full.")
    else:
        StackPointer = StackPointer + 1
        Names[StackPointer] = Val

    
def pop():
    global Names
    global StackPointer

    if StackPointer == -1:
        print("List is empty")
    else:
        print(Names[StackPointer])
        StackPointer = StackPointer - 1
#DECLARE StackData : ARRAY [0 : 9] OF INTEGER
#DECLARE stackPointer : INTEGER
global StackData
global stackPointer

StackData = [0] * 10
stackPointer = 0

def push(Values):
    global StackData
    global stackPointer

    if stackPointer > 10:
        print ("List full.")
    else:
        Names[StackPointer] = Values
        StackPointer = StackPointer + 1

def pop():
    global StackData
    global StackPointer

    if StackPointer == 0:
        print("List Empty")
    else:
        StackPointer = StackPointer -1
        print(Names(StackPointer))

def outval():
    global StackData
    print(StackPointer)
    for x in range(10):
        print(StackData[x])

def push(Value):
    global StackData 
    global StackPointer
    if StackPointer > 9:
        return False
    else:
        Names[StackPointer] = Value
        StackPointer = StackPointer + 1
        return True

    
    