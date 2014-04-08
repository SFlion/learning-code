
def info(obj,spacing=10,collapse=1):
    
    methodlist=[e for e in dir(obj) if callable(getattr(obj,e))]
    processfunc=collapse and (lambda s: " ".join(s.split())) or (lambda x:x)
    print "\n".join(["%s %s" %(e.ljust(spacing), 
                               processfunc(str(getattr(obj,e).__doc__))) 
                               for e in methodlist])
if  __name__=="__main__":
    print info.__doc__
