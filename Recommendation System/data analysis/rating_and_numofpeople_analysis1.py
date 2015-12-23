__author__ = 'xiaocong'

# -*- coding:utf-8 -*-

from mongodb_conn import Mongodb_connect
import matplotlib.pyplot as plt
from sklearn import linear_model
from pandas import DataFrame
import types
connection=Mongodb_connect().conn()

coll=connection.doubaninfo  #collection name is doubaninfo


def film_an():
    """
        X axis stands for the average-grading,
        y axis stands for the total number of people to rate.
    """


    film_rating_X=[]
    film_rating_y=[]

    for item_an in coll.find():
        if type(float(item_an['film_grading'][0]['average_grading']))==types.FloatType and type(float(item_an['film_grading'][0]['num_of_people_to_grading']))==types.FloatType:
            film_rating_X.append(item_an['film_grading'][0]['average_grading'])
            film_rating_y.append(item_an['film_grading'][0]['num_of_people_to_grading'])

    film_rating_X=DataFrame(film_rating_X)
    film_rating_y=DataFrame(film_rating_y)
    plt.subplot(2,1,1)
    plt.scatter(film_rating_X,film_rating_y,color='black')
    plt.title('(sum)average_grading --- num_of_people_to_grading')

    film_rating_X_train=film_rating_X[:-100]
    film_rating_X_test=film_rating_X[-100:]

    film_rating_y_train=film_rating_y[:-100]
    film_rating_y_test=film_rating_y[-100:]

    regr=linear_model.LinearRegression()
    regr.fit(film_rating_X_train,film_rating_y_train)
    print('(trianed_an)Coefficients : %s '%regr.coef_[0][0])
    plt.subplot(2,1,2)
    plt.scatter(film_rating_X_test,film_rating_y_test,color='black')
    plt.plot(film_rating_X_test,regr.predict(film_rating_X_test),color='red',linewidth=3)
    plt.xlim()
    plt.ylim()
    plt.xlabel('average_grading')
    plt.ylabel('num_of_people_to_grading')
    plt.xticks(())
    plt.yticks(())
    plt.title('(trained)average_grading --- num_of_people_to_grading')
    plt.show()









if __name__=='__main__':
    film_an()