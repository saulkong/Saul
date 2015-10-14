__author__ = 'xiaocong'


from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import probplot



data=pd.read_csv('/Users/xiaocong/Downloads/datasource/regression_data_file.csv')
data=data[data['type']=='s']
del data['type']


colnums=len(data.columns)
rownums=len(data)


data_train=data[:40]
data_test=data[40:]

data_train_X=data_train.iloc[:,:colnums-1].values
data_train_y=data_train.loc[:,['production_efficiency']].values


data_test_X=data_test.iloc[:,:colnums-1].values
data_test_y=data_test.loc[:,['production_efficiency']].values



regr=linear_model.LinearRegression()
regr.fit(data_train_X,data_train_y)

predictions=regr.predict(data_test_X)


print regr.predict(data_test_X).shape
print data_test_X.shape


print 'Coefficients: \n', regr.coef_
print "Residual sum of squares: %.2f"% np.mean((data_test_y-predictions)**2)

print 'Variance score: %.2f' % regr.score(data_test_X, data_test_y)




f=plt.figure(figsize=(7,5))
ax=f.add_subplot(111)
ax.hist(data_test_y-regr.predict(data_test_X),bins=5)
#f=plt.figure(figsize=(7,5))
#bx=f.add_subplot(111)
#probplot(data_test_y-predictions,plot=bx)






