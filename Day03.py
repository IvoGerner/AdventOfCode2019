f = open("input/inputD3.txt", 'r')

L = f.readline().split(",")
M = f.readline().split(",")


# set, store all positions. Go by min and max where intersections are.
# tupels
#

def pather(inputList):
    currentPos = (0, 0)
    path = set()
    for i in range(len(inputList)):
        step = int(''.join(x for x in inputList[i] if x.isdigit()))
        if 'R' in inputList[i]:
            for x in range(step):
                path.add((currentPos[0] + x, currentPos[1]))
            currentPos = (currentPos[0] + step, currentPos[1])
            # print(inputList[i], currentPos)
        elif 'L' in inputList[i]:
            for x in range(step):
                path.add((currentPos[0] - x, currentPos[1]))
            currentPos = (currentPos[0] - step, currentPos[1])
            # print(inputList[i], currentPos)
        elif 'U' in inputList[i]:
            for y in range(step):
                path.add((currentPos[0], currentPos[1] + y))
            currentPos = (currentPos[0], currentPos[1] + step)
            # print(inputList[i], currentPos)
        elif 'D' in inputList[i]:
            for y in range(step):
                path.add((currentPos[0], currentPos[1] - y))
            currentPos = (currentPos[0], currentPos[1] - step)
            # print(inputList[i], currentPos)

    return path


setL = (pather(L))
setL.remove((0, 0))
# print(setL)

setM = (pather(M))
setM.remove((0, 0))
# print(setM)

# with open("input/inputD3.txt", 'r') as f:
#     wires = [list(pather(line) for line in f.readline())]

intersection = setL & setM
intersection = set(setL).intersection(setM)
# print(intersection)
print("Part one:", min(abs(x)+abs(y) for (x, y) in intersection))
# print(2+min(sum(wire.index(intersect) for wire in wires) for intersect in intersection))
# for x, y in intersection:
#     test = abs(x)+abs(y)
#     if test < minimum:
#         if test == 0:
#             break
#         minimum = test
#         minX = x
#         minY = y
# print("Part 1:",minX, minY, abs(minX)+abs(minY))




# print(intersection)

