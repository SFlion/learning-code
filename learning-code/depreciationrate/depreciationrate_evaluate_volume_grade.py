# This Python file uses the following encoding: utf-8
'from depreciationrate_evaluate_volume_grade import DepreciationRate as dr'

import os,sys,string
import MySQLdb
from numpy import *
import matplotlib
import matplotlib.pyplot as plt

dz=[0.0535, 0.0138, 0.09432143, 0.106125, nan]

def DepreciationRate(brand='dazhong',frac=2.31):
    try:
        conn=MySQLdb.connect(host="192.168.1.96",user="zhangzupeng",
                             passwd="zhangzupeng",db="pingjia",charset="utf8")
    except Exception,error:
        print error
        sys.exit()
    x0=arange(2010,2014)
    y0=zeros((4,))
    add0=0
    addv=0
    mark0=0
    for ye in range(2010,2014):
        cursor=conn.cursor()
        sql='''select a.depreciation_rate,a.volume,b.gradevalue from open_by_year_volume
        as a inner join dazhong_category as b on a.model_slug=b.brand_slug where a.year=%d
        and a.depreciation_rate is not null and a.depreciation_rate<1 and a.brand_slug='%s'
        and (a.volume=2 or a.volume=3) and a.units>%d'''%(ye,brand,100)
        cursor.execute(sql)
        alldata=cursor.fetchall()
        cursor.close()
        n=len(alldata)
        d_temp=zeros((n,))
        v_temp=zeros((n,))
        g_temp=zeros((n,))
        for i in range(0,n):
            d_temp[i]=alldata[i][0]
            v_temp[i]=alldata[i][1]
            g_temp[i]=alldata[i][2]
            avg=average(d_temp)
        y0[ye-2010]=avg
        if y0[ye-2010]>0:
            mark0+=n 
            for i in range(0,n):
                add0=add0+sqrt((d_temp[i]-y0[ye-2010])**2)/y0[ye-2010]
                addv=addv+sqrt((d_temp[i]-(y0[ye-2010]+g_temp[i]/50+(\
                (frac-v_temp[i])/10)*(dz[ye-2010]/dz[3])))**2)/(y0[ye-2010]\
                +g_temp[i]/50+((frac-v_temp[i])/10)*(dz[ye-2010]/dz[3]))                    
    if mark0>0:
        add0=add0/mark0
        addv=addv/mark0
       
    #for i in range(2010,2015):
    #    print x0[i-2010],y0[i-2010]

    x1=arange(2010,2014)
    y1=zeros((4,))
    add1=0
    mark1=0
    for ye in range(2010,2014):
        cursor=conn.cursor()
        sql='''select depreciation_rate,volume from open_by_year_volume where year=%d
        and depreciation_rate is not null and depreciation_rate<1 and brand_slug='%s'
        and volume=2 and units>%d'''%(ye,brand,100)
        cursor.execute(sql)
        alldata=cursor.fetchall()
        cursor.close()
        n=len(alldata)
        d_temp=zeros((n,))
        v_temp=zeros((n,))
        for i in range(0,n):
            d_temp[i]=alldata[i][0]
            v_temp[i]=alldata[i][1]
        avg=average(d_temp)
        y1[ye-2010]=avg
        if y1[ye-2010]>0:
            mark1+=n
            for i in range(0,n):
                add1=add1+sqrt((d_temp[i]-y1[ye-2010])**2)/y1[ye-2010]
    if mark1>0:
        add1=add1/mark1

    x2=arange(2010,2014)
    y2=zeros((4,))
    add2=0
    mark2=0
    for ye in range(2010,2014):
        cursor=conn.cursor()
        sql='''select depreciation_rate,volume from open_by_year_volume where year=%d
        and depreciation_rate is not null and depreciation_rate<1 and brand_slug='%s'
        and volume=3 and units>%d'''%(ye,brand,100)
        cursor.execute(sql)
        alldata=cursor.fetchall()
        cursor.close()
        n=len(alldata)
        d_temp=zeros((n,))
        v_temp=zeros((n,))
        for i in range(0,n):
            d_temp[i]=alldata[i][0]
            v_temp[i]=alldata[i][1]
        avg=average(d_temp)
        y2[ye-2010]=avg
        if y2[ye-2010]>0:
            mark2+=n
            for i in range(0,n):
                add2=add2+sqrt((d_temp[i]-y2[ye-2010])**2)/y2[ye-2010]
    if mark2>0:
        add2=add2/mark2


    #print 'original accuracy rate0:',1-add0
    #print 'original accuracy rate1:',1-add1
    #print 'original accuracy rate2:',1-add2
    #print 'volume accuracy rate:',1-addv

    cursor=conn.cursor()
    sql='''select year,depreciation_rate from open_by_year_volume where
    depreciation_rate is not null and depreciation_rate<1 and brand_slug='%s'
    and (volume=2 or volume=3) and units>%d'''%(brand,100)
    cursor.execute(sql)
    alldata=cursor.fetchall()
    cursor.close()
    conn.close()
    
    n=len(alldata)
    x=zeros((n,))
    y=zeros((n,))
    for i in range(0,n):
        x[i]=alldata[i][0]
        y[i]=alldata[i][1]
    #print "Sample Num：",n
    
    plt.plot(x,y,'.',x0,y0,'ro',x1,y1,'bo',x2,y2,'go')
    plt.axis([1990,2015,0,1])
    plt.xlabel('Year')
    plt.ylabel('Depreciation_rate')
    plt.title('Depreciation_rate by Year of dazhong')
    plt.text(1991, 0.8, "samples choosen by 'units>100'")
    #plt.show()

    return 1-addv

if __name__ == "__main__":
    DepreciationRate()
