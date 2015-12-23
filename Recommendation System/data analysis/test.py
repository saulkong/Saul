__author__ = 'xiaocong'

# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model

diabetes=datasets.load_diabetes()
diabetes_X=diabetes.data[:,np.newaxis]
diabetes_X_temp=diabetes_X[:,:,2]


diabetes_X_train=diabetes_X_temp[:-20]
print type(diabetes_X_train)
diabetes_X_text=diabetes_X_temp[-20:]

diabetes_y_train=diabetes.target[:-20]
diabetes_y_test=diabetes.target[-20:]

regr=linear_model.LinearRegression()
regr.fit(diabetes_X_train,diabetes_y_train)

plt.scatter(diabetes_X_text,diabetes_y_test,color='black')
plt.plot(diabetes_X_text,regr.predict(diabetes_X_text),color='blue')

plt.xticks(())
plt.yticks(())
plt.show()
