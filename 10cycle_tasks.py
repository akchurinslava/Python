

#Task1
j=0
i=0
while True:
	i+=1
	a=float(input(f'{i} Enter A: '))
	if int(a)==a:
		j+=1
	if i==15: break
print(j)
#Task2
from math import *
c=int(input('Enter a number:'))
a=0
for x in range(1,c+1):
	a=x+a
print(a)
#Task3
x=1
z=1
for i in range(0,8,1):
	x =float(input('Enter a number:'))
	if x>0:
		z*= x
print(z)
#Task4
for i in range(10,20):
	print(i**2)	
#Task5
n=int(input('Enter quantity of N:'))
z=0
for i in range(0,n,1):
	x =float(input('Enter a number:'))
	if x<0:
		z+=x
print(z)
#Task6
n=int(input('Enter quantity of N:'))
z=0
q=0
y=0
l=0
for i in range(0,n,1):
	x =float(input('Enter a number:'))
	if x<0:
		q+=1
	elif x>0:
		y+=1
	else:
		x=0
		l+=1
print('The number of negativa',q)
print('The numbet of positive',y)
print('The number of zeros',l)
#Task7
z=int(input('Enter a multiplicity:'))
a=int(input('Enter a A:'))
b=int(input('Enter a B:'))
for i in range(a, b+1, 1):
	if i%z==0:
		print(int(i))
#Task8
for i in range(1, 20):
	i=float(i*2.5)
	print(str(i))
#Task9
n=int(input('Deposit:'))
s=int(input('Years:'))
z=0
for i in range(s*12):
	z=n*0.03/12
	n+=z
	output=n
print(output)
#task10
z=0
while z!=10:
	z+=1
	a,b=map(int,input(f'Pair{z}: ').split())
	if a==0 and b==0:break
	else:
		if a>b:
			print(a)
		elif a<b:
			print(b)
#task11
from random import *
y = 1
a=(randrange(1, 100))
for i in range(1, 100):
    if i%2 == 1:
        if i%a == 0:
            y *= i
print(y)
#task12
a=int(input('Enter number of lawn mowers:'))
b=int(input('Hours of first lawn mower worked:'))
c1=b*60
for i in range(1, a):
	c1+=10
print(c1)
#task13





















