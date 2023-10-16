currentHighest = 0

def setHighest(new):
    global currentHighest
    if new > currentHighest:
        currentHighest = new

def getID(reihe, platz):
    return reihe*8+platz

def determineRow(currentLine):
    calcRowH = 127
    calcRowL = 0
    calcRowLIsNot0 = 0
    for i in range(6):
        #print(str(i)+":"+str(i+1))
        j = i+1
        letter = currentLine[i:j]
        #print(letter)
        if calcRowL > 0:
            calcRowLIsNot0 += calcRowL
            calcRowH -= calcRowL
            calcRowL -= calcRowL
            #print("nicht 0: "+str(calcRowH))
        if letter == "F":
            #print("F: "+str(calcRowH))
            calcRowH = int(calcRowH/2)
            lastCalc = "F"
            #print("F: "+str(calcRowH))
        else:
            #print("B: "+str(calcRowL))
            calcRowL = int(calcRowH/2)+1
            lastCalc = "B"
            #print("B: "+str(calcRowL))
    if lastCalc == "B":
        return calcRowL+1+calcRowLIsNot0
    if lastCalc == "F":
        return calcRowH-1+calcRowLIsNot0

def determineColumn(currentLine):
    calcRowH = 7
    calcRowL = 0
    calcRowLIsNot0 = 0
    for i in range(2):
        #print(str(i)+":"+str(i+1))
        i +=8
        j = i+1
        letter = currentLine[i:j]
        if calcRowL > 0:
            calcRowLIsNot0 += calcRowL
            calcRowH -= calcRowL
            calcRowL -= calcRowL
            #print("nicht 0: "+str(calcRowH))
        if letter == "L":
            #print("F: "+str(calcRowH))
            calcRowH = int(calcRowH/2)
            lastCalc = "L"
            #print("F: "+str(calcRowH))
        else:
            #print("B: "+str(calcRowL))
            calcRowL = int(calcRowH/2)+1
            lastCalc = "R"
            #print("B: "+str(calcRowL))
    if lastCalc == "R":
        return calcRowL+1+calcRowLIsNot0
    if lastCalc == "L":
        return calcRowH-1+calcRowLIsNot0

with open("5input.txt") as f:
    lines = f.readlines()
    for x in lines:
        #print(determineRow(x))
        #print(determineColumn(x))
        setHighest(getID(determineRow(x), determineColumn(x)))
print(currentHighest)