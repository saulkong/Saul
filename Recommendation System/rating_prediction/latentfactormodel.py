__author__ = 'xiaocong'

# -*- coding:utf-8 -*-


import random
import math
import codecs

def InitModel(train,F):
    """
    init decomposing model
    p means user-classification matrix
    q means classfication-item matrix
    bu means user bias
    bi means item bias
    """
    p=dict()
    q=dict()
    bu=dict()
    bi=dict()
    for tra in train:
        user,item,rating,timestamp=tra.split('::')
        bu[user]=0.0
        bi[item]=0.0
        if user not in p:
            p[user]=list()
            for i in range(0,F):
                p[user].append(random.random()/math.sqrt(F))
        if item not in q:
            q[item]=list()
            for i in range(0,F):
                q[item].append(random.random()/math.sqrt(F))
    return p,q,bu,bi


def SinglePredict(user,item,p,q,bu,bi,mu):
    #predict a rating of single item belonging to single user
    ret=mu+bu[user]+bi[item]
    for f in range(len(p[user])):
        ret+=p[user][f]*q[item][f]
    return ret





def GlobalAverage(train):
    total_num=0.0
    sum_rating=0.0
    for tra in train:
        total_num+=1
        user,item,rating,timestamp=tra.split('::')
        sum_rating+=float(rating)
    return sum_rating/(total_num)


def LearningBiasLFM(train,F,n,alpha,_lambda,mu):
    p,q,bu,bi=InitModel(train,F)
    for step in range(0,n):
        for tra in train:
            user,item,rating,timestamp=tra.split('::')
            prediction_rating=SinglePredict(user,item,p,q,bu,bi,mu)
            prediction_error=float(rating)-prediction_rating
            bu[user]+=alpha*(prediction_error-_lambda*bu[user])
            bi[item]+=alpha*(prediction_error-_lambda*bi[item])
            for f in range(0,F):
                p[user][f]+=alpha*(q[item][f]*prediction_error-_lambda*p[user][f])
                q[item][f]+=alpha*(p[user][f]*prediction_error-_lambda*q[item][f])
        alpha*=0.9
    return p,q,bu,bi


def TotalPrediction(train,test,F,N,alpha,_lambda):
    """
    train means train set
    test means test set
    F means latent factor model decomposition dimension
    N means cycle index for latent factor model
    alpha means study parameter for latent factor model
    _lambda means fitting parameter for latent factor model

    """

    mu=GlobalAverage(train)
    p,q,bu,bi=LearningBiasLFM(train,F,N,alpha,_lambda,mu)
    prediction_error=0.0
    train_users_set=set()
    train_items_set=set()
    for tra in train:
        user,item,rating,timestamp=tra.split('::')
        train_users_set.add(user)
        train_items_set.add(item)

    for te in test:
        user,item,rating,timestamp=te.split('::')
        if user in train_users_set and item in train_items_set:
            prediction_rating=SinglePredict(user,item,p,q,bu,bi,mu)
            prediction_error+=(float(rating)-prediction_rating)**2
    RMSE=math.sqrt(prediction_error)/len(test)

    return RMSE





if __name__=='__main__':
    train_file=codecs.open('/Users/xiaocong/Downloads/moviedata/testfile/train_set.txt','r','utf-8')
    train_data=[x for x in train_file.read().split('\n') if x]
    test_file=codecs.open('/Users/xiaocong/Downloads/moviedata/testfile/test_set.txt','r','utf-8')
    test_data=[x for x in test_file.read().split('\n') if x]
    RMSE=TotalPrediction(train_data,test_data,10,10,0.01,0.01)
    print 'RMSE:',RMSE
    #RMSE: 0.00728231973819
    train_file.close()
    test_file.close()
