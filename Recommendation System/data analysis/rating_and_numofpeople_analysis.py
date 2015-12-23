__author__ = 'xiaocong'

# -*- coding:utf-8 -*-

from mongodb_conn import Mongodb_connect
import matplotlib.pyplot as plt
from sklearn import linear_model
from pandas import DataFrame
import types
connection=Mongodb_connect().conn()

coll=connection.doubaninfo  #collection name is doubaninfo


def film_ls():
    """
        X axis stands for the total number of film-goers to post long review,
        y axis stands for the total number of film-goers to post brief review.
    """


    film_rating_X=[]
    film_rating_y=[]

    for item_ls in coll.find():
        if type(float(item_ls['film_long_review']))==types.FloatType and type(float(item_ls['film_brief_review']))==types.FloatType:
            film_rating_X.append(item_ls['film_long_review'])
            film_rating_y.append(item_ls['film_brief_review'])

    film_rating_X=DataFrame(film_rating_X)
    film_rating_y=DataFrame(film_rating_y)
    plt.subplot(2,1,1)
    plt.scatter(film_rating_X,film_rating_y,color='black')
    plt.title('(sum)film_long_review --- film_brief_review')

    film_rating_X_train=film_rating_X[:-100]
    film_rating_X_test=film_rating_X[-100:]

    film_rating_y_train=film_rating_y[:-100]
    film_rating_y_test=film_rating_y[-100:]

    regr=linear_model.LinearRegression()
    regr.fit(film_rating_X_train,film_rating_y_train)
    print('(trianed_ls)Coefficients : %s '%regr.coef_[0][0])
    plt.subplot(2,1,2)
    plt.scatter(film_rating_X_test,film_rating_y_test,color='black')
    plt.plot(film_rating_X_test,regr.predict(film_rating_X_test),color='red',linewidth=3)
    plt.xlim([-2000,10000])
    plt.ylim([-40000,200000])
    plt.xlabel('film_long_review')
    plt.ylabel('film_brief_review')
    plt.xticks(())
    plt.yticks(())
    plt.title('(trained)film_long_review --- film_brief_review')
    plt.show()


def film_al():

    """
        X axis stands for the average rating of film rated by film-goers,
        y axis stands for the total number of film-goers to post long review.
    """


    film_rating_X=[]
    film_rating_y=[]
    for item_la in coll.find():
         if type(float(item_la['film_long_review']))==types.FloatType and type(float(item_la['film_grading'][0]['average_grading']))==types.FloatType:
            film_rating_y.append(item_la['film_long_review'])
            film_rating_X.append(item_la['film_grading'][0]['average_grading'])

    film_rating_X=DataFrame(film_rating_X)
    film_rating_y=DataFrame(film_rating_y)

    plt.subplot(2,1,1)
    plt.scatter(film_rating_X,film_rating_y,color='black')
    plt.title('(sum)film_average_grading --- film_long_review')

    film_rating_X_train=film_rating_X[:-100]
    film_rating_X_test=film_rating_X[-100:]

    film_rating_y_train=film_rating_y[:-100]
    film_rating_y_test=film_rating_y[-100:]

    regr=linear_model.LinearRegression()
    regr.fit(film_rating_X_train,film_rating_y_train)
    print('(trained_al)Coefficients : %s '%regr.coef_[0][0])
    plt.subplot(2,1,2)
    plt.scatter(film_rating_X_test,film_rating_y_test,color='black')
    plt.plot(film_rating_X_test,regr.predict(film_rating_X_test),color='red',linewidth=3)

    plt.ylabel('film_long_review')
    plt.xlabel('film_average_grading')
    plt.xticks(())
    plt.yticks(())
    plt.title('(trained)film_average_grading --- film_long_review ')
    plt.show()


def film_ab():

    """
        X axis stands for the average rating of film rated by film-goers,
        y axis stands for the total number of film-goers to post brief review.
    """


    film_rating_X=[]
    film_rating_y=[]
    for item_la in coll.find():
         if type(float(item_la['film_brief_review']))==types.FloatType and type(float(item_la['film_grading'][0]['average_grading']))==types.FloatType:
            film_rating_y.append(item_la['film_brief_review'])
            film_rating_X.append(item_la['film_grading'][0]['average_grading'])

    film_rating_X=DataFrame(film_rating_X)
    film_rating_y=DataFrame(film_rating_y)

    plt.subplot(2,1,1)
    plt.scatter(film_rating_X,film_rating_y,color='black')
    plt.title('(sum)film_average_grading --- film_brief_review')

    film_rating_X_train=film_rating_X[:-100]
    film_rating_X_test=film_rating_X[-100:]

    film_rating_y_train=film_rating_y[:-100]
    film_rating_y_test=film_rating_y[-100:]

    regr=linear_model.LinearRegression()
    regr.fit(film_rating_X_train,film_rating_y_train)
    print('(trained_ab)Coefficients : %s '%regr.coef_[0][0])
    plt.subplot(2,1,2)
    plt.scatter(film_rating_X_test,film_rating_y_test,color='black')
    plt.plot(film_rating_X_test,regr.predict(film_rating_X_test),color='red',linewidth=3)

    plt.ylabel('film_brief_review')
    plt.xlabel('film_average_grading')
    plt.xticks(())
    plt.yticks(())
    plt.title('(trained)film_average_grading --- film_brief_review ')
    plt.show()



if __name__=='__main__':

    film_ls()
    film_al()
    film_ab()

