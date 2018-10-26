# -*- coding: utf-8 -*-
"""
Spyder Editor
"""
import nltk
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
#text=f.read()
#print(text)
import os
patha = "C:/Users/Embedded/Desktop/data mining/20news-18828" #文件夹目录
files= os.listdir(patha) #得到文件夹下的所有文件名称
s = []  
list=[]
for filelist in files: #遍历文件夹
    tmp_path = os.path.join(patha,filelist)
    filess=os.listdir(tmp_path)
    for file in filess:
        if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
            f = open(tmp_path+"/"+file); #打开文件
            iter_f = iter(f); #创建迭代器
            str = ""
            for line in iter_f: #遍历文件，一行行遍历，读取文本
                str = str + line
               # s.append(str) #每个文件的文本存到list中
                value = nltk.sent_tokenize(str.lower())
                for i in value:
                    words = nltk.word_tokenize(text=i)
                    for word1 in words:
                        wordss=word1.strip(':().,"@`-;><!?_[]')
                        word=wordss.strip("'")
                        if(len(word)!=0):
              #提取词干
                             lancaster_stemmer = LancasterStemmer()
                             words=lancaster_stemmer.stem(word) 
                             list.append(words)
#print(s)
#f=open('C:\\Users\\Embedded\\Desktop\\data mining\\20news-18828\\alt.atheism\\49960.txt','rb')
#text1=f.read()
#转小写
   #标志词性
        #words1 = nltk.word_tokenize(words)    
        #word_tag = nltk.pos_tag(words1)
        #print(word_tag)

print(list) 
#过滤stopwords
#filtered_words = [word3 for word3 in list if word3 not in stopwords.words('english')]       
#print(filtered_words)
#将文本中的词语转换为词频矩阵
#from sklearn.feature_extraction.text import CountVectorizer
#vectorizer = CountVectorizer()
#计算每个词语出现的次数
#X = vectorizer.fit_transform(filtered_words)
#获取词袋中所有文本关键词
#word4 = vectorizer.get_feature_names()
#print word4
#查看词频结果
#print X.toarray()
#from sklearn.feature_extraction.text import TfidfTransformer
#类调用
#transformer = TfidfTransformer()
#print transformer
#将词频矩阵X统计成TF-IDF值
#tfidf = transformer.fit_transform(X)
#查看数据结构 tfidf[i][j]表示i类文本中的tf-idf权重
#print tfidf.toarray() 



