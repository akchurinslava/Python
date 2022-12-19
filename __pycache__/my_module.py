
def Control(ik:str):
	"""
	Isikukood control number
	Must enter isikukood
	:param str ik: Human isikukood
	:rtype: var Not marked type

	"""
	ik_list=list(ik)
	s=0
	for i in range(0,10):
		s+=(i%9+1)*int(ik_list[i])
		print(f'{i%9+1}*{int(ik_list[i])}+', end="")
	print(s)
	s=s-(s//11)*11
	print(s)
	if s==int(ik_list[10]):
		answer=s
	else:
		answer='Control number is wrong'
	return vastus

def Medical(ik3:int):
	"""
	Medical 3 isikukood on number
	:param int ik3:
	:rtype: str medical center and place
	"""
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
def Gender(ik1:int)->str:
	if ik1%2==0:
		gender='woman'
	else:
		gender='man'











