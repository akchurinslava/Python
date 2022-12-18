from math import *
from random import *


list1=['fdsfdsfs', 'dsgdbevdfv', 'gdfgdfccsd']
list2=['fdsapwqesfs', 'dsvdfv', 'dfccsd']
list3=['fdss', 'dvdfv', 'gmnbnvbfccsd']
max1 = len(max(list1, key = len))
max2 = len(max(list2, key = len))
max3 = len(max(list3, key = len))


print([(max1 - len(x))*'_' + x for x in list1])
print([(max2 - len(x))*'_' + x for x in list2])
print([(max3 - len(x))*'_' + x for x in list3])



