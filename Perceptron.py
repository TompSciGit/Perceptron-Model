from matplotlib import pyplot as plt
import numpy as np
import random as rnd
from Dataset import *

perceptrons = [[0.5, 1, 0]]
learning_rate = 0.1
iterations = 1000

costs = []  # keep log of costs through every iteration.


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def sigmoid_p(x):
    return sigmoid(x) * (1 - sigmoid(x))


def feedForward(weights, inputs, bias):
    z = 0
    for i in range(0, len(weights)):
        z = z + weights[i] * inputs[i]
    z = z + bias
    return sigmoid(z)


def costss(prediction, target):
    return (prediction - target) ** 2


def slope(prediction, target):
    return 2 * (prediction - target)  # Only for this case though


trainingData = createDataset(1, 0, 100)

## TRAINING

# get a random point
for iterr in range(0, iterations):
    ## choose a random training data point
    point = trainingData[rnd.randint(0, len(trainingData) - 1)]

    z = point[0] * perceptrons[0][0] + point[1] * perceptrons[0][1] + perceptrons[0][2]
    pred = sigmoid(z)  # networks prediction

    target = point[2]

    # cost for current random point
    cost = costss(pred, target)

    # print the cost over all data points every 1k iters
    if iterr % 10 == 0:
        c = 0
        for j in range(len(trainingData)):
            p = trainingData[j]
            p_pred = sigmoid(perceptrons[0][0] * p[0] + perceptrons[0][1] * p[1] + perceptrons[0][2])
            c += costss(p_pred, p[2])
        costs.append(c / j)

    dcost_dpred = slope(pred, target)
    dpred_dz = sigmoid_p(z)

    dz_dw1 = point[0]
    dz_dw2 = point[1]
    dz_db = 1

    dcost_dz = dcost_dpred * dpred_dz

    dcost_dw1 = dcost_dz * dz_dw1
    dcost_dw2 = dcost_dz * dz_dw2
    dcost_db = dcost_dz * dz_db

    perceptrons[0][0] = perceptrons[0][0] - learning_rate * dcost_dw1
    perceptrons[0][1] = perceptrons[0][1] - learning_rate * dcost_dw2
    perceptrons[0][2] = perceptrons[0][2] - learning_rate * dcost_db

## things we're interested in (costs, perceptrons[0][0], perceptrons[0][1], perceptrons[0][2])
fig = plt.plot(costs)
# plt.ylim([0, 1])
plt.show()
print(costs)
print("Done. ")
