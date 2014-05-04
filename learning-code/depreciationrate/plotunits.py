
#import sys
import MySQLdb
from numpy import *
#import matplotlib
import matplotlib.pyplot as plt

def plotunits():
    try:
        conn=MySQLdb.connect(host="192.168.1.96",user="zhangzupeng",
                             passwd="zhangzupeng",db="pingjia",charset="utf8")
    except Exception,error:
        print error
        sys.exit()
        
    unitsnum=zeros((8,))
    
    for i in range(5):
        cursor=conn.cursor()
        u=i+1
        sql="select count(*) from open_by_year_volume where units=%d"%u
        cursor.execute(sql)
        data=cursor.fetchone()
        cursor.close()
        unitsnum[i]=data[0]
        
    cursor=conn.cursor()
    sql="select count(*) from open_by_year_volume where units>5 and units<11"
    cursor.execute(sql)
    data=cursor.fetchone()
    cursor.close()
    unitsnum[5]=data[0]

    cursor=conn.cursor()
    sql="select count(*) from open_by_year_volume where units>10 and units<101"
    cursor.execute(sql)
    data=cursor.fetchone()
    cursor.close()
    unitsnum[6]=data[0]

    cursor=conn.cursor()
    sql="select count(*) from open_by_year_volume where units>100"
    cursor.execute(sql)
    data=cursor.fetchone()
    cursor.close()
    unitsnum[7]=data[0]

    labels = 'units=1','units=2','units=3','units=4','units=5','units=5-10','units=10-100','units>100'
    sizes = unitsnum
    colors = ['blue','red','green', 'gold', 'lightskyblue', 'lightcoral','yellow','yellowgreen']
    explode = (0, 0, 0,0,0,0,0,0) # only "explode" the 2nd slice (i.e. 'Hogs')

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=False, startangle=90)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    plt.title("units distribution")
    plt.show()

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x(), 1.03*height,'%s' %int(height))

    plt.xlabel('units')
    plt.ylabel('Num')
    plt.title("units distribution")
    plt.xticks(tuple(range(8)),('1','2','3','4','5','5-10','10-100','>100'))
    rect = plt.bar(left = tuple(range(8)),height = tuple(unitsnum),width = 0.5,align="center",yerr=0.000001)

    #plt.legend((rect,),(u"Í¼Àý",))
    #+rect.get_width()/2.
    autolabel(rect)

    #plt.show()

if __name__ == "__main__":
    plotunits()
        
