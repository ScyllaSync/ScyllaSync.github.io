#function
import sys
sum=0
while True:
    val=int(input('Enter number(999 to exit)'))
    if val == 999:
        sys.exit(0)
    sum+=val
    print('Sum is : ',sum)
