year = 105
def centuryFromYear(year):
    if (year<=100):
        print("1")
    elif (year%100):
        print(int(year/100)+1)
    else:
        print(year/100)



centuryFromYear(year)