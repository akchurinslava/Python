from math import *
from random import *

a=input('Please choose your level[easy, normal, hard]:')



if a.lower() == 'easy':
    print('So you chose a newbie level')
    print('It is better to start than not to start at all')
    input('Please press enter to continue...')
    c1=0
    c2=0
    for i in range(5):
        n1=randint(1, 100)
        n2=randint(1, 100)
        a1=int(input(str(n1)+'+'+str(n2)+'='))
        check=n1+n2
        if check==a1:
            c1+=1
        else:
            check!=a1
            c2+=1
            