'''
Created on 2014-4-9

@author: SHENFENG
'''

class MyClass:
    '''
    a test for class
    '''
    def __init__(self):
        self.data={}
    def clear(self): self.data.clear()
    def keys(self):return self.data.keys()
    
class YourClass(MyClass):     
    def __init__(self,name):
        MyClass.__init__(self) 
        self["name"]=name 
    def clear(self):
        MyClass.clear(self)
k=YourClass("Best")
print k

        