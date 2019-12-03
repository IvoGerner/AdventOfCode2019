f = open("input/inputD3.txt", 'r')

L = f.readline().split(",")
M = f.readline().split(",")

# dictionary, store all positions. Go by min and max where intersections are.
# tupels
#

def pather(inputList):
    distance = [0, 0] #(x, y)
    for i in range(len(inputList)):
        if 'R' in inputList[i]:
            distance[0] += int(''.join(x for x in inputList[i] if x.isdigit()))
        elif 'L' in inputList[i]:
            distance[0] -= int(''.join(x for x in inputList[i] if x.isdigit()))
        elif 'U' in inputList[i]:
            distance[1] += int(''.join(x for x in inputList[i] if x.isdigit()))
        elif 'D' in inputList[i]:
            distance[1] -= int(''.join(x for x in inputList[i] if x.isdigit()))

    return distance

print(pather(L))

print(pather(M))




