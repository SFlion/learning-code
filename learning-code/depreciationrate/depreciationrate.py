# This Python file uses the following encoding: utf-8

#import sys
import MySQLdb
from numpy import *
#import matplotlib
import matplotlib.pyplot as plt

def DepreciationRateall():
    try:
        conn=MySQLdb.connect(host="192.168.1.245",user="zhangzupeng",
                             passwd="zhangzupeng",db="pingjia",charset="utf8")
    except Exception,error:
        print error
        sys.exit()
    x0=arange(1990,2015)
    y0=zeros((25,))
    add0=0
    mark=0
    for ye in range(1990,2015):
        cursor=conn.cursor()
        sql='''select depreciation_rate from open_by_year_volume where year=%d and
        depreciation_rate is not null and depreciation_rate<1 and brand_slug='dazhong' and volume>1.7 and volume<2.1 and units>%d'''%(ye,100)
        cursor.execute(sql)
        alldata=cursor.fetchall()
        cursor.close()
        n=len(alldata)
        y_temp=zeros((n,))
        for i in range(0,n):
            y_temp[i]=alldata[i][0]
        v_temp=average(y_temp)
        y0[ye-1990]=v_temp
        add=0
        if y0[ye-1990]>0:
            mark+=1
            for i in range(0,n):
                add+=(y_temp[i]-y0[ye-1990])**2
        add=add/(n*y0[ye-1990]**2)
        add0+=add
    add0=add0/mark
    print 'accuracy rate:',add0
            
    for i in range(1990,2015):
        print x0[i-1990],y0[i-1990]

    cursor=conn.cursor()
    sql='''select year,depreciation_rate from open_by_year_volume where
    depreciation_rate is not null and depreciation_rate<1 and brand_slug='dazhong' and volume>1.7 and volume<2.1 and units>%d'''%100
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
    print "Sample Num：",n
    plt.plot(x,y,'.',x0,y0,'ro')
    plt.axis([1990,2015,0,1])
    plt.xlabel('Year')
    plt.ylabel('Depreciation_rate')
    plt.title('Depreciation_rate by Year')
    plt.text(1991, 0.8, "samples choosen by 'units>100'")
    plt.show() 

#and brand_slug='acura'
#plt.grid(True)
#plt.text(1995, 0.8, r'$\mu=100,\ \sigma=15$')

def DepreciationRatebrand(brand):
    try:
        conn=MySQLdb.connect(host="192.168.1.96",user="zhangzupeng",
                             passwd="zhangzupeng",db="pingjia",charset="utf8")
    except Exception,error:
        print error
        sys.exit()
    x0=arange(1990,2015)
    y0=zeros((25,))
    for ye in range(1990,2015):
        cursor=conn.cursor()
        sql='''select depreciation_rate from open_by_year_volume where
        model_slug='%s' and year=%d and depreciation_rate is not null and
        depreciation_rate<1 and units>%d'''%(brand,ye,10)
        cursor.execute(sql)
        alldata=cursor.fetchall()
        cursor.close()
        n=len(alldata)
        y_temp=zeros((n,))
        for i in range(0,n):
            y_temp[i]=alldata[i][0]
        v_temp=average(y_temp)
        y0[ye-1990]=v_temp
    for i in range(1990,2015):
        print x0[i-1990],y0[i-1990]

    cursor=conn.cursor()
    sql='''select year,depreciation_rate from open_by_year_volume where
    model_slug='%s' and depreciation_rate is not null and depreciation_rate<1
    and units>%d'''%(brand,10)
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

    print "Sample Num：",n
    plt.plot(x,y,'.',x0,y0,'ro')
    plt.axis([1990,2015,0,1])
    plt.xlabel('Year')
    plt.ylabel('Depreciation_rate')
    plt.title('Depreciation_rate by Year of %s'%brand)
    plt.text(1991, 0.8, "samples choosen by 'units>10'")
    plt.show()

if __name__ == "__main__":
    DepreciationRateall()
