num1=int(input('Enter 1st number:'))
num2=int(input('Enter 2nd number:'))
num3=int(input('Enter 3rd number:'))
num4=int(input('Enter 4th number:'))
num5=int(input('Enter 5th number:'))

max_num=num1
min_num=num1
if num2>max_num:
    max_num=num2
if num3>max_num:
    max_num=num3
if num4>max_num:
    max_num=num4
if num5>max_num:
    max_num=num5


if num2<min_num:
    min_num=num2
if num3<min_num:
    min_num=num3
if num4<min_num:
    min_num=num4
if num5<min_num:
    min_num=num5
print('Maximum number is ',max_num)
print('Minimum number is ',min_num)
