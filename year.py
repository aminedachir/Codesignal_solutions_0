def centuryFromYear(year):
    a = 1
    b = 100
    c = b/100
    for i in range(20):
        if(a<=int(year)<=b):
            return (int(c))
        a = a + 100
        b = b + 100
        c = b/100