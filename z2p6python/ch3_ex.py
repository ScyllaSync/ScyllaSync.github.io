# Division 
print('Enter two numbers to divide:')
divident=int(input('Enter divident:'))
divisor=int(input('Enter divisor:'))
result=divident/divisor
print(divident,'/',divisor,'=',result)

#Half
value=int(input('Enter a number to split:'))
result=value/2
print('Half of the number is ',result)

#temperatur conversion
# C = 5/9 * (F - 32)
degreeF=float(input('Enter F degrees:'))
#Business logic
degreeC=5/9 * (degreeF - 32)
#output
print( degreeF,'degree F =',degreeC,'degree C.')

#Timeconversion
seconds=int(input('Please enter seconds:'))
hour=seconds//3600
seconds=seconds%3600
minutes=seconds//60
seconds=seconds%60
print(hour,'hour:',minutes,'minitues:',seconds,'seconds')
