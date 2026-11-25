#DECLARE Queue:Array[0:99] OF STRING
#DECLARE QueueHead , QueueTail , NumberOfItems: INTEGER
Queue = [""]*100
QueueHead = -1
QueueTail = -1
NumberOfItems = 0

def Enqueue(mystr):
    # Cannot take BYREF so taking them as global
    global QueueHead
    global QueueTail
    global NumberOfItems
    global Queue

    if NumberOfItems == 100:
        return False
    else:
        if QueueHead == -1:
            QueueHead = 0
            QueueTail = 0
        Queue[QueueTail] =  mystr
        QueueTail = QueueTail + 1
        NumberOfItems = NumberOfItems + 1
        return True
    
def Dequeue():
    # Cannot take BYREF so taking them as global
    global QueueHead
    global QueueTail
    global NumberOfItems
    global Queue

    if NumberOfItems == 0 :
        return False
    else:
        data = Queue[QueueHead]
        QueueHead = QueueHead + 1
        NumberOfItems = NumberOfItems - 1
        if QueueHead == QueueTail:
            QueueHead = -1
            QueueTail = -1
    return data


def ReadData():
    #Cannot take BYREF so taking them as global
    global Queue
    global QueueTail
    global QueueHead
    global Queue
    global NumberOfItems

    try:
        file = open("BinaryData.txt", "r")
        for line in file:
            if NumberOfItems >= 100:
                break 
            else:
                Enqueue(line)
        file.close()
    except:
        print("Cannot read file")

        
def CompressData():
    global NewString
    NewString = ""
    LastDigit = Dequeue()
    while LastDigit != False:
        count = 1
        result = Dequeue()
        while result == LastDigit:
            count = count + 1
            result = Dequeue()
        NewString = NewString +str(LastDigit) + str(count)
        LastDigit = result
    return NewString
        
            
ReadData()
print(CompressData() , end = " ")







        
            






            


