__author__ = 'xiaocong'

# -*- coding:utf-8 -*-


import math
import random
import codecs
import operator
from heapsort import HeapSort
from computeperformance import Recall_Precision,Coverage

def UserItemTable(_set):
    #build inverse table for users_items
    users_items=dict()
    for tra in _set:
        user,item,rating,timestamp=tra.split('::')
        if user not in users_items:
            users_items[user]=set()
        users_items[user].add(item)
    return users_items


def ItemSimilarity(users_items):
    #calculate co-related users between items
    #initiate C matrix and N matrix
    C=dict()
    N=dict()
    for u,items in users_items.items():
        for i in items:
            N[i]=0
            if i not in C:
                C[i]=dict()
            for j in items:
                if i==j:
                    continue
                C[i][j]=0

    #calculate similarity matrix W
    for u,items in users_items.items():
        for i in items:
            N[i]+=1
            for j in items:
                if i==j:
                    continue
                C[i][j]=C[i][j]+1

    for i,related_items in C.items():
        for j,cij in related_items.items():
            C[i][j]=cij/math.sqrt(N[i]*N[j])

    #normalize similarity matrix W

    for i,related_items in C.items():
        max=0
        for j,wij in related_items.items():
            if wij>max:
                max=wij
        for j,wij in related_items.items():
            C[i][j]=C[i][j]/max
    print 'generate final itemsimilarity'

    return C





def Recommendation(train,test,K):
    train_users_items=UserItemTable(train)
    test_users_items=UserItemTable(test)
    C=ItemSimilarity(train_users_items)
    rankdict=dict()
    ranklist=dict()
    recommendlist=dict()
    for user,items in train_users_items.items():
        rankdict[user]=dict()
        ranklist[user]=list()
        recommendlist[user]=list()
        for item in items:
            for related_item,cij in C[item].items():
                if related_item in items:
                    continue
                if related_item not in rankdict[user]:
                    rankdict[user][related_item]=0.0
                rankdict[user][related_item]+=cij
        ranklist[user].append({'stuffing':0})
        for item,value in rankdict[user].items():
            ranklist[user].append({item:value})
        recommendlist[user]=HeapSort(ranklist[user],len(rankdict[user]))[:K]
        print 'user:',user,'recommendlist finished'

    recall_proportion,precision_proportion=Recall_Precision(train_users_items,test_users_items,K,recommendlist)
    coverage_proportion=Coverage(train_users_items,recommendlist)
    return recall_proportion,precision_proportion,coverage_proportion





if __name__=='__main__':
    train_file=codecs.open('/Users/xiaocong/Downloads/moviedata/train_set.txt','r','utf-8')
    train=[x for x in train_file.read().split('\n') if x]
    test_file=codecs.open('/Users/xiaocong/Downloads/moviedata/test_set.txt','r','utf-8')
    test=[x for x in test_file.read().split('\n') if x]
    r,p,c=Recommendation(train,test,2)
    print r,p,c
    # 0.0369713312518 0.277422790202 0.0206122135056
    train_file.close()
    test_file.close()
































































































