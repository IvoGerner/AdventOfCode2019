f = open("input/inputD3.txt", 'r')

L = f.readline().split(",")
M = f.readline().split(",")


# dictionary, store all positions. Go by min and max where intersections are.
# tupels
#

def pather(inputList):
    currentPos = (0, 0)
    distanceDict = {0: 0}
    for i in range(len(inputList)):
        step = int(''.join(x for x in inputList[i] if x.isdigit()))
        if 'R' in inputList[i]:
            for x in range(step):
                distanceDict[currentPos[0] + x] = currentPos[1]
            currentPos = (currentPos[0] + step, currentPos[1])
            # print(inputList[i], currentPos)
        elif 'L' in inputList[i]:
            for x in range(step):
                distanceDict[currentPos[0] - x] = currentPos[1]
            currentPos = (currentPos[0] - step, currentPos[1])
            # print(inputList[i], currentPos)
        elif 'U' in inputList[i]:
            for y in range(step):
                distanceDict[currentPos[0]] = currentPos[1] + y
            currentPos = (currentPos[0], currentPos[1] + step)
            # print(inputList[i], currentPos)
        elif 'D' in inputList[i]:
            for y in range(step):
                distanceDict[currentPos[0]] = currentPos[1] - y
            currentPos = (currentPos[0], currentPos[1] - step)
            # print(inputList[i], currentPos)

    return distanceDict


dictL = (pather(L))
print(dictL)

dictM = (pather(M))
print(dictM)

# d_inter = dict(set(dictL.items()).intersection(dictM.items()).intersection())
# print(d_inter)
