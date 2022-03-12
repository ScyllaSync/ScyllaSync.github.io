#If statement
var1=100
if var1:
    print('100 is true expression')
    print(var1)
print('End')       

var2=int(input('Enter a number:'))
if var2%2:
    print(var2, 'is odd')
else:
    print(var2, 'is even')
print('Bye')

#Nested if statement
var3=100
if var3<200:
    print(var3,'is less than 200')
    if var3 == 150:
        print('which is 150')
    elif var3==100:
        print(var3,'which is 100')
    elif var3==50:
        print(var3,'which is 50')
    elif var3<50:
        print(var3,'less than 50')
else:
    print(var3,'is greater than or equal 200')
print('bye')                

#Check divisor not to be zero
divident=int(input('Enter divident'))
divisor=int(input('Enter divisor'))

#if divisor is zero or not
if divisor!=0:
    quotitent=divident/divisor
    print(divident,'/',divisor,'=',quotitent)
print('end')



