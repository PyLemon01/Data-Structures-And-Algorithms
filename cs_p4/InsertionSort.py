ArrayData = [ 2, 8, 4, 5, 3 ]

ArraySize = len(ArrayData)

for Pointer in range(1 , ArraySize):
    val = ArrayData[Pointer]
    HolePosition = Pointer

    while HolePosition > 0 and ArrayData[HolePosition-1] > val:
        ArrayData[HolePosition] = ArrayData[HolePosition - 1]
        HolePosition = HolePosition -1
    ArrayData[HolePosition] = val

print(ArrayData)