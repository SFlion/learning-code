'''
Created on 2014-4-2
@author: SHENFENG
'''
#dictionary
d={"ad":"d",23:"3","2":25}
print "Hello World!"
print d["ad"]
print d[23]
print d["2"]
print d
d[23]=45
print d
del d["2"]
print d
d.clear()
print d


#list
li=["sds",23,'e3']
print li
print li[2]
print li[-2]
print li[0:2]
print li[0:-2]
li.append(34)
print li 
li.insert(3, 'df')
print li
li.extend([23,'df'])
print li
print li.index(23)
print 3 in li
print 23 in li
print li[0:0]
print li.pop()
print li*3
print li
print li+li
li+=li
print li

#tuple
t=(34,'df')
print t
pu={t:34}
print pu
tt=(li)
print tt
print li==tt

################

print range.__doc__
s=6
print "%d is a good number"%7
li=[23,4,"d34",'ds']
print [a*2 for a in li]
dd={23:'ffd','gtg':'f4'}
print dd.items()
print dd.keys()
print ["%s=%s"%(k,v) for k,v in dd.items()]
print ','.join(["%s=%s"%(k,v) for k,v in dd.items()])








