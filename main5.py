n = input('enter nmuber for area :')
def shapearea(n):
	b = int(n)
	c = b-1
	d = b*2
	for i in range(100):
		a = c*d+1
		print(a)

shapearea(n)