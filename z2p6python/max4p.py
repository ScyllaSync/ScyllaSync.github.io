print('Enter 4 numbers to compare')
num1=int(input('Enter 1st number:'))
num2=int(input('Enyter 2nd number:'))
num3=int(input('Enter 3rd nnumber:'))
num4=int(input('Enter 4th number:'))

max=num1
if num2>max:
    max=num2
if num3>max:
    max=num3
if num4>max:
    max=num4
print('Maximun number is :',max)