#enter positive numbers to add, 999 to exit, skip negaative numbers
sum=0
done=False
while not done:
    val=int(input('Enter a number to add 999 to quit:'))
    if val<0:
        print('Negative numbers',val,'ignored')
        continue
    if val!=999:
        print('Tallying',val)
        sum += val
    else:
        done=(val==999)
print('Sum is',sum)