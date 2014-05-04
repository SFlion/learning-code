'''about year-contract rate '''

#import os,sys
import MySQLdb
from numpy import *
#import matplotlib
import matplotlib.pyplot as plt

def DepreRateYearGap(brand='dazhong',unit=100,colar='-go'):
    try:
        conn=MySQLdb.connect(host="192.168.1.96",user="zhangzupeng",
                             passwd="zhangzupeng",db="pingjia",charset="utf8")
    except Exception,error:
        print error
        sys.exit()

    x1=arange(2010,2015)
    y1=zeros((5,))
    add1=0
    mark1=0
    for ye in range(2010,2015):
        cursor=conn.cursor()
        sql='''select depreciation_rate,volume from open_by_year_volume where year=%d
        and depreciation_rate is not null and depreciation_rate<1 and brand_slug='%s'
        and volume=2 and units>%d'''%(ye,brand,unit)
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

    x2=arange(2010,2015)
    y2=zeros((5,))
    add2=0
    mark2=0
    for ye in range(2010,2015):
        cursor=conn.cursor()
        sql='''select depreciation_rate,volume from open_by_year_volume where year=%d
        and depreciation_rate is not null and depreciation_rate<1 and brand_slug='%s'
        and volume=3 and units>%d'''%(ye,brand,unit)
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

    #print 'original accuracy rate1:',1-add1
    #print 'original accuracy rate2:',1-add2
    if  (y1-y2)[0]>-1:
        print 'YearGap is:',y1-y2,brand
        plt.plot(x1,y1-y2,colar)
        
    '''plt.plot(x1,y1,'-bo',x2,y2,'-go')
    plt.axis([1990,2015,0,1])
    plt.xlabel('Year')
    plt.ylabel('Depreciation_rate')
    plt.title('Depreciation_rate by Year of dazhong')
    plt.text(1991, 0.8, "samples choosen by 'units>100'")
    plt.show()'''

    return y1-y2

if __name__ == "__main__":
    DepreRateYearGap()
