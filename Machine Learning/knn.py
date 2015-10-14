__author__ = 'xiaocong'

from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.preprocessing import scale
import numpy as np
import pandas as pd

data=pd.read_csv('/Users/xiaocong/Downloads/datasource/knn_data_file.txt',header=None)
data_value=scale(data.iloc[:,:4])
data_label=data[4]

X=np.array(data_value)
y=np.array(data_label)

clf=NearestCentroid()
clf.fit(X,y)
test_set=[5.2,3.8,1.1,0.3]
print (clf.predict(test_set))


