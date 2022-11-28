

# Task 1
from math import *
for i in range(1,16,1):
	a=float(input(f'{i} Enter A: '))
	if int(a)==a:
		j+=1
print(j)

from math import *
for i in range(0,15,1):
	a=float(input(f'{i+1} Enter A: '))
	if int(a)==a:
		j+=1
print(j)

j=0
i=0
while True:
	i+=1
	a=float(input(f'{i} Enter A: '))
	if int(a)==a:
		j+=1
	if i==15: break
print(j)


j=0
i=0
while i==15:
	i+=1
	a=float(input(f'{i} Enter A: '))
	if int(a)==a:
		j+=1
print(j)

