__author__ = 'xiaocong'

# -*- coding:utf-8 -*-

import random
import codecs

def ReadFile(file):
    data=codecs.open(file,'r','utf-8')
    return [x for x in data.read().split('\n') if x]

def SplitData(data,M,k,seed):
    test_set=codecs.open('/Users/xiaocong/Downloads/moviedata/test_set.txt','a','utf-8')
    train_set=codecs.open('/Users/xiaocong/Downloads/moviedata/train_set.txt','a','utf-8')
    random.seed(seed)
    for dat in data:
        print dat
        userid,movieid,rating,timestamp=dat.split('::')
        if userid=='1001':
            break
        print userid+'\t'+movieid+'\t'+rating+'\t'+timestamp
        if random.randint(0,M)==k:
            test_set.write(dat+'\n')
        else:
            train_set.write(dat+'\n')
    test_set.close()
    train_set.close()

if __name__=='__main__':
    data=ReadFile('/Users/xiaocong/Downloads/moviedata/ml-10M100K/ratings.dat')
    SplitData(data,8,6,1)

