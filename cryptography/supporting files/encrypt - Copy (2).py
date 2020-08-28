from cryptography.fernet import Fernet
import os

#get key from the file
file  = open('key.key', 'rb')
key = file.read()
file.close()

#open the file to encrypt
with open ('test.txt', 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)
os.remove("test.txt")
print("file removed!!!!!!")

#write the encrypted file
with open ('test.txt.encrypted', 'wb') as f:
    f.write(encrypted)
