__author__ = 'xiaocong'

from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import probplot


columns=['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','car name']
"""
    Attribute Information:

    1. mpg:           continuous
    2. cylinders:     multi-valued discrete
    3. displacement:  continuous
    4. horsepower:    continuous
    5. weight:        continuous
    6. acceleration:  continuous
    7. model year:    multi-valued discrete
    8. origin:        multi-valued discrete
    9. car name:      string (unique for each instance)
"""

data=pd.read_csv('/Users/xiaocong/Downloads/datasource/auto_mpg_data/auto-mpg.data-original.txt',
                 names=columns,sep='\\s+')

data=data.dropna()
print 'Data Description\n\n',data.describe()


colnums=len(data.columns)
rownums=len(data)


data_train=data[:350]
data_test=data[350:]

data_train_X=data_train.iloc[:,1:colnums-1].values
data_train_y=data_train.loc[:,['mpg']].values



data_test_X=data_test.iloc[:,1:colnums-1].values
data_test_y=data_test.loc[:,['mpg']].values





regr=linear_model.LinearRegression()
regr.fit(data_train_X,data_train_y)


predictions=regr.predict(data_test_X)


print regr.predict(data_test_X).shape
print data_test_X.shape


print 'Coefficients: \n', regr.coef_
print 'Intercept:\n',regr.intercept_
print "Residual sum of squares: %.2f"% np.mean((data_test_y-predictions)**2)

print 'Variance score: %.2f' % regr.score(data_test_X, data_test_y)




f=plt.figure(figsize=(7,5))
ax=f.add_subplot(111)
ax.hist(data_test_y-regr.predict(data_test_X),bins=10)
#f=plt.figure(figsize=(7,5))
#bx=f.add_subplot(111)
#probplot(data_test_y-predictions,plot=bx)

