__author__ = 'xiaocong'

# -*- coding:utf-8 -*-


import math
import random
import codecs
import operator
from bubblesort import BubbleSort
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



def RandomSelectNegativeSample(items):
    #single user item's basket including positive item and negative item
    items_pool_file=codecs.open('/Users/xiaocong/Downloads/moviedata/items_pool.txt','r','utf-8')
    items_pool=[x for x in items_pool_file.read().split('\n') if x]

    ret=dict()

    for item in items:
        ret[item]=1
    n=0
    for i in range(0,len(items)*10):
        item=items_pool[random.randint(0,len(items_pool)-1)]
        if item in ret:
            continue
        ret[item]=0
        n+=1
        if n>len(items):
            break

    items_pool_file.close()
    return ret

def InitModel(train,F):
    #init decomposing model
    """
    p means user-classification matrix
    q means classfication-item matrix
    bu means user bias
    bi means item bias
    """
    p=dict()
    q=dict()
    for tra in train:
        user,item,rating,timestamp=tra.split('::')
        if user not in p:
            p[user]=list()
            for i in range(0,F):
                p[user].append(random.random()/math.sqrt(F))
        if item not in q:
            q[item]=list()
            for i in range(0,F):
                q[item].append(random.random()/math.sqrt(F))

    return p,q

def Predict(user,item,p,q):
    #predict user behavior
    """
    p means user-classification matrix
    q means classfication-item matrix
    """
    all=0
    for f in range(0,len(p[user])):
        all+=p[user][f]*q[item][f]
    return all


def LatentFactorModel(train,users_items,F,N,alpha,_lambda):
    #train model
    p,q=InitModel(train,F)
    for step in range(0,N):
        for user,items in users_items.items():
            samples=RandomSelectNegativeSample(items)
            for item,rui in samples.items():
                eui=rui-Predict(user,item,p,q)
                for f in range(0,F):
                    p[user][f]+=alpha*(eui*q[item][f]-_lambda*p[user][f])
                    q[item][f]+=alpha*(eui*p[user][f]-_lambda*q[item][f])
        alpha*=0.9
    return p,q


def ItemInterestLevel(user,p,q):
    #single user's  interest level for all items
    level=dict()
    puf=p[user]
    len_puf=len(puf)
    for item ,qfi in q.items():
        for f in range(len_puf):
            if item not in level:
                level[item]=0
            level[item]+=puf[f]*qfi[f]

    print 'user:',user,'  ','iteminterstlevel finished'
    return level


def Recommendation(train,test,F,N,alpha,_lambda,K):
    """
    train means train set
    test means test set
    F means latent factor model decomposition dimension
    N means cycle index for latent factor model
    alpha means study parameter for latent factor model
    _lambda means fitting parameter for latent factor model
    K means the number of recommend items to each user

    """
    train_users_items=UserItemTable(train)
    test_users_items=UserItemTable(test)
    p,q=LatentFactorModel(train,train_users_items,F,N,alpha,_lambda)
    rankdict=dict()
    ranklist=dict()
    recommendlist=dict()
    for user in train_users_items.keys():
        rankdict[user]=dict()
        ranklist[user]=list()
        recommendlist[user]=list()
        level=ItemInterestLevel(user,p,q)
        for item,preference in level.items():
            if item not in train_users_items[user]:
                ranklist[user].append({item:preference})
        print ranklist[user]

        recommendlist[user]=BubbleSort(ranklist[user],len(ranklist[user]),K)
        print recommendlist[user]
        print 'user:',user,'recommendlist finished'

    recall_proportion,precision_proportion=Recall_Precision(train_users_items,test_users_items,K,recommendlist)
    coverage_proportion=Coverage(train_users_items,recommendlist)
    return recall_proportion,precision_proportion,coverage_proportion


if __name__=='__main__':
    train_file=codecs.open('/Users/xiaocong/Downloads/moviedata/train_set.txt','r','utf-8')
    train=[x for x in train_file.read().split('\n') if x]
    test_file=codecs.open('/Users/xiaocong/Downloads/moviedata/test_set.txt','r','utf-8')
    test=[x for x in test_file.read().split('\n') if x]
    r,p,c=Recommendation(train,test,10,10,0.02,0.01,2)
    print r,p,c
    # 0.0349843883054 0.262513312034 0.0241501307491
    train_file.close()
    test_file.close()








































