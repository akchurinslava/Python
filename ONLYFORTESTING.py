from math import *
a=float(input('Please enter the number for A:'))
b=float(input('Please enter the number for B:'))
c=float(input('Please enter the number for C:'))
if a!=0:
	d=b*b-4*a*c
	if d<0:
		print('No solutions')
	elif d>0:
		x1=(-b+sqrt(d))/2*a
		x2=(-b-sqrt(d))/2*a
		print('x1='+str(round(x1,2))+' x2='+str(round(x2,2)))
	elif d==0:
		x3=-b/(2*a)
		print(str(round(x3,2)))
else:
	print("A can't be 0")

		
	
