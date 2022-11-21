a=float(input())
b=float(input())
if a>0 and b>0: # or, not
	S=a*b
else:
	S="ei saa leida"
print("Pindala:", S)

#a,b,g=input('Insert number:').split() split dajot vozmownostj k perechisleniju

#v=input('here text') 
## if v.upper()=='YES'

mark=float(input('What mark you had at school:'))
if mark>=1 or mark<=5:
	if mark==1 and mark==2:
		answer='Bad'
	elif mark==3:
		answer='Not bad'
	elif mark==4:
		answer='Good'
	else:
		answer=='Pretty good'
else:
	answer='Data error'
print(answer)