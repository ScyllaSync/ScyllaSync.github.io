#1 read lines
from cgitb import text


infile=open('data.txt','r')
'''
list=infile.readlines()
print(list)
infile.readline()
infile.readline()
infile.readline()
print(infile.readline())

'''
text=infile.read()
print(text)

infile.close()
