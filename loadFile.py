
import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    np.set_printoptions(threshold=np.inf)
    test = np.load("testDic/IM-0004-0002.png.npy")
    for i in test:
        for j in i:
            if j == 1:
               print(i.tolist().index(j))
       # print(i)