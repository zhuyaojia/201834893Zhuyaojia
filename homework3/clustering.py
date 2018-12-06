# -*- coding: utf-8 -*-
import os
import nltk
import sklearn
import numpy
from sklearn import metrics
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
nltk.download()
numpy.set_printoptions(threshold = numpy.inf)
#若想不以科学计数显示:
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
vectorizer=CountVectorizer()
transformer=TfidfTransformer()
tfidf=transformer.fit_transform(vectorizer.fit_transform(words))
weight=tfidf.toarray()
#print weight
from sklearn.cluster import KMeans
num_clusters = len(relresult)#聚成89个类
km_cluster = KMeans(n_clusters=num_clusters, max_iter=300, n_init=40,
                   init='k-means++', n_jobs=-1)
 #返回各自文本的所被分配到的类索引
preresult = km_cluster.fit_predict(weight)
print "Predicting result: ", preresult
#使用NMI评价
#evaluation=metrics.adjusted_mutual_info_score(preresult, cnumber)#值越大表示预测结果和真实结果越接近
#print evaluation
