"""
-*- coding: utf-8 -*-
Created by lhy on 2021/4/24 22:27
Description:
"""

# coding: utf-8
import sys, os
import time
sys.path.append(os.pardir)  # 为了导入父目录的文件而进行的设定
import numpy as np
import pickle
from dataset.mnist import load_mnist
from common.functions import sigmoid, softmax


def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_train, t_train, x_test, t_test


def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network


def predict(network, x):
    w1, w2, w3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, w1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, w2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, w3) + b3
    y = softmax(a3)

    return y


def NonBatch(x_test, t_test, network):
    accuracy_cnt = 0
    start = time.time()
    for i in range(len(x_test)):
        y = predict(network, x_test[i])
        p = np.argmax(y)  # 获取概率最高的元素的索引
        if p == t_test[i]:
            accuracy_cnt += 1
    end = time.time()
    print('Running time: %s Seconds' % (end - start))
    print("Accuracy:" + str(float(accuracy_cnt) / len(x_test)))


def Batch(x_test, t_test, batch_size, network):
    accuracy_cnt = 0
    start = time.time()
    for i in range(0, len(x_test), batch_size):
        x_batch = x_test[i:i + batch_size]
        y_batch = predict(network, x_batch)
        p = np.argmax(y_batch, axis=1)
        accuracy_cnt += np.sum(p == t_test[i:i + batch_size])
    end = time.time()
    print('Running time: %s Seconds' % (end - start))
    print("Accuracy:" + str(float(accuracy_cnt) / len(x_test)))


if __name__ == '__main__':
    batch_size = 100  # 批数量
    x_train, t_train, x_test, t_test = get_data()
    network = init_network()

    NonBatch(x_test, t_test, network)
    Batch(x_test, t_test, batch_size, network)


