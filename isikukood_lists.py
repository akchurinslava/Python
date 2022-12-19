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
					s=0
					for i in range(0,10):
						s+=(i%9+1)*int(ikl[i])
						print(f'{i%9+1}*{int(ikl[i])}+', end="")
					print(s)
					s=s-(s//11)*11
					print(s)
				if int(ikl[0]) in [1,3,5]:
					print('Man')
				else:
					int(ikl[0]) in [2,4,6]
					print('Woman')
				ik3=int(ik[7:10])
				if ik3>1 and ik3<=10:
					mcenter='Kuressaare'
				elif ik3>11 and ik3<=19:
					mcenter='Tartu'
				elif ik3>21 and ik3<=220:
					mcenter='Ida-Tallinna'
				elif ik3>=221 and ik3<=270:
					mcenter='Ida-Viru'
				elif ik3>=271 and ik3<=370:
					mcenter='Maarjamoisa'
				elif ik3>=371 and ik3<=420:
					mcenter='Narva'
				elif ik3>=421 and ik3<=470:
					mceneter='Parnu'
				elif ik3>=471 and ik3<=490:
					mcenter='Pelgulinna'
				elif ik3>=491 and ik3<=520:
					mcenter='Jarvamaa'
				elif ik3>=521 and ik3<=570:
					mcenter='Rakvere'
				elif ik3>=571 and ik3<=600:
					mcenter='Valga'
				elif ik3>=601 and ik3<=650:
					mcenter='Viljandi'
				else:
					ik3>=651 and ik3<=700
					mcenter='Louna-Eesti'
				print(mcenter)
			else:
				print('First number is wrong')
		except:
			print('Data is wrong, must insert numbers')
	else:
		print('Isikukood must be 11 symbols')
