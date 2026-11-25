import random
#DECLARE Stack:ARRAY[0:29] OF INTEGER
#DECLARE TopOfStack: INTEGER
Stack = [-1] * 30
TopOfStack = -1

def Push(data):
    #cannot take BYREF so taking them as global
    global Stack
    global TopOfStack

    if TopOfStack  == 29:
        return False
    else:
        TopOfStack = TopOfStack + 1
        Stack[TopOfStack] = data
        
    return True


def Pop():
    global Stack
    global TopOfStack
    if TopOfStack == -1:
        return -999
    else:
        data = Stack[TopOfStack]
        TopOfStack = TopOfStack - 1
    return data

myarray = random.sample(range(0 ,1001) , 40)
flag = True
while flag == True:
    for x in range(40):
        myint = myarray[x]
        result = Push(myint)
        if result == False:
            flag = False
print("Stack is full.")

def FindValues():
    smallestval = 0
    largestval = 0
    val = 0
    while val != -999:
        val = Pop()
        if val > largestval:
            largestval = val
        elif val < smallestval:
            samllestval = val
    print("The larget integer value in the Stack is:" , largestval)
    print("The smallest integer value in the stack is:", smallestval)

FindValues()