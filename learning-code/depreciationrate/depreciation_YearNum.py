'''从数据库中 open_by_year_volume 取折旧率的数据，处理。
折旧率数据的大致年份分布，即判断多数数据是哪年以后。'''

import os,sys,string
import MySQLdb
from numpy import *
import matplotlib
import matplotlib.pyplot as plt

try:
    conn=MySQLdb.connect(host="192.168.1.96",user="zhangzupeng",
                         passwd="zhangzupeng",db="pingjia",charset="utf8")
except Exception,error:
    print error
    sys.exit()
    
cursor=conn.cursor()
sql='''select count(year) from open_by_year_volume where
depreciation_rate is not null'''
cursor.execute(sql)
data=cursor.fetchone()
result0=data[0]

result=zeros((8,1))
i=0
for year in range(2008,2000,-1):
    cursor=conn.cursor()
    sql='''select count(year) from open_by_year_volume where
    depreciation_rate is not null and year> %s'''
    cursor.execute(sql,year)
    data=cursor.fetchone()
    result[i]=data[0]
    i+=1
print result0
print result
x=range(2001,2009)
plt.axis([2001,2009,0.6,1])
plt.plot(x,result/result0,'*')
plt.show()

