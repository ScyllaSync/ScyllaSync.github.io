#ask user to enter maximum value to find prime number start from 2
from time import process_time


max_value=int(input('Enter maximum prime number:'))
value= 2
while value <= max_value:
    is_prime = True
    trial_factor=2
    while trial_factor<value:
        if value%trial_factor==0:
            is_prime=False
            break
        trial_factor+=1
    if is_prime:
        print(value,end=' ')
    value+=1
print()
