import os
import shutil

def moveFiles():
    MAIN = r"C:\Users\User\Desktop\python\organize files\temp"

    DIRS = r"C:\Users\User\Desktop\python\organize files\files_for_sorting"

    for root, subdirs, files in os.walk(DIRS):
        for file in files:
            path = os.path.join(root, file)
            shutil.move(path, MAIN)

def organizeFiles():
    path = r"C:\Users\User\Desktop\python\organize files\temp"
    path3 = r"C:\Users\User\Desktop\python\organize files\folders"
    os.makedirs(path3)
    l = os.listdir(path)
    for e in l:
        #print(f"File name is {e} and the extenson is {os.path.splitext(e)[1]}")
        #make new directory based on file type
        newPath = f"C:/Users/User/Desktop/python/organize files/folders/{os.path.splitext(e)[1]}"
        try:
            os.makedirs(newPath)
    
    names = os.listdir(path)
    path, dirs, files = next(os.walk(r"C:\Users\User\Desktop\python\organize files\folders"))
    file_count = len(dirs)
    semi_ext_array = []
    for i in range (file_count):
        l = os.listdir(r"C:\Users\User\Desktop\python\organize files\folders")
        for e in l:
            #print(f"File name is {e} and the extenson is {os.path.splitext(e)[0]}")
            data = str(e)
            semi_ext_array.append(data)

    ext_type = list(dict.fromkeys(semi_ext_array))
    
    for files in names:
        path = r"C:\Users\User\Desktop\python\organize files\temp"
        for x in range(0,file_count):
            result = files.endswith(ext_type[x])           
            if result == True:
                shutil.move(path+f"\{files}", path3+f"\{ext_type[x]}")          
            x+=1
moveFiles()
organizeFiles()
print("Organizing done. View \"folders\" folder for your files sorted according to theie extension")      




        
        

