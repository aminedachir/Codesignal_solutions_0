def makeArrayConsecutive2(statues):
    a, c = min(statues), 0
    for i in range(100):
        if (a+1 != statues[i]):
            c = c+1
    return c