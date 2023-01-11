#1
from my_module2 import *
a=arithmetic(2.5,1.8,"+")
print(a)
while True:
    a=arithmetic(input(),input(),input())
    print(a)

#2
from my_module2 import *

a=is_year_leap(int(input()))
print(a)

#3
from my_module2 import *
from math import *

a=square(input())
print(a)

#4
from my_module2 import *

a=season(input())
print(a)

#5
from my_module2 import *

a=bank(input(), input())
print(a)

#6
from my_module2 import *

a=is_prime(input())
print(a)

#7
from my_module2 import *
a=date(input(),input(),input())
if a!=None:
    print(a)


#8
from my_module2 import *

a=XOR_cipher(input(), special_key(input()))
print(a)

b=XOR_uncipcher(input(), special_key(input()))
print(b)