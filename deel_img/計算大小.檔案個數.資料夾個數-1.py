import os
import sys
import datetime
from tqdm import tqdm
start = datetime.datetime.now()


def ONE_Statistics_file(rootdir):
    fileList = []
    fileSize = 0
    folderCount = 0
    for root, subFolders, files in os.walk(rootdir):
        folderCount += len(subFolders)
        for file in files:
            f = os.path.join(root, file)
            fileSize += os.path.getsize(f)
            # print(f)
            fileList.append(f)

    fileSize = fileSize/1000000000

    print("Total Size is {0} GB".format(round(fileSize, 2)))
    print('Total Files ', len(fileList))
    print('Total Folders', folderCount)


if __name__ == "__main__":  # 執行本文件則執行下述代碼
    rootdir = input("Please input the files path:")  # 輸入路徑
    ONE_Statistics_file(rootdir)


end = datetime.datetime.now()
print("執行時間：", end - start)
