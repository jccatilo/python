import os
import shutil

inputDIRS =  input("Enter absolute path of folder containing the files to be sorted: ")
DIRS = f"{inputDIRS}"
print(DIRS)

#dirs = os.listdir(DIRS) #displays folders and files
dirs = [f for f in os.listdir(DIRS) if os.path.isfile(os.path.join(DIRS, f))] #displays files onleh
#insideFiles = []
for f in dirs:
    print (f)
print (dirs)
#print (insideFiles)
#print (len(insideFiles))
