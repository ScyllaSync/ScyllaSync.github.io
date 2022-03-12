from pyexpat.errors import messages


mylist=[2,4,6,8,9]
print(mylist)
print(mylist.index(2))
mylist.append(12)
print(mylist)
mylist.insert(3,5)
print(mylist)

def sayHi(message='Thant'):
    print('Hi',message)
sayHi('Tkss')
sayHi()

def F(C):
    return (9.0/5) * C + 32

fdegree = F(45)
print(fdegree)

# y(t) = v0t + 1/2gt**2

def y(t,v0):
    g = 9.81
    return v0 * t + 0.5 * g * t ** 2
y1 = y (12 , 35)
print(y1)