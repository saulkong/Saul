__author__ = 'xiaocong'


from time import time
import numpy as np
from pandas import DataFrame
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

np.random.seed(10)

data=pd.read_csv('/Users/xiaocong/Downloads/datasource/seeds_dataset.txt',header=None,sep='\t')


"""
    The examined group comprised kernels belonging to three different varieties of wheat: Kama, Rosa and Canadian,

    Attribute Information:

    1. area A,
    2. perimeter P,
    3. compactness C = 4*pi*A/P^2,
    4. length of kernel,
    5. width of kernel,
    6. asymmetry coefficient
    7. length of kernel groove.

"""
data=data.dropna()
data[7]=data[7]-1


data_values=data.iloc[:,:7].values
data_values=scale(data_values)



#print 'Data Description \n',data.describe()
labels=data.iloc[:,7].values
sample_size=20


print("n_digits: %d, \t n_samples %d, \t n_features %d"
      % (3, len(data), 7))
print(79 * '_')
print('% 9s' % 'init'
      '         time  inertia  homo   compl   v-meas    ARI     AMI ')





def bench_k_means(estimator, name, data):
    t0 = time()
    estimator.fit(data)
    print('% 9s   %.2fs    %i   %.3f   %.3f   %.3f   %.3f   %.3f   '
          % (name, (time() - t0), estimator.inertia_,
             metrics.homogeneity_score(labels, estimator.labels_),
             metrics.completeness_score(labels, estimator.labels_),
             metrics.v_measure_score(labels, estimator.labels_),
             metrics.adjusted_rand_score(labels, estimator.labels_),
             metrics.adjusted_mutual_info_score(labels,  estimator.labels_),
             ))

bench_k_means(KMeans(init='k-means++', n_clusters=3, n_init=20),
              name="k-means++", data=data)

bench_k_means(KMeans(init='random', n_clusters=3, n_init=20),
              name="random", data=data)

# in this case the seeding of the centers is deterministic, hence we run the
# kmeans algorithm only once with n_init=1
pca = PCA(n_components=3).fit(data)
bench_k_means(KMeans(init=pca.components_, n_clusters=3, n_init=1),
              name="PCA-based",
              data=data)
print(79 * '_')



