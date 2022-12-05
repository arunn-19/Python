'''i=0
while(True):
    print(i, end=' ')
    i+=1'''

'''i=0
while (True):
    print(i, end=' ')
    if i==25:
        break #stop the loop
    i+=1'''

'''i=0
while (True):
    if i<8:
        i+=1
        print(i, end='')
    continue
    print(i, end=' ')
    if i==25:
        break #stop the loop
    i+=1'''

'''i=10
while (True):
    if i<5:
        i+=1
        print(i, end='')
        continue
    print(i, end=' ')
    if i==25:
        break #stop the loop
    i+=1'''

a=int(input())
i=0
while (True):
    if a<100:
        print(a, end=' ')
        a+=1
        continue
    if a>100:
        print('Error')
        break
    


