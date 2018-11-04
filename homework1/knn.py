# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 18:55:24 2018

@author: Embedded
"""
import math
import operator
import csv
import random
import os
#计算距离
def euclideanDistance(instance1,instance2,length):
    distance = 0
    for x in range(length):
        distance = pow((instance1[x] - instance2[x]),2)
    return math.sqrt(distance)
#返回K个最近邻
def getNeighbors(trainingset,testInstance,k):
    distances = []
    length = len(testInstance) -1
    #计算每一个测试实例到训练集实例的距离
    for x in range(len(trainingset)):
        dist = euclideanDistance(testInstance, trainingset[x], length)
        distances.append((trainingset[x],dist))
    #对所有的距离进行排序
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    #返回k个最近邻
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors
#加载数据集
def loadDataset(filename,split,trainingset=[],testingset = []):
    files= os.listdir(filename)
    for filelist in files: #遍历文件夹
        tmp_path = os.path.join(filename,filelist)
        filess=os.listdir(tmp_path)
        for file in filess:
            if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
                csvfile=open(tmp_path+"/"+file,'r')#打开文件:
                lines = csv.reader(csvfile)
                dataset = list(lines)
                for x in range(len(dataset)-1):
                    for y in range(4):
                        dataset[x][y] = float(dataset[x][y])
                        if random.random()<split:
                            trainingset.append(dataset[x])
                        else:
                            testingset.append(dataset[y])
#对k个近邻进行合并，返回value最大的key
def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response]+=1
        else:
            classVotes[response] = 1
    #排序
    sortedVotes = sorted(classVotes.iteritems(),key = operator.itemgetter(1),reverse =True)
    return sortedVotes[0][0]
#计算准确率
def getAccuracy(testingset,predictions):
    correct = 0
    for x in range(len(testingset)):
        if testingset[x][-1] == predictions[x]:
            correct+=1
    return (correct/float(len(testingset))) * 100.0
def main():
    trainingset = []  #训练数据集
    testingset = []      #测试数据集
    split = 0.67      #分割的比例
    loadDataset(r"C:\Users\Embedded\Documents\GitHub\201834893zhuyaojia\20news-18828", split, trainingset, testingset) 
    print "Train set :" + repr(len(trainingset))
    print "Test set :" + repr(len(testingset))                
    
    predictions = []
    k = 3
    for x in range(len(testingset)):
        neighbors = getNeighbors(trainingset, testingset[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print ">predicted = " + repr(result) + ",actual = " + repr(testingset[x][-1])
    accuracy = getAccuracy(testingset, predictions)
    print "accuracy:" + repr(accuracy) + "%"
