__author__ = 'xiaocong'

# -*- coding:utf-8 -*-


def BubbleSort(R,n,K):
    i=0
    recommend=list()
    while i<n-1:
        j=n-1

        while j>i:
            if R[j].values()[0]>R[j-1].values()[0]:
                tmp=R[j-1]
                R[j-1]=R[j]
                R[j]=tmp
            j-=1
        recommend.append(R[i])
        print R[i]
        i+=1
        K-=1
        if K==0:
            break
    return recommend



