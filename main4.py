inputArray = input('enter array :')
def adjacentElementsProduct(inputArray):
    return max(i nputArray[i] * inputArray[i+1] \
    	for i in range(len(inputArray)-1))

adjacentElementsProduct(inputArray)
