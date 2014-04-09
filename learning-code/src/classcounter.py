'''
Created on 2014-4-9

@author: SHENFENG
'''

class Counter:
    '''
    classdocs
    '''
    count=0

    def __init__(self):
        self.__class__.count +=1
        
print Counter
print Counter.count
g=Counter()
print g.count
f=Counter()
print f.count
