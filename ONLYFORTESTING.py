from untitled import *
from datetime import *
while True:
	ik=input('Isikukood:')
	if len(ik)==11:
		try:
			ikl=list(ik)
			if int(ikl[0]) in [1,2,3,4,5,6]:
				if int(ikl[0]) in [1,2]:
					a=1800
				elif int(ikl[0]) in [3,4]:
					a=1900
				else:
					a=2000
				year=int(ikl[1]+ikl[2])
				month=int(ikl[3]+ikl[4])
				day=int(ikl[5]+ikl[6])
				if datetime(year,month,day):
					answer=Control(ik)
					if type(answer)==int:
						ik3=int(ik[7:10])
						medical=Medical(ik3)
						print(medical)
						gender=Gender(int(ik[0]))
						print(gender)
					else:
						print(answer)

			else:
				print('First number is wrong')
		except:
			print('Data is wrong, must insert numbers')
	else:
		print('Isikukood must be 11 symbols')








