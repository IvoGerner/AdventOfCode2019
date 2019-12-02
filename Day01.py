import math

def refuel(mass):
    fuel = math.floor(mass/3)-2
    if fuel <= 0:
        fuel = 0
    return fuel

L = [116860, 130144, 79347, 120725, 137692, 139037, 72089, 133224, 102168, 100679, 122298, 132969, 109196, 85162, 66316, 68461, 87608, 108091, 71061, 85477, 97748, 105766, 141169, 94553,
     98932, 134376, 69822, 104858, 102584, 59682, 52092, 105784, 144100, 83695, 130436, 105447, 133102, 82770, 68684, 103878, 136774, 71462, 96828, 74743, 127523, 124145, 148013, 103862,
     80052, 74095, 130394, 125589, 137576, 111299, 69311, 63144, 119014, 136084, 94348, 109511, 102493, 117791, 76202, 138442, 72724, 104579, 80285, 56847, 145460, 132255, 58264, 60460,
     98995, 63343, 51207, 133619, 126155, 130707, 105010, 104589, 128527, 67715, 71823, 82517, 74115, 135483, 82230, 127410, 128969, 140127, 59133, 145973, 109430, 103608, 113203, 133402,
     123971, 71761, 114178, 52940]

total = 0
for i in L:
    input = i
    oldInput = 0
    while (input != oldInput):
        oldInput = input
        input = refuel(input)
        total += input


print(total)