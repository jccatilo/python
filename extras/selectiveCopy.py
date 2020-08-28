import os, shutil

def selectiveCopy(folder, destination):

    #walks through folder using os.walk(folder)
    for foldername, subfolders, filenames in os.walk(folder):
        print('in os.walk() for ' + folder)
        for filename in filenames:
            # select files with pdf ending
            if filename.endswith('.pdf'):
                print('Copying %s from %s to %s...' % (
                    filename, foldername, destination))
                shutil.copy(os.path.join(foldername,filename), destination')
    #adds files with folder.endswith('.pdf') to new folder

selectiveCopy('./folder1/',
              './folder1/pdf_Folder/')