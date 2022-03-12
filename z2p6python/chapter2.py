from tkinter.font import names
from turtle import right


counter=100
miles=1000.0
name='John'
print(counter,miles,name)
print(type(counter))
print(type(miles))
print(type(name))

#multiple assignment
a=b=c=1
print(a,b,c)
a,b,c=1,2,3
print(a,b,c)
str='Hello World'
print(str)
print(str[0])
print(str[2:5])
print(str[2:])
print(str*2)
print(str + "Test")

#list example
list = [ 'abcd',786,2.23,'john,70.2']
tinylist = [123,'john']
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist * 2)
print( list + tinylist)

#Tuples elements cammnot update as list
tuple = ('abcd',786,2.23,'john',70.2)
tinytuples = (123,'Yan')
print(tuple)
print(tuple[0])
print(tuple[1:4])
print(tinytuples * 2)
print(tuple + tinytuples)

#dictionary
dict = { 'one':'This is one'}
print(dict['one'])
dict[2]="This is two"
print(dict[2])
dict2 = {'name':"Mg Mg",'age':23,'city':"Yangon"}
print(dict2)
print(dict2['name'],dict2['age'])
