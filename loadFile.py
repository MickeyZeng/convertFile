# import numpy as np
# from matplotlib import pyplot as plt
#
# if __name__ == '__main__':
#     # np.set_printoptions(threshold=np.inf)
#     test = np.load("testDic/210_IM-0001-0001.png.npy")
#     test = np.swapaxes(test, 1, 2)
#     test = np.swapaxes(test, 0, 1)
#     # temp = np.zeros(test.shape)
#     # groundTruth = 0
#     # if groundTruth == 0:
#     #     result = np.stack((test, temp))
#     # else:
#     #     result = np.stack((temp, test))
#     #
#     # result = result.astype('uint8')
#     # np.save("testDic/9_IM-0001-0002.png.npy", result)
#
#     # for display the scribble and original image
#     # image = plt.imread("testDic/IM-0003-0002.png")
#     # plt.imshow(image)
#     plt.imshow(test, alpha=.5)
#     plt.show()

import os

import numpy as np
import pandas as pd
from tqdm import tqdm


#
#
def copy_files_to_new_csv(files):
    tempCSV = pd.read_csv("validate.csv")
    tempPath = []
    result_rows = None

    for i in files:
        temp = i.split("/")[6] + '/' + i.split("/")[7]
        temp = temp.split('.')[0] + '.png'
        tempPath.append(temp)

    for i in tempPath:
        if result_rows is not None:
            result_rows = pd.concat([tempCSV.loc[tempCSV['image_path'] == i], result_rows], ignore_index=True)
        else:
            result_rows = tempCSV.loc[tempCSV['image_path'] == i]
    result_rows.to_csv("availableTemp.csv", index=False)
    pass


def findUnlabeledImage(file):
    test = np.load(file)

    # if all 0 - did not scribble yet
    if test.max() == 0:
        return file
    # else did scribble

    return


#
def main():
    root_folder_name = '/testScribble'
    root_path = os.getcwd() + root_folder_name
    # 1: get all the folders
    folders = os.listdir(root_path)
    # print(dirs)
    not_label_arr = []

    # 2: loop every folder get all the files within the folders
    for folder in tqdm(folders):
        if folder == '.DS_Store':
            continue
        path_to_file = root_path + '/' + folder + '/'
        folder_files = os.listdir(path_to_file)
        for file in folder_files:
            if file == '.DS_Store':
                continue
            file_full_path = path_to_file + file

            # 3: rename the file
            # if file == '.DS_Store':
            #     continue
            # splitted_name = file.split('_')
            # new_name = splitted_name[1]
            # # print(new_name)
            # os.rename(file_full_path, path_to_file + new_name)

            # 4: swap axies

            # 5: change 2 to -1, change 1 to 2, -1 to 1

            # 6: change thickness

            result = findUnlabeledImage(file_full_path)
            if result:
                not_label_arr.append(result)
            # old code
            # test = np.load(file_full_path)
            #
            # # 1 -> neg, 2 -> pos
            # test = np.where(test == 1, 3, test)
            # test = np.where(test == 2, 1, test)
            # test = np.where(test == 3, 2, test)
            #
            # # chagne axes
            # test = np.swapaxes(test, 0, 1)
            # test = np.swapaxes(test, 1, 2)
            #
            # np.save(file_full_path, test)
    print(len(not_label_arr))
    print(not_label_arr)
    # copy_files_to_new_csv(not_label_arr)


#
#
# def main1():
#     test = np.load(
#         "/Users/mickey/PycharmProjects/loadNumpy/testScribble/9/IM-0001-0002.npy")
#
#     # # 1 -> neg, 2 -> pos
#     # test = np.where(test == 1, 3, test)
#     # test = np.where(test == 2, 1, test)
#     # test = np.where(test == 3, 2, test)
#
#     # # chagne axes
#     # test = np.swapaxes(test, 0, 1)
#     # test = np.swapaxes(test, 1, 2)
#
#     pass
#
#
# def main2():
#     folder_name = 'truthScribble'
#     result_folder = 'testScribble'
#     files = os.listdir(folder_name)
#     for file in files:
#         if file == '.DS_Store':
#             continue
#
#         content = np.load(folder_name + "/" + file)
#
#         # print(file)
#         patientId = file.split("_")[0]
#         newName = file.split("_")[1].split(".")[0] + "." + file.split("_")[1].split(".")[2]
#         # os.rename(os.path.join(folder_name + '/' + file), newName)
#
#         # print(os.path.join(folder_name + '/' + file))
#         # print(newName)
#         np.save(result_folder + "/" + patientId + "/" + newName, content)
#
#
# def main3():
#     testPath = "testScribble/210/IM-0001-0001.png.npy"
#     testContent = np.load(testPath)
#     print(testContent.shape)
#
#
if __name__ == '__main__':
    # print('hello')
    main()
