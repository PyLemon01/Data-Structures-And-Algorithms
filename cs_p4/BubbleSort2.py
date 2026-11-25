# Bubblesort
#GLOBAL Animals :ARRAY[0 : 9] of STRING
global Animals
Animals = []
Animals.append("horse")
Animals.append("lion")
Animals.append("rabbit")
Animals.append("mouse")
Animals.append("bird")
Animals.append("deer")
Animals.append("whale")
Animals.append("elephant")
Animals.append("kangaroo")
Animals.append("tiger")

def SortDesc():
    #Declare ArrayLen : INTEGER
    #Declare Temp : STRING
    ArrayLen = len(Animals)
    for x in range(0 , ArrayLen -1 ):
        for y in range( 0 , ArrayLen - x - 1):
            if Animals[y][0] < Animals[y + 1][0]:
                print(y)
                temp = Animals[y + 1]
                Animals[y + 1] = Animals[y]
                Animals[y] = temp
            
print(Animals)
SortDesc()
for x in range(len(Animals)):
    print(Animals[x])
        