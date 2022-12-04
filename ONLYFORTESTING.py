a=int(input('Enter number of lawn mowers:'))
b=int(input('Hours of first lawn mower worked:'))
c1=b*60
for i in range(1, a):
	c1+=10
print(c1)