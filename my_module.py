
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
		print('Not OK')