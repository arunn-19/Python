'''mssg='hello'
index=0
for i in mssg:
    print(i)
    index+=1'''

'''a='hello welcome to python'
i=2
print(a[2:8:2]) '''

'''a=str('hello')
b=str('welcome to python')
print(a+','+b)
print(a+b)'''

'''a='hello and welcome to python'
print(a.capitalize())
b='el'
print(a.count(b,0,len(a)))
print(a.endswith('on',0,len(a)))'''

'''a='BoNd007'
b='007'
c='abcd'
print(b.isalnum())
print(c.isalpha())
print(a.swapcase())
print(a.replace('B','b'))'''

'''a='welcome to python'
b='t'
print(a.startswith('t',0,len(a)))
print(a.endswith('t',0,len(a)))
print(a.count('t',0,len(a)))
if b in a:
    print('found')
else:
    print('not found')'''

#ASCII A-Z=65-90   and    a-z=97-122   

'''a='welcome to python'
for i in a:
    print(i,end=' ')'''

'''a='welcome to python'
i=0
while i<len(a):
    print(a[i], end='\t ')
    i+=1'''

'''for i in range(1,7):
    ch='A'
    print()
    for j in range(1,i+1):
        print(ch,end=' ')
        ch=chr(ord(ch)+1)'''

'''a='welcome to python world'
b='a,e,i,o,u,A,E,I,O,U'
for i in a:
    if i in b:
        pass
    else:
        print(i,end=' ')'''

'''a='welcome to python'
b='e'
for i in a:
    if i in a:
        print('yes it has vowels',a.count(b,0,len(a)),end=' \t')
    else:
        print("no, don't have vowel")'''

'''a='hello python'
i=0
while i <=len(a):
    print(a[i])
    i+=1'''

'''a='hello python'
print(a.isupper())
print(a.upper())'''

'''a=('1,32,2,13')
print(a.split(','))'''

v=['a','e','i','o','u','A','E','I','O','U']
a=('the world is beautiful')
b=''
for i in range(len(a)):
    if a[i] not in v:
        print(b+a[i],end='')
    

