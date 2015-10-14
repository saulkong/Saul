__author__ = 'xiaocong'

from pandas import DataFrame,Series
import pandas as pd
import numpy as np
from scipy.spatial.distance import euclidean
from random import randint

class Kmeans(object):

    def __init__(self,dataset,k):      #k means the number of clustering centre
        self.dataset=dataset.dropna()
        self.k=k
        self.index_set=[]           #index-value of firstclusering centre
        self.linage=len(self.dataset) # the number of points
        self.summatrix=[] # usage for designating which cluster does single point belong to
        self.colnums=len(self.dataset.columns)           #the number of columns of self.dataset
        #self.Coordinates=['A','B','C','D','E','F','G','H','I','J']         #diversion of self.dataset
        self.centroid_set=[]          #centre set of clustering including firstclusting




    def SelectPrimaryCluster(self):
        """randomly select the clustering-centre for firstclutering"""

        centre_set=[]

        while len(self.index_set)!=self.k:
            primaryindex=randint(0,self.linage-1)
            if primaryindex not in self.index_set:
                self.index_set.append(primaryindex)
                centre_set.append(self.dataset.ix[primaryindex])

        self.centroid_set.append(centre_set)

        print self.index_set



    def Clustering(self,u):

        """clustering ;
        u means the index position in the centroid_set """

        clustersys=['a','b','c','d','e','f','g','h','i','j'] #columns name for matrix
        centre_set=[]
        pre_array=np.zeros((self.linage,self.k))
        matrix=DataFrame(pre_array,columns=clustersys[:self.k])

        for i in range(self.linage):
            min=65535
            sel=clustersys[0]          #initial sel
            for j in range(self.k):
                p=clustersys[j]
                distance=euclidean(DataFrame(self.dataset.ix[i]).T,DataFrame(self.centroid_set[u][j]).T)
                if distance<min:
                    min=distance
                    sel=p
            matrix.ix[i][sel]=1
        self.summatrix.append(matrix)

        for i in matrix.columns:
            c_set=[]
            for j in range(self.linage):
                if matrix[i][j]==1:
                    c_set.append(j)

            centre_set.append(self.CalculateCentroid(c_set))
        self.centroid_set.append(centre_set)



    def CalculateCentroid(self,clu_set):
        """calculate the centre for each finished clustering"""
        cen=self.dataset.ix[clu_set]
        return Series(cen.mean())




    def Loop(self):
        """continually  clustering """
        i=0
        flag=True
        while(flag):
            self.Clustering(i)
            if i>=1:
                flag=self.TerminalCondition(self.summatrix[i],self.summatrix[i-1])
            i+=1
        print 'clustering time is  %d'%i



    def TerminalCondition(self,fore,back):
        """terminal condition for loop"""
        k=0
        DValue=fore.values-back.values
        for i in range(self.linage):
            for j in range(self.k):
                if DValue[i][j]==0:

                    k+=1
        if k==(self.linage*self.k):
            return False
        else:
            return True



def ReadFile(file):
    """read file"""
    return pd.read_csv(file,names=['A','B','C','D'])


def main():
    data=ReadFile('/Users/xiaocong/Downloads/kmeans_data_file.txt')
    run=Kmeans(data,5)
    run.SelectPrimaryCluster()

    run.Loop()
    print run.summatrix
    #print run.centroid_set


if __name__=='__main__':
    main()









