Vjatseslav_uslovnqj_operator
#NR 1
a=float(input('Insert number:'))
if a>0:
	if a%2==0:
			print(f'{a} is great number')
	else:
		print(f'{a} is not great number')
else:
	print('Does not work')

#NR2

a=float(input('Number1 :'))
b=float(input('Number2 :'))
c=float(input('Number3 :'))
if a>0 and b>0 and c>0:
	if a+b+c==180:
		if a==b==c==60:
			print('Ravnostoronnij')
		elif a==b or b==c or a==c:
			print('Ravnobedrennqj')
		else:
			print('Raznostoronnij')
	else:
		print('Not treugolnik')
else:
	print('not correct')

#NR3
d=input('Do you want decoding [Yes or No]:')
if d.upper()=="YES":
	number=int(input('Choose number from 1 to 7:'))
	if number==1:
		day="Monday"
	elif number==2:
		day="Tuesday"
	elif number==3:
		day="Wednesday"
	elif number==4:
		day="Thursday"
	elif number==5:
		day="Friday"
	elif number==6:
		day="Saturday"
	elif number==7:
		day="Sunday"

	print(str(number)+ f' is {day}')
else:
	print(str('bye'))


#NR4

a,b=input(int('Insert day and month:'))
	if a>21 and a>31 and b==03 or (a>0 and a>=20 and b==04)
	sign="Baran"


















