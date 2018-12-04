#!/usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: zhou_me
@file: perceptron.py 
@time: 2018/12/04
@contact: zhou_me@worksap.co.jp
@site:  
@software: PyCharm
"""

ITERATION = 70
W = [1, 1, 1]


def createData():
    lines_set = open('dataSet_pla.txt').readlines()
    linesTrain = lines_set[1:7]
    linesTest = lines_set[8:13]

    trainDataList = processData(linesTrain)
    testDataList = processData(linesTest)
    return trainDataList, testDataList


def processData(lines):
    dataList = []
    for line in lines:
        dataLine = line.strip().split()
        dataLine = [int(data) for data in dataLine]
        dataList.append(dataLine)
    return dataList


def sign(W, dataList):
    sum = 0
    for i in range(len(W)):
        sum += W[i] * dataList[i]
    if sum > 0:
        return 1
    else:
        return -1


def renewW(W, trainData):
    signResult = sign(W, trainData)
    if signResult == trainData[-1]:
        return W
    for k in range(len(W)):
        W[k] = W[k] + trainData[-1] * trainData[k]
    return W


def trainW(W, trainDatas):
    newW = []
    for num in range(ITERATION):
        index = num % len(trainDatas)
        newW = renewW(W, trainDatas[index])
    return newW


def predictTestData(W, trainDatas, testDatas):
    W = trainW(W, trainDatas)
    print W
    for i in range(len(testDatas)):
        result = sign(W, testDatas[i])
        print result


trainDatas, testDatas = createData()

predictTestData(W, trainDatas, testDatas)