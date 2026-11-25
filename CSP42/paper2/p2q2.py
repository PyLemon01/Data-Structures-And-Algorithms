#Declare DataArray:ARRAY[0:13] OF INTEGER
DataArray = [0, 3, 4, 56, 67, 44, 43, 32, 31, 345, 45, 6, 54, 1]

def InsertionSort(array):
    last = len(array)
    for i in range(last):
        position = i
        temp = array[position]

        while position > 0 and temp < array[position-1]:
            array[position] = array[position -1]
            position = position -1
        
        array[position] = temp
    return array


def OutputArray(array):
    Output = ""
    length = len(array)
    for x in range(length):
        Output = Output + str(array[x]) + " "
    print(Output)

OutputArray(DataArray)
print(InsertionSort(DataArray))
OutputArray(DataArray)

def Search(DataArray , ItemToFind):
    upperbound = (len(DataArray)-1)
    lowerbound = 0
    found = False
    while found == False and upperbound >= lowerbound:
        mid = (upperbound + lowerbound) // 2
        if DataArray[mid] == ItemToFind:
            return mid
            found = True
        elif ItemToFind > DataArray[mid]:
            lowerbound = mid+1
        else:
            upperbound = mid - 1 
    return -1

print(Search(DataArray , 0))
print(Search(DataArray , 345))
print(Search(DataArray , 67))
print(Search(DataArray , 2))
