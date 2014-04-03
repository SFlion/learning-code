'''
Created on 2014-4-3

@author: SHENFENG
'''

def connectstring(params):
    #params is a dictionary
    
    return ";".join(['%s=%s'%(k,v)for k,v in params.items()])
if __name__=="__main__":
    myparams={"sd":23,"d2":"3sd"
             }
    print connectstring(myparams)

    

    