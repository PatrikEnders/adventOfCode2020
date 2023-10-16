trees = 0
posx = 1


with open("3input.txt") as f:
    lines = f.readlines()
    for x in lines:
        right = False
        while right == False:
            standort = x[posx-1:posx]
            right = True
            if standort == ".":
                posx += 3
            elif standort == "#":
                trees += 1
                posx += 3
            elif standort == "" or standort == "\n":
                posx = posx-31
                right = False
print(trees)