from math import *
from random import *

while True:
	a=input('Enter your name:')
	if a.isalpha():
		list(a)
		break
c=str.capitalize(a)
print('Hello ' + c +' !')
b=len(a)
print('Your name content '+str(b)+' letters')
vowel=0
consonants=0
all_vowel=['a','e','i','o','u']
for i in a:
	if i in all_vowel:
		vowel+=1
	else:
		consonants+=1
q=sorted(list(a),key=str)
print(q)

