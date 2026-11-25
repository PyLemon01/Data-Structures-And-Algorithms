#DECLARE TheData:ARRAY[0:8] OF STRING
TheData = ["laptop" , "tablet", "printer","computer", "processor" , "monitor" , "memory", "cable" , "touchscreen" ]

def FindLongestShortest(array):
    smallesttxt = array[0]
    Longesttxt = ""
    for x in range(len(array)):
        txt = array[x]
        if len(txt) > len(Longesttxt):
            Longesttxt = txt
        if len(txt) < len(smallesttxt):
            smallesttxt = txt
    print("Word with most characters:", Longesttxt)
    print("Word with least characters:", smallesttxt)

FindLongestShortest(TheData)


def InsertionSort(array):
    temp = ""
    last = len(array)
    if last <= 1:
        return False
    else:
        for x in range(last):
            position = x
            temp = array[position]
            while position > 0 and array[position-1] > temp:
                array[position] = array[position -1]
                position = position - 1
            array[position] = temp
        return array

print("Before sorting:" )
print(TheData)
InsertionSort(TheData)
print ("After sorting")
print(TheData)

