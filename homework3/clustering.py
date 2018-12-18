# -*- coding: utf-8 -*-
import os
import nltk
import sklearn
import numpy
from sklearn import metrics
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
numpy.set_printoptions(threshold = numpy.inf)
#nltk.download()
# KMeans聚类:
def KMeansclustering(weight,num_clusters):
    from sklearn.cluster import KMeans

    km_cluster = KMeans(n_clusters=num_clusters, max_iter=300, n_init=40,
                  init='k-means++', n_jobs=-1)
 #返回各自文本的所被分配到的类索引
    preresult = km_cluster.fit_predict(weight)
    return preresult
#使用NMI评价
def evaluation(preresult,cnumber):
    evaluation=metrics.adjusted_mutual_info_score(preresult, cnumber)#值越大表示预测结果和真实结果越接近
    return evaluation
#Affinity propagation
def Affclustering(weight):
    from sklearn.cluster import AffinityPropagation
    #X = numpy.array(weight)
    clustering = AffinityPropagation(affinity='euclidean', convergence_iter=15, copy=True,
         damping=0.5, max_iter=200, preference=None, verbose=False).fit(weight)
    return clustering.labels_
#Spectral clustering
def Speclustering(weight,num_clusters):
    from sklearn.cluster import SpectralClustering
    clustering = SpectralClustering(n_clusters=num_clusters,assign_labels = "discretize",random_state = 0).fit_predict(weight)
    return clustering
#Mean-shirft
def Meanclustering(weight):
    from sklearn.cluster import MeanShift
    clustering = MeanShift(bandwidth=2, bin_seeding=False, cluster_all=True, min_bin_freq=1,
     n_jobs=None, seeds=None).fit_predict(weight)
    return clustering
#Ward hierarchical clustering
def Wardclustering(weight,num_clusters):
    from sklearn.cluster import AgglomerativeClustering
    clustering=AgglomerativeClustering(n_clusters=num_clusters, linkage='ward').fit_predict(weight)
    return clustering
#Agglomerative clustering
def Aggclustering(weight,num_clusters):
    from sklearn.cluster import AgglomerativeClustering
    clustering=AgglomerativeClustering(affinity='euclidean', compute_full_tree='auto',
            connectivity=None, linkage='ward', memory=None, n_clusters=num_clusters,
            pooling_func='deprecated').fit_predict(weight)
    return clustering
#DBSCAN
def DBSCANclustering(weight):
    from sklearn.cluster import DBSCAN
    clustering=DBSCAN(algorithm='auto', eps=3, leaf_size=30, metric='euclidean',
    metric_params=None, min_samples=2, n_jobs=None, p=None).fit_predict(weight)
    return clustering
#Gaussian Mixtures
def Gauclustering(weight):
    from sklearn import mixture
    clustering = mixture.BayesianGaussianMixture(n_components=8,covariance_type='full').fit_predict(weight)
    return clustering
numpy.set_printoptions(suppress = True)
path="C:\\Users\\Embedded\\Desktop\\homework3\\Tweets.txt"
f=open(path,'r')
str=f.readlines()
str_num=len(str)
word_list=[]
words=[]#每一类文本切词后的结果
cnumber=[]
allword=[]
text_word=[]
relresult=[]#真实类索引
for i in range(str_num):
    word=str[i].split(',')
    for w in word:
        word1=w.split(':')
        word_list.append(word1[1])
word_num=len(word_list)
for j in range(word_num):
    if(j%2==0):
      words.append(word_list[j])
    else:
        n=word_list[j].split('}\n')
        cnumber.append(n[0])
#print words
num=len(cnumber)
#print num
for i in range(num):
    if cnumber[i] not in relresult:
        relresult.append(cnumber[i])
#print len(relresult)一共89个类
for word1 in words:
      allword.append(nltk.word_tokenize(word1))
for aword in allword:
    for awords in aword:
        if(len(awords)>2):
            text_word.append(awords)

#print text_word
num_clusters = len(relresult)#聚成89个类
vectorizer=CountVectorizer()
transformer=TfidfTransformer()
tfidf=transformer.fit_transform(vectorizer.fit_transform(words))
weight=tfidf.toarray()
#KMeans聚类方法
#preresultForKMeans=KMeansclustering(weight,num_clusters)
#evaForKMeans=evaluation(preresultForKMeans,cnumber)
#print "Predicting result: ", preresult
#print evaForKMeans
#AffinityPropagation聚类方法
clustering=Gauclustering(weight)
print clustering
eva=evaluation(clustering,cnumber)
print eva