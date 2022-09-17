"""
-*- coding: utf-8 -*-
Created by lhy on 2020/11/9 20:22
Description:
"""

from math import log2
import operator
import pickle
from math import log


def creatDataset():  # 数据集的形成
    datafile = open("bank-data.csv", 'r')
    data = []
    t = 0
    for line in datafile:
        if "@data" in line:
            t = 2
        if t == 1:
            a = line.strip().split(",")  # strip 函数去除换行符\n，然后以逗号作为分割符
            data.append(a)  # 将数据添加到data中
            t = 2
        t -= 1
    for i in range(0, len(data)):  # 去掉无用数据ID号和收入
        del (data[i][4])
        del (data[i][0])
    # print(data)
    labels = ['age', 'sex', 'region', 'married', 'children', 'car', 'save_act', 'current_act', 'mortgage']
    return data, labels


def calcShannonEnt(dataset):  # 计算信息熵
    num_of_Entries = len(dataset)
    labelCounts = {}
    for featVec in dataset:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts.keys():
        prob = labelCounts[key] / num_of_Entries
        shannonEnt -= prob * log2(prob)
    return shannonEnt


def splitDataSet(dataset, axis, value):  # 根据特征划分数据axis表示特征， value表示特征的取值
    subDataSet = []
    for featVec in dataset:
        if featVec[axis] == value:
            reduce_featVec = featVec[:axis]
            reduce_featVec.extend(featVec[axis + 1:])
            subDataSet.append(reduce_featVec)
    return subDataSet


# 选择最佳的划分数据集的特征（ID3的信息增益法）（C4.5）
def chooseBestFeatureToSplit(dataset):
    num_of_feature = len(dataset[0]) - 1
    baseEntropy = calcShannonEnt(dataset)
    best_info_gain = 0.0
    bestLabel_index = -1
    for i in range(num_of_feature):
        feature_vec = [each[i] for each in dataset]
        uniqueVals = set(feature_vec)
        newEntroy = 0.0
        splitInfo = 0.0
        for value in uniqueVals:
            subdataset = splitDataSet(dataset, i, value)
            prob = len(subdataset) / float(len(dataset))
            newEntroy += prob * calcShannonEnt(subdataset)
            splitInfo -= prob * log(prob, 2);
        # print(splitInfo)
        if splitInfo == 0:
            splitInfo = 0.0000000001
        # print(splitInfo)
        info_gain = (baseEntropy - newEntroy) / splitInfo;
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            bestLabel_index = i
    return bestLabel_index


# 多数表决函数
def majorityVote(classlist):
    classcount = {}
    for each in classlist:
        if each not in classcount.keys():
            classcount[each] = 0
        classcount[each] += 1
    sorted_classcount = sorted(classcount.items(),
                               key=operator.itemgetter(1), reverse=True)
    return sorted_classcount[0][0]


# 树的创建
def createTree(dataset, label):
    t_label = label[:]
    classlist = [each[-1] for each in dataset]
    # 设置树的终止条件
    if classlist.count(classlist[0]) == len(classlist):
        return classlist[0]
    if len(dataset) == 1:
        return majorityVote(classlist)
    best_feature_index = chooseBestFeatureToSplit(dataset)
    best_feature = t_label[best_feature_index]
    myTree = {best_feature: {}}
    del (t_label[best_feature_index])
    feature_vec = [each[best_feature_index] for each in dataset]
    uniqueValues = set(feature_vec)
    for value in uniqueValues:
        sublabel = t_label[:]
        myTree[best_feature][value] = createTree(splitDataSet(dataset, best_feature_index, value),
                                                 sublabel)  # 递归调用createTree来创建树
    return myTree


# 判别函数
def classify(mytree, feat_label, testvec):
    global classLabel
    firstStr = list(mytree.keys())[0]
    secondDict = mytree[firstStr]
    feat_index = feat_label.index(firstStr)
    for key in secondDict.keys():
        if testvec[feat_index] == key:
            if isinstance(secondDict[key], dict):
                classLabel = classify(secondDict[key], feat_label, testvec)
            else:
                classLabel = secondDict[key]
    return classLabel  # 这块可能会存在隐藏的bug[系统提示，实际中操作还没遇到]


# 腌制树
def storeTree(mytree, filename):
    fw = open(filename, 'wb')
    pickle.dump(mytree, fw)
    fw.close()


# 取出树
def loadTree(filename):
    fr = open(filename, 'rb')
    return pickle.load(fr)


if __name__ == "__main__":
    dataSet, Labels = creatDataset()
    mytree = createTree(dataSet[:480], Labels)
    storeTree(mytree, "C4.5_tree")  # 形成树之后树的存储位置
    Tree = loadTree("C4.5_tree")  # 调用该位置的 树
    rs = dataSet[490:]
    result = []
    print(mytree)
    temp = []
    su = 0  # 记录预测正确数量
    for i in range(0, len(rs)):
        temp.append(rs[i][9])  # 将真实值存入temp数组中
        del (rs[i][9])
        result.append(classify(Tree, Labels, rs[i]))  # 将预测值添加进result中

    print("真实值", temp)
    print("预测值", result)
    for i in range(0, len(temp)):
        if temp[i] == result[i]:
            su += 1
    print("准确率为：", su / len(temp))



