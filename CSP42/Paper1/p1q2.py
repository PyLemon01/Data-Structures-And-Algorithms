import random
MyArray = []
MyArray = random.sample(range(0, 101), 20)

def PrintArray(Array):
    Output = ""
    for x in range(20):
        Output =  Output  + str(Array[x]) + " " 
    print (Output)

def BubbleSort(Array):
    arrlength = len(Array)
    swap = True
    i =0
    while swap == True and i < (arrlength -1):
        swap = False
        for j in range(arrlength -i -1):
            temp = Array[j]
            if Array[j+1] < temp:
                Array[j] = Array[j+1]
                Array[j+1] = temp
                swap = True
        i = i + 1
    return Array

PrintArray(MyArray)
BubbleSort(MyArray)
print("Sorted")
PrintArray(MyArray)

def RecursiveBinarySearch(array,LowerB,UpperB,value):
    if LowerB > UpperB:
        return -1
    else:
        mid = (LowerB+UpperB)// 2
        if array[mid] == value:
            return mid
        elif value > array[mid]:
            return RecursiveBinarySearch(array,mid + 1,UpperB,value)
        else:
            return RecursiveBinarySearch(array,LowerB ,mid -1,value)

myint = int(input("Enter an integer:"))
result = RecursiveBinarySearch(MyArray , 0 , 19 , myint)
if result == -1:
    print("Not found")
else:
    print("Found at position:" , result)


