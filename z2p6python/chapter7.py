import sys
'''
filename=sys.argv[0]
username=sys.argv[1]
userage=sys.argv[2]
usercity=sys.argv[3]
print('arg 0 is ',filename)
print('arg 1 is ',username)
print('arg 2 is ',userage)
print('arg 3 is ',usercity)

C = float(sys.argv[1])
F = 9.0 * C / 5 + 32
print(C , 'C is ', F ,'F')


# eval
s = '10-2'
print(s)
print(eval(s))
print(eval('[1,4,5,6]+[2,3]'))
print(eval('"hello "* 5'))

statement= 'r = 2 + 2'
exec(statement)
print('Value of r :',r)
'''
formula = input('Write a formula with x :')
code="""def f(x) :
    return %s
"""% formula
from math import*
exec(code)

x=int(input('Enter x value :'))
y=f(x)
print('f(%g)=%g'%(x,y))