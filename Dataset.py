import random as rnd
## FAKE DATA SET
## y = mx + c
def createDataset(m, c, size):
    # [y, x, correct?] (1:true, 0:false)
    cp = ''
    trainingData = []
    for i in range(0, size):
        x = rnd.randint(0, 101)
        y = rnd.randint(0, 101)
        if (y >= (m * x) + c):
            trainingData.append([y, x, 1])
            cp = 'b'
        else:
            trainingData.append([y, x, 0])
            cp = 'r'

        # plt.scatter([x],[y],c=cp, alpha=.2)
    # plt.show()

    return trainingData