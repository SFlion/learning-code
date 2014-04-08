'''
Created on 2014-4-8

@author: SHENFENG
'''

def output(data,form="text"):
    output_function=getattr(statsout,"statsout_%s"%form)
    return output_function(data)

