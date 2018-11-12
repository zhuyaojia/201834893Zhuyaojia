# -*- coding: utf-8 -*-
import os
import random
#import sklearn.cross_validation
#将数据集分成训练集和数据集，从每个文件夹中抽取80%作为训练集，20%作为测试集，最后得到总的训练集train，测试集test，每个元素都是文件的名字
def trainTestSplit(X, test_size=0.2):
           X_num = len(X)#所有文件数量
           train_num=int(X_num*(1-test_size))#训练集文件数量
          # train_index = range(train_num)
           #test_index = range(test_num)
           for i in range(train_num):
                train.append(X[i])
           for j in range(train_num+1,X_num):
                test.append(X[j])
           return train, test
#得到每个文件夹下的所有文件
def getlist(tmp_path):
        filess=os.listdir(tmp_path)#读取一个文件夹下的所有文件名
        return filess
def dividedata(dataset):
    dataset_num=len(dataset)
    data_list=[]
   #打开训练集下所有文件(一个文件夹下的)
    for j in range(dataset_num):
       file_path = os.path.join(tmp_path + "\\" + dataset[j])
       data_list=detaildividedata(file_path)
    return data_list
#具体分词
def detaildividedata(path):
    data_list=[]
    f = open(path, 'r')  # 打开一个文件
    str = f.read()
    word_list = str.split()
    # 处理一个文件
    for word1 in word_list:
        wordss = word1.strip(':().,"@`-;><!?_[]')
        word = wordss.strip("'")
        if (len(word) != 0):
            data_list.append(word)
    return data_list

def createVocabList(datalist):  #创建词库 这里就是直接把所有词去重后，当作词库
    vocablist = []
    data_len=len(datalist)
    for i in range(data_len):
        if datalist[i] not in vocablist:
             vocablist.append(datalist[i])
    return vocablist
def setOfWords2Vec(vocabList):  #文本词向量。词库中每个词当作一个特征，文本中就该词，该词特征就是1，没有就是0
    returnVec = [0] * len(vocabList)#returnVec是零矩阵
    docu_size=len(list)
    data_list=[]
    data_list=dividedata(list)
    for word in data_list:
         if word in vocabList:
             returnVec[vocabList.index(word)] = 1
    return returnVec
patha = "D:\\homework2\\20news-18828" #文件夹目录
files= os.listdir(patha) #得到文件夹下的所有文件夹名称
word_list = []
filess=[]
words=[]
str=""
train=[]#训练集文件的名字
test=[]#测试集文件的名字
list=[]#每个文件夹下所有文件名字的列表
train_vocab=[]
test_vocab=[]
filelist_num= len(files)
#分词后的集合
test_data=[]
train_data=[]
train_vec=[]#训练集的向量表示
test_vec=[]#测试集的向量表示
#for i in range(filelist_num):
    #处理一个文件夹下的所有文件
tmp_path = os.path.join(patha + "\\" + files[0])
list=getlist(tmp_path)
train, test =trainTestSplit(list, test_size=0.2)
#得到训练集和测试集的分词
train_data=dividedata(train)
test_data=dividedata(test)
train_vocab=createVocabList(train_data)
test_vocab=createVocabList(test_data)
train_vec.append(setOfWords2Vec(train_vocab))
#test_vec.append(setOfWords2Vec(test_vocab))
print train_vec
   #打开训练集下所有文件(一个文件夹下的)
# 打开训练集下所有文件(一个文件夹下的)


