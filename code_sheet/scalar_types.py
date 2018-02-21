x = "apples"
y = "lemons"
z = "In the basket are %s & %s" % (x,y)
print(z)
#String Formatting with the % Operator
print('hello {}'.format('world'))
print('{} {}'.format('hello', 'world'))
print('{1} {0}'.format('world', 'hello'))
print('{first} {second}'.format(first='hello', second='world'))
#import and find path

import sys
print(sys.path)
