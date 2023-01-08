from math import *
from random import *
text=''
for i in range(1, 11):
	a1=randint(-100,100)
	a2=randint(-100,100)
	if a1>a2:
		print(f'{a1} is bigger then {a2}')
	elif a2>a1:
		print(f'{a2} is bigger then {a1}')
	else:
		print(f'{a1} and {a2} are equal')
print(text)