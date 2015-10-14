__author__ = 'xiaocong'


from pandas import DataFrame
import pandas as pd
from scipy.spatial.distance import euclidean
from sklearn.preprocessing import scale

class Knn(object):
    def __init__(self,dataset):
        data_values=scale(dataset.iloc[:,:4])
        dataset[['a','b','c','d']]=data_values
        self.dataset=dataset

    def CountDistance(self,test_set,col_num):
        """calculate the distance between test_set and dataset"""
        print test_set
        linage=len(self.dataset)
        distance_set=[]
        for i in range(linage):
            single_distance=euclidean(DataFrame(self.dataset.ix[i][:col_num-1]).T,test_set)
            distance_set.append(single_distance)

        self.dataset['distance']=DataFrame(distance_set)
        print 'dataset with distance'
        print self.dataset

    def Educe(self,k):
        """determine which classification does test_set belong to"""
        max_collections=self.dataset.sort_index(by='distance')[:k]
        print 'the set top 10'
        print max_collections
        print '\n\n\n'
        result=pd.value_counts(max_collections['classification']).index[0]
        print 'test_set belongs to %s'%result





def read(fn):
    return pd.read_csv(fn,names=['a','b','c','d','classification'])


def main():
    test_set=[5.2,3.8,1.1,0.3]
    test_set=DataFrame(test_set).T
    col_num=5
    k=10
    data=read('/Users/xiaocong/Downloads/knn_data_file.txt')
    run=Knn(data)
    run.CountDistance(test_set,col_num)
    run.Educe(k)



if __name__=='__main__':
    main()