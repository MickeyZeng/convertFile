import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    # np.set_printoptions(threshold=np.inf)
    test = np.load("testDic/279_IM-0004-0001.png.npy")
    # temp = np.zeros(test.shape)
    # groundTruth = 0
    # if groundTruth == 0:
    #     result = np.stack((test, temp))
    # else:
    #     result = np.stack((temp, test))
    #
    # result = result.astype('uint8')
    # np.save("testDic/9_IM-0001-0002.png.npy", result)

    # for display the scribble and original image
    image = plt.imread("testDic/IM-0003-0002.png")
    plt.imshow(image)
    plt.imshow(test, alpha=.5)
    plt.show()
