import os
import shutil

MAIN = r"C:\Users\User\Desktop\python\organize files\sorted"

DIRS = r"C:\Users\User\Desktop\python\organize files\files_for_sorting"

for root, subdirs, files in os.walk(DIRS):
    print('root', root)
    print('subdirs', subdirs)
    print('files', files)
    for file in files:
        path = os.path.join(root, file)
        print(path)
        shutil.move(path, MAIN)
