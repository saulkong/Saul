__author__ = 'xiaocong'



from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import probplot


class Regression(object):
    def __init__(self,dataset):
        self.dataset=dataset


    def Construct(self):
        bk=LinearRegression()
        X=self.data[['project_workload','demand_eval_density','code_eval_density','sys_de_weighing','de_density']]
        y=self.data['production_efficiency']
        bk.fit(X,y)
        prediction=bk.predict(X)
        print prediction
        print bk.coef_
        print np.mean(y-prediction)



        f1=plt.figure(figsize=(7,5));ax1=f1.add_subplot(211);ax1.hist(self.data['project_workload']-prediction,bins=50);
        ax1.set_title('Histogram of Residuals')



        ax2=f1.add_subplot(212)
        probplot(self.data['production_efficiency']-prediction,plot=ax2)
        print "which",prediction




    def SelectProjectType(self):
        self.data=self.dataset[self.dataset['type']=='s']


def ReadFile(file):
    return pd.read_csv(file)

def main():
    data=ReadFile('/Users/xiaocong/Downloads/datasource/regression_data_file.csv')

    run=Regression(data)
    run.SelectProjectType()
    run.Construct()

if __name__=='__main__':
    main()