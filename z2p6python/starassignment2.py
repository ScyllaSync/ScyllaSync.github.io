height=int(input('Enter tree height: '))
row = 0
while row < height:
    count = 0
    while count <= row:
        print(end='*')
        count +=1
    print()
    row+=1
'''
i = 1
while i < length:
    j = length
    while j > i:
        print(end='*')
        j-=1
    print()
    i+=1
'''
row=1
while row <height:
    count = 0
    while count < height-row:
        print(end='*')
        count+=1
    print()
    row+=1