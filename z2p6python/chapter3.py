#Arithemetic operator
from ast import Not
from operator import truediv
from re import I, T


num1=int(input('Enter 1st number:'))
num2=int(input('Enter 2nd number:'))
num3=num1 + num2 #add
num4=num1 - num2 #sub
num5=num1 * num2 #mul
num6=num1 / num2 #div
num7=num1 % num2 #modulus
num8=num1 // num2 #floor division
num9=num1 ** num2 #exponent
print(num1,num2,num3,num4,num4,num5,num6,num7,num8,num9)

#Comparision operator ==,<>,!=,>=,<=,<,>
if num1 == num2 :
    print('%s is equal to %s' %(num1,num2))

if num1 != num2 :
    print('%s is not equal to %s' %(num1,num2))

if num1>num1:
    print('%s is greater than %s' %(num1,num2))

if num1<num2:
    print(('%s is less than %s' %(num1,num2)))

if num1>=num1:
    print('%s is greater than or equal %s' %(num1,num2))

if num1<=num1:
    print('%s is less than or equal %s' %(num1,num2))

# Assignment operator =,+=, -=, *=, /=,%=,**=,//=
num10 = num1 + num2
num10 += num2
num10 -= num2
num10 *= num2
print('Num 10 is %s' %(num10))


a=60
print(a>>2)
#1009 => 9
#1100 => 12
#& 1000 =>8
#| 1101 => 13
#^ 0101 => 5
#~ 0110 => -10
#~ 0011 => -13
a=9
b=12
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(~b)

#logical operator
if True and True:
    print('ok')
print(True and False)
print(False or True)
print(not(True))
print(type(True))