

a=7
b=2
print(a+b)
print(a%b)
print(a**b)

a=4.5
b=2
print(a/b)
print(a//b)

'''
ddd
'''
a=''' aaa '''
print(a)

print("="*50)
print("My program")
print("="*50)
a="My program"
b=a[1]
print(b)
print(a[4]+"\n")
#read from backward. actually 0 and -0 is same
print(a[-1])
a="Life is too short, you need python"
print(a[0:4])
#[0:4] means 0 <= x < 4
print(a[0]+a[1]+a[2]+a[3])
print(a[19:])
print(a[:])

a="20010331Rainy"
data=a[0:7]
weather=a[8:]
print(data + "\t" + weather)

a="pithon"
#a[1]="y" --> this doesn't work
print(a)

print()
print(a[:1] + "y" +a[2:])

print("I eat %d apples" %3)
a="I eat %d apples" %3
print(a)

a="I have %s apples" %3
print(a)

a="Change is %d dollors" %3.21
print(a)

print("Error is %d%%" %98)

#sorting and spacing
print("%10s" %'hi')
print("%-3sjane" %'hi')
print("%0.4f" %3.4213233)

print("change is %0.2f dollors" %3.21)
print("%10.4f" %3.435123)

a="hobby"
print(a.count('b'))

print()
a="Python is best choice"
print(a.find('b'))
print(a.find('k'))
#returns if there is no character which is requested
print(a.index('t'))
a=","
a=a.join('abcd')
print(a)
a='hi'
print(a.upper())

a="dsfd   "
print(a.rstrip())

a="Life is too short"
print(a.replace("Life","Your leg"))

a="Life is too short"
print(a.split())
print(a.split(':'))

print()
a="a:b:c:d"
print(a.split(':'))

print("I eat {0} apples".format(3))

#print("I eat {1} apples".format(3,1)) --> too many argument for one string


print("I ate {number} apples. so I was sick for {day} days.".format(number=10,day=3))

print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))
print("{0:!>10}".format("hi"))

a=3.4213223
print("{0:!<10.4f}".format(a))
#print("{('so what?')}".format())--> error

print("{{so what}}".format())

print("{0:!^10}".format("hey"))


##LIST

a=[] #= a=list()
b=[1,2,3]
c=['Life','is','too','short']
d=[1,2,'Life','is']
e=[1,2,['Life','is']]
print(e)

a=[1,2,3]
print(a[0]*a[2])
print(a[-1])

a=[1,2,3,['a','b','c']]
print(a[3][0])

#Three - level indexing
a=[1,2,['a','b',['Life','is']]]
print(a[2][2][1])

a=[1,2,3,4,5]
print(a[0:2])
print(a[2:])

#Reiterated List
a=[1,2,3,['a','b','c'],4,5]
print(a[2:5])
print(a[3][2:])

a=[1,2,3]
b=[4,5,6]
print(a+b)

print(a*3)

#print(a[2]+"hi") --> type error
print(str(a[2])+"hi")

#replace value in list
a=[1,2,3]
a[2]=4
print(a)
print(a[1:2])
a[2]=['a','b','c']
print(a)

del a[1]
print(a)
a.append([4,5])
print(a)
a=[1,2,3]
print(a)
print(min(a))

a=['a','b','c']
print(a)
#print(a.reverse()) --> reverse function has return value as null
print(a.index('a'))

a.insert(0,4)
print(a)
a.insert(3,5)
print(a)

a.remove('a')
print(a)

a=[1,2,3]
a.pop()
print(a)

a=[1,2,3]
a.pop(1)
print(a)

a=[1,2,3,4,2,1,2]
print(a.count(2))

a.extend([1]) #--> add is not possible
print(a)


##Tuple

t1 = ()
t2 = (1,)
t3 = (1,2,3)
t4 = 1,2,3
t5 = ('a','b',('ab','cd'))

print(t1, t2, t3, t4 ,t5)

t1 = (1,2,'a','b')
#del t1[0] --> error
#t1[0] = 'c' --> error

print(t1[0], t1[3])
print(t1[1:])

t2=(3,4)
print(t1+t2)
print(t2*3)


#Dictionary

dic = {'name' : 'pey', 'phone' : '0119232313' , 'birth' : '1118'}
print(dic)

a = {1:'hi'}
a={'a' : [1,2,3]}


#appending

a={1:'a'}
a[2] ='b'
print(a)

a['name'] = 'pey'
a[3]=[1,2,3]
print(a)

del a[1]
print(a)


grade = {'pey':10, 'julliet':99}
print(grade['pey'])
print(grade['julliet'])

a = {'name' : 'pey', 'phone' : '01231243', 'birth' : '1118'}
print(a.keys())

for k in a.keys():
    print(k)
    
print(list(a.keys()))

print(a.values())

print(a.items())

a.clear()
print(a)

a={'name' : 'pey' , 'phone' : '01231234', 'birth' : '1118'}
print(a.get('name'))

print(a.get('foo','bar'))

print('name' in a)
print('email' in a)

s1=set([1,2,3])
print(s1)

s2 = set("Hello")
print(s2)

s1 = set([1,2,3])
l1 = list(s1)
print(l1)
print(l1[0])

t1 = tuple(s1)
print(t1[0])

s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

print(s1 & s2)
print(s1.intersection(s2))
print(s1 | s2)
print(s1.union(s2))

print(s1 - s2)
print(s1.difference(s2))

s1=set([1,2,3])
s1.add(4)
print(s1)

s1.update([4,5,6])
print(s1)

s1 = set([1,2,3])
s1.remove(2)
print(s1)


a=[1,2,3,4]
while a:
    print(a.pop())
    
a=3
print(type(a))
b=3
print(a is b)

import sys
print(sys.getrefcount(3))

a=3
print(sys.getrefcount(3))
b=3
print(sys.getrefcount(3))
c=3
print(sys.getrefcount(3))

a=[1,2,3]
from copy import copy
b = copy(a)
print(b is a)