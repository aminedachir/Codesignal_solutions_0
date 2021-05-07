def makeArrayConsecutive2(statues):
    a = min(statues)
    c = 0
    for i in range(100):
        if (a+1 != statues[i]):
            c = c+1