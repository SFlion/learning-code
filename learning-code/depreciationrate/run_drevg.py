#run the depreciationrate_evaluate_volume_grade in loop mode
from numpy import *
from depreciationrate_evaluate_volume_grade import DepreciationRate as dr

a=linspace(2.0,2.5,40)
for i in range(0,40):
    b=dr(frac=a[i])
    print 'frac=%.2f:'%a[i],b
