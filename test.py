def determineRow(currentLine):
    calcRowH = 127
    calcRowL = 0
    calcRowLIsNot0 = 0
    for i in range():
        #print(str(i)+":"+str(i+1))
        j = i
        i -= 1
        print("j: "+str(j))
        print("i: "+str(i))
        letter = currentLine[i:j]
        print(letter)
with open("5input.txt") as f:
    lines = f.readlines()
    for x in lines:
        print(determineRow(x))
        input()