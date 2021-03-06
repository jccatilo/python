import os
import shutil

def moveFiles():
    inputDIRS =  input("Enter absolute path of folder containing the files to be sorted: ")
    DIRS = f"{inputDIRS}"
    
    print(DIRS)
    MAIN = r"C:/Users/ENGR/OneDrive/Documents/python/organize_files/temp"

    try:
        os.makedirs(MAIN)
    except OSError:
        print ("Creation of the directory %s failed. Already exists." % MAIN)
    else:
        print ("Successfully created the directory. %s" % MAIN)
    #DIRS = r"C:/Users/User/Desktop/python/organize files/files_for_sorting"

    for root, subdirs, files in os.walk(DIRS): #do not remove any of root, subdirs, or files. error will occur.
        for file in files:
            path = os.path.join(root, file)
            shutil.move(path, MAIN)

    return inputDIRS


def organizeFiles(DIRS):
    path = r"C:/Users/ENGR/OneDrive/Documents/python/organize_files/temp"
    #path3 = r"C:/Users/User/Desktop/python/organize files/folders"
    path3 = DIRS
    
    try:
        os.makedirs(path3)
    except OSError:
        print ("Creation of the directory %s failed. Already exists." % path3)
    else:
        print ("Successfully created the directory. %s" % path3)
    l = os.listdir(path)
    for e in l:
        #make new directory based on file type
        newPath = f"{path3}/{os.path.splitext(e)[1]}"
        
        try:
            os.makedirs(newPath)
        except OSError:
            print ("Creation of the directory %s failed. Already exists." % newPath)
        else:
            print ("Successfully created the directory. %s" % newPath)

    names = os.listdir(path)
    path, dirs, files = next(os.walk(path3))
    file_count = len(dirs)
    semi_ext_array = []
    for i in range (file_count):
        l = os.listdir(path3)
        for e in l:
            #print(f"File name is {e} and the extenson is {os.path.splitext(e)[0]}")
            data = str(e)
            semi_ext_array.append(data)

    ext_type = list(dict.fromkeys(semi_ext_array))
    
    for files in names:
        path = r"C:/Users/ENGR/OneDrive/Documents/python/organize_files/temp"
        for x in range(0,file_count):
            result = files.endswith(ext_type[x])
            
            if result == True:
                shutil.move(path+f"\{files}", path3+f"\{ext_type[x]}")
            
            x+=1


def deleteTempFolder():
    temp_path = r'C:/Users/ENGR/OneDrive/Documents/python/organize_files/temp'
    os.rmdir(temp_path)

def main():
    print("###Python file organizer rev1###")
    inputDIRS = moveFiles()
    organizeFiles(inputDIRS)
    deleteTempFolder()
    

main()

print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print("Organizing done. View folder directory for your files sorted according to their extension.") 




        
        

