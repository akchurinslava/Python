from math import *
from random import *


list1=['fdsfdsfs', 'dsgevdfv', 'gdfgdfccsd']
list2=['fdsapwqesfs', 'dsvdfv', 'dfccsd']
list3=['fdss', 'dvdfv', 'gmnbnvbfccsd']

print([x.ljust(len(max(list1, key = len)), '_') for x in list1])
print([x.ljust(len(max(list2, key = len)), '_') for x in list2])
print([x.ljust(len(max(list3, key = len)), '_') for x in list3])

