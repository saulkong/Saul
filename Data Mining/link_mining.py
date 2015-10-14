__author__ = 'xiaocong'

# -*- coding: utf-8 -*-
import urlparse
import codecs
import re


topHostPostfix = (
    '.com','.la','.io','.co','.info','.net','.org','.me','.mobi',
    '.us','.biz','.xxx','.ca','.co.jp','.com.cn','.net.cn',
    '.org.cn','.mx','.tv','.ws','.ag','.com.ag','.net.ag','.gov.cn','edu.cn',
    '.org.ag','.am','.asia','.at','.be','.com.br','.net.br','.cn',
    '.bz','.com.bz','.net.bz','.cc','.com.co','.net.co',
    '.nom.co','.de','.es','.com.es','.nom.es','.org.es',
    '.eu','.fm','.fr','.gs','.in','.co.in','.firm.in','.gen.in',
    '.ind.in','.net.in','.org.in','.it','.jobs','.jp','.ms',
    '.com.mx','.nl','.nu','.co.nz','.net.nz','.org.nz',
    '.se','.tc','.tk','.tw','.com.tw','.idv.tw','.org.tw',
    '.hk','.co.uk','.me.uk','.org.uk','.vg', ".com.hk")



path='/Users/xiaocong/Downloads/url.txt'
path=codecs.open(path,'r','utf-8')


f=[list(e.strip().split('\t')) for e in path.read().strip().split('\n')]
f1=[]
f2=[]
f3=[]
f4=[]
f5=[]

for i in f:
    if(len(i)==2):
        j=i[1]
        f1.append(j)


for i in f1:
    j=urlparse.urlsplit(i).netloc
    f2.append(j)

for i in f2:
    j=i.replace('www.','')
    f3.append(j)

for i in f3:
    j='.'+i
    f4.append(j)


f6=set(f4)
f7=list(f6)


output=codecs.open('/Users/xiaocong/Downloads/url2.txt','w','utf-8')
for i in f7:
    output.write(i+'\n')
output.close()
path.close()


fdomain=[]
TopHostPostfix=[]
for i in range(len(topHostPostfix)):
    TopHostPostfix.append('\.'+'(\w+)'+topHostPostfix[i]+'$')
for i in range(len(TopHostPostfix)):
    for j in range(len(f7)):
        m=re.search(TopHostPostfix[i],f7[j])
        if(m):
            fdomain.append(m.group())

fdomain=set(fdomain)
fdomain=list(fdomain)


output1=codecs.open('/Users/xiaocong/Downloads/url3.txt','w','utf-8')
for i in fdomain:
    output1.write(i+'\n')
output1.close()


input=codecs.open('/Users/xiaocong/Downloads/url3.txt','r','utf-8')
input=[e for e in input.read().split('\n')]
print type(input[1].encode('utf-8'))





url2data=codecs.open('/Users/xiaocong/Downloads/url2.txt','r','utf-8')
url3data=codecs.open('/Users/xiaocong/Downloads/url3.txt','r','utf-8')
url2data=list([e for e in url2data.read().split('\n')])
url3data=list([e for e in url3data.read().split('\n')])


url4data=codecs.open('/Users/xiaocong/Downloads/url5.txt','w','utf-8')
finaldata=set()


for i in range(len(url3data)):
    k=0
    urlpattern=url3data[i].encode('utf-8')

    for j in range(len(url2data)):

        urlstring=url2data[j].encode('utf-8')
        m=urlpattern in urlstring
        if(m==True and urlpattern!=urlstring):
            k=k+1

            if(k==2):
                finaldata.add(url3data[i])
                print url3data[i]
                break

finaldata=list(finaldata)
for i in finaldata:
    url4data.write(i+'\n')

url4data.close()




for i in range(len(url2data)):

    m=re.search('.51cto.com',url2data[i])
    if(m):
        print m.group()



data10=[]
input=codecs.open('/Users/xiaocong/Downloads/url5.txt','r','utf-8')
input=[e for e in input.read().split('\n')]
for i in range(len(input)):
    j=input[i][1:]
    data10.append(j)


input1=codecs.open('/Users/xiaocong/Downloads/url__.txt','r','utf-8')
input2=[e for e in input1.read().split('\n')]
input3=sorted(input2,reverse=True)

