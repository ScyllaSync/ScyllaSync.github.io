# ask user to use y or n to increase count and print
count=0
entry='Y'
while entry!='N' and entry!='n':
    print(count)
    entry=input('Please enter Y to continue or N to quit :')
    if entry=='Y' or entry=='y':
        count=count +1
    elif entry !='N' or entry !='n':
        print('"',entry,'"is invalid answer!')
print('Exit programmm')
