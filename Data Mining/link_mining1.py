
# -*-coding:utf-8 -*-

import codecs
import re
import urlparse




data=codecs.open('/Users/xiaocong/Downloads/url__.txt','r','utf-8')
data1=codecs.open('/Users/xiaocong/Downloads/url__1.txt','r','utf-8')
data=[e for e in data.read().strip().split('\n')]
data1_=[e for e in data1.read().strip().split('\n')]
f1=data1_

data2=codecs.open('/Users/xiaocong/Downloads/url__2.txt','a','utf-8')
for i in data:
    m=i in f1
    if not m:
        data2.write(i+'\n')


data=codecs.open('/Users/xiaocong/Downloads/url.txt','r','utf-8')
data2=codecs.open('/Users/xiaocong/Downloads/url__3.txt','a','utf-8')
data=[e.strip().split('\t') for e in data.read().strip().split('\n')]
for i in data:
    if len(i)==2:
        i[0]=i[0]
        i[1]=urlparse.urlsplit(i[1]).netloc
        data2.write(i[0]+'\t'+i[1]+'\n')


f1=[]
data3=codecs.open('/Users/xiaocong/Downloads/url__1.txt','r','utf-8')
data4=codecs.open('/Users/xiaocong/Downloads/url__2.txt','r','utf-8')
data3_=[e for e in data3.read().strip().split('\n')]
data4_=[e for e in data4.read().strip().split('\n')]
print len(data4_)

data5=codecs.open('/Users/xiaocong/Downloads/url__2.txt','r','utf-8')
data6=codecs.open('/Users/xiaocong/Downloads/url__3.txt','r','utf-8')
data5_=[e.strip() for e in data5.read().strip().split('\n')]
data6_=[e.strip.split('\t') for e in data6.read().strip().split('\n')]
print data6_

f2=[]
data7=codecs.open('/Users/xiaocong/Downloads/url__3.txt','r','utf-8')
data8=codecs.open('/Users/xiaocong/Downloads/url__4.txt','a','utf-8')

data7_=[e.strip().split('\t') for e in data7.read().strip().split('\n')]
for i in data7_:
    if len(i)==2:
        i[1]=i[1].encode('utf-8')
        if i[1] not in f2:
            i[0]=i[0].encode('utf-8').split('_')[0]
            f2.append(i[1])
            print i[0]+'\t'+i[1]
            data8.write(i[0].decode('utf-8')+'\t'+i[1].decode('utf-8')+'\n')

data9=codecs.open('/Users/xiaocong/Downloads/url__4.txt','r','utf-8')
data9_=[e.strip().split('\t') for e in data9.read().strip().split('\n')]
data10=codecs.open('/Users/xiaocong/Downloads/url__2.txt','r','utf-8')
data10_=[e.strip() for e in data10.read().strip().split('\n')]
data11=codecs.open('/Users/xiaocong/Downloads/url__7.txt','a','utf-8')
f=[]
k=0
for i in data10_:
    k=0
    for j in data9_:
        k+=1
        if len(j)==2:
            m=re.search(i.encode('utf-8'),j[1].encode('utf-8'))
            if m:
                print j[0]+'\t'+i
                data11.write(j[0]+'\t'+i+'\n')
                break
        if k==len(data9_):
            u=i.replace('www','')
            v=0
            for l in data9_:
                v+=1
                if len(l)==2:
                    m=re.search(u.encode('utf-8'),l[1].encode('utf-8'))
                    if m:
                        print l[0]+'\t'+i
                        data11.write(l[0]+'\t'+i+'\n')
                        break
                if v==len(data9_):
                    print '\t'+i
                    data11.write('\t'+i+'\n')








data10=codecs.open('/Users/xiaocong/Downloads/url__7.txt','r','utf-8')
data10_=[e.strip().split('\t') for e in data10.read().strip().split('\n')]
print len(data10_)




data12=codecs.open('/Users/xiaocong/Downloads/url__5.txt','r','utf-8')
data12_=[e for e in data12.read().strip().split('\n')]
print data12_[1]








