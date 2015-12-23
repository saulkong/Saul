__author__ = 'xiaocong'

# -*- coding:utf-8 -*-

import math
import operator
import codecs




def UserItemTable(train):
    #build inverse table for users_items
    users_items=dict()
    for tra in train:
        user,item,rating,timestamp=tra.split('::')
        if user not in users_items:
            users_items[user]=dict()
        users_items[user][item]=float(rating)
    return users_items


def ItemSimilarity(train,users_items):
    """
    calculate corelation between items
    """

    #calculate average rating for the items  user rated
    T=dict() #items's total rating
    M=dict() #times's num
    A=dict() #average rating of items a user rated
    for tra in train:
        user,item,rating,timestamp=tra.split('::')
        if user not in T:
            T[user]=float(0)
            M[user]=0
        T[user]+=float(rating)
        M[user]+=1
    for user,ratings in T.items():
        A[user]=(ratings)/M[user]


    #init item similarity matrix
    C=dict() #store adjust cosine similarity matrix
    N=dict() #sum(rui-A[user])(ruj-A[user])
    S=dict() #sum(rui-A[user])**2 | (ruj-A[user])**2
    for u,items in users_items.items():
        for i in items:
            if i not in N:
                N[i]=dict()
                S[i]=float(0)
            if i not in C:
                C[i]=dict()
            for j in items:
                if i==j:
                    continue
                C[i][j]=float(0)
                N[i][j]=float(0)

    #calculate similarity between items
    for u,items in users_items.items():
        for i,i_rating in items.items():
            S[i]+=(i_rating-A[u])**2
            for j,j_rating in items.items():
                if i==j:
                    continue
                N[i][j]=N[i][j]+(i_rating-A[u])*(j_rating-A[u])



    for i ,related_items in N.items():
        for j,cij in related_items.items():
            if S[i]==0 or S[j]==0 or N[i][j]==0:
                continue
            C[i][j]=float(N[i][j]/math.sqrt((S[i]*S[j])))
    print 'generate itemsimilarity matrix'
    return C

def ItemAverageRating(train):
    """
    average rating for each item
    """

    I=dict()#each item's total ratings
    N=dict()#the number of each item
    A=dict()#average rating of each item
    for tra in train:
        user,item,rating,timestamp=tra.split('::')
        if item not in I:
            I[item]=float(0)
            N[item]=float(0)
        I[item]=I[item]+float(rating)
        N[item]+=1
    for item,ratings in I.items():
        A[item]=ratings/N[item]
    print 'generate item average rating matrix'
    return A




def Prediction(train,test,K):
    train_users_items=UserItemTable(train)
    test_users_items=UserItemTable(test)
    A=ItemAverageRating(train)
    C=ItemSimilarity(train,train_users_items)
    prediction_error=0
    for user,items in test_users_items.items():
        R=dict()# sum(wij(ruj-_ri))
        W=dict()# sum(abs(wij))
        for item,rating in items.items():
            if item in C:
                for related_item,cij in sorted(C[item].items(),key=operator.itemgetter(1),reverse=True)[:K]:
                    if cij==0:
                        continue
                    if related_item in train_users_items[user]:
                        if item not in R:
                            R[item]=0
                            W[item]=0
                        R[item]+=cij*(train_users_items[user][related_item]-A[item])
                        W[item]+=abs(cij)
            if item in A and item in R and item in W:
                prediction_rating=A[item]+R[item]/W[item]
                prediction_error+=(rating-prediction_rating)**2
    RMSE=math.sqrt(prediction_error)/len(test)
    return RMSE





if __name__=='__main__':
    train_file=codecs.open('/Users/xiaocong/Downloads/moviedata/testfile/train_set.txt','r','utf-8')
    traindata=[x for x in train_file.read().split('\n') if x]
    test_file=codecs.open('/Users/xiaocong/Downloads/moviedata/testfile/test_set.txt','r','utf-8')
    testdata=[x for x in test_file.read().split('\n') if x]
    p=Prediction(traindata,testdata,10)
    print 'RMSE:',p
    #RMSE: 0.00508280146008
    train_file.close()
    test_file.close()



































































