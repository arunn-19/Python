'''d={}
#print(type(d))

d={'harry':'burger','rohan':'rotti'}
#print(d)
#print(d['harry'])

d={'harry':'rice','rohan':'dal'}
d['manny']= 'chicken'
print(d) '''

'''d={'Roll':'23','Name':'ABC','Course':'Btech CSE'}
print(d)'''

'''print(dict([('Rollno','23'),('Name','ABC'),('Course','BTech CSE')]))'''

'''d={x:x*2 for  x in range(1,10)}
print(d)'''

d={'Roll':'23','Name':'ABC','Course':'Btech CSE'}
print(d)
print(d['Name'])
print(d['Roll'])
print(d['Course'])
d2={'Marks':'89'}
d.update(d2)
print(d)
d['Marks']=89
print(d['Marks'])
d['Course']='BBA'
print(d['Course'])

'''d={'Roll':'23','Name':'ABC','Course':'Btech CSE'}
print(sorted(d.keys()))
print(sorted(d.values()))'''
