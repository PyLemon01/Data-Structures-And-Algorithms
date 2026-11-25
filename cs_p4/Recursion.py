#Input a value and count the number of small vowels letters(a,e,i,o,u) in the value

def RecursiveVowels(value): #house
    
    if len(value) == 0:
        return 0
    else:
        FirstChar = value[0]
        if FirstChar == "a" or FirstChar == "e" or FirstChar == "i" or FirstChar == "o" or FirstChar == "u":
            value = value[1 : len(value)]
            return 1 + RecursiveVowels(value)
        else:
            value = value[1 : len(value)]
            return 0 + RecursiveVowels(value)
        
temp = RecursiveVowels("house")
print (temp)


def IterativeCalculate(Value):
    Total = 0
    endPoint = Value
    while endPoint != 0:
        if Value % endPoint == 0:
            Total = Total + endPoint
        endPoint = endPoint - 1
    return Total
            
temp = IterativeCalculate(10)
print(temp)

def RecursiveCalculate(Value, number):
    if number == 0:
        return 0
    else:
        if Value % number == 0:
            return number + RecursiveCalculate(Value, number -1)
        else:
            return 0 + RecursiveCalculate(Value, number - 1)
        
temp = RecursiveCalculate(50, 50)
print (temp)
    


