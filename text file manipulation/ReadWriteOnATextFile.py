'''
read / write / overwrite/ append a text file
r =read
w = write/overwrite
a+ = append
w+ = create/write

/n = new line
/r = carriage return
'''
file = "C:/Users/User/Desktop/python/text-file.txt"
from time import sleep

def createFile():
    #Creating new file...
    print("Creating file...")
    ThisFile = open(file,"w")
    ThisFile.write("Hi. I'm a newly created text file.")
    ThisFile.close()

def readTextFile():
    #read
    #print("Reading...")
    ThisFile = open(file,"r")
    a = ThisFile.read()
    ThisFile.close()
    print(a)

def overWritingFile():
    #writing/overwrite
    print("Overwriting...")
    ThisFile = open(file,"w")
    ThisFile.write("Successfully overwritten!")
    ThisFile.close()

def appendingFile():
    #appending
    print("Appending...")
    ThisFile = open(file,"a+")
    ThisFile.write("\n"+str("Added new line")+"\n"+str("and another Line."))
    ThisFile.close()

print("hello JC!")
    
createFile()
sleep(1)
readTextFile()
sleep(1)
overWritingFile()
sleep(1)
readTextFile()
sleep(1)
appendingFile()
sleep(1)
readTextFile()

