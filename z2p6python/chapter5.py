#while loop

count=0
while count<9:
    print('Count value is',count)
    count=count+1
else:
    print(count,'Count is greater than or equal to 9')
print('end')

ans='y'
while ans=='y':
    number=int(input('Enter a number to check even or odd:'))
    if number%2:
        print(number,'is odd')
    else:
        print(number,'is even')    
    ans=input('Wanna try again? y or n :')
