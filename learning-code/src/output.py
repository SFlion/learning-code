'''
Created on 2014-4-8

@author: SHENFENG
'''
import statsout

def output(data,form="text"):
    output_function=getattr(statsout,
                            "statsout_%s"%form,statsout.statsout_text)
    return output_function(data)

