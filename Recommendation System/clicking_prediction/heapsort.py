__author__ = 'xiaocong'

# -*- coding:utf-8 -*-

def sift(R,low,high):
    i=low
    j=2*i
    tmp=R[i]
    while(j<=high):
        if j<high and R[j].values()[0]<R[j+1].values()[0]:
            j+=1
        if tmp.values()[0]<R[j].values()[0]:
            R[i]=R[j]
            i=j
            j=i*2
        else:
            break
    R[i]=tmp

def HeapSort(R,n):
    i=n/2
    tmp=R[0]
    recommendlist=list()
    while i>=1:
        sift(R,i,n)
        i-=1
    i=n
    while(i>=2):
        recommendlist.append(R[1])
        tmp=R[1]
        R[1]=R[i]
        R[i]=tmp
        sift(R,1,i-1)
        i-=1
    return  recommendlist


