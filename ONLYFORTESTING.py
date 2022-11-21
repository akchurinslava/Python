number=float(input("Insert numnber"))
if number. isalpha():
	print('This is text')
elif number. isdigit():
	number=float(number)
	if number>0:
		if number%2==0:
			print(f'{number} is great number')
		else:
			print(f'{number} not great number')
	else:
		print(f'{number} does not exits')
else:
	print(f'{number} unreal number')