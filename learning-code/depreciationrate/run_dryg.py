#run the depreciationrate_evaluate_volume_grade in loop mode
import sys
import MySQLdb
#from numpy import *
'random.rand(4)生成四个小于1的小数'
import random as rd
'rd.randrange(0,12)生0到12之间的一个整数,或者rd.randint(0,12)'
from depreciationrate_yeargap import DepreRateYearGap as dy
#import matplotlib
import matplotlib.pyplot as plt


try:
    conn=MySQLdb.connect(host="192.168.1.96",user="zhangzupeng",
                         passwd="zhangzupeng",db="pingjia",charset="utf8")
except Exception,error:
    print error
    sys.exit()
    
cursor=conn.cursor()
sql='select slug from open_category where id<147'
cursor.execute(sql)
alldata=cursor.fetchall()
cursor.close
n=len(alldata)
col=['-ro','-go','-bo','-yo']
for i in range (0,n):
    dy(alldata[i][0],100,col[rd.randint(0,3)])
plt.show()

