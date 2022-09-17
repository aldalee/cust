import os
import sys
import numpy as np
import pickle
sys.path.append(os.pardir)  # 为了导入父目录的文件而进行的设定
from PIL import Image
from dataset.mnist import load_mnist
from common.functions import sigmoid, softmax


# def init_network():
#     network = {'W1': np.random.random((784,50)), 'b1': np.random.rand(50),
#                'W2': np.random.random((50,100)), 'b2': np.random.rand(100),
#                'W3': np.random.random((100,10)), 'b3': np.random.rand(10)}
#     return network

def init_network():
    network = {'W1': np.random.uniform(-0.39754742,0.48118895,(784,50)), 'b1': np.random.uniform(-0.26460695,0.23342554,50),
               'W2': np.random.uniform(-1.0815927,0.8596072,(50,100)), 'b2': np.random.uniform(-0.13659105,0.19770803,100),
               'W3': np.random.uniform(-1.4223181,1.2528085,(100,10)), 'b3': np.random.uniform(-0.08397342,0.066196986,10)}
    return network


def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test


# def init_network():
#     with open("../experiment02/sample_weight.pkl", 'rb') as f:
#         network = pickle.load(f)
#     return network


def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y


x, t = get_data()
network = init_network()
accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network, x[i])
    p= np.argmax(y) # 获取概率最高的元素的索引
    if p == t[i]:
        accuracy_cnt += 1

print("Accuracy:" + str(float(accuracy_cnt) / len(x)))

f = open('sample_weight.pkl','rb')
data = pickle.load(f)
# print(data['W1'])

print(np.max(data['b1']))
print(np.min(data['b1']))

print(np.max(data['b2']))
print(np.min(data['b2']))

print(np.max(data['b3']))
print(np.min(data['b3']))
# print("-"*80)
# print(network['b1'])
# print(data['b1'].shape)
#
# print(data['W2'].shape)
# print(data['b2'].shape)
#
# print(data['W3'].shape)
# print(data['b3'].shape)

