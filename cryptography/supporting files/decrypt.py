from cryptography.fernet import Fernet
import os

#get key from the file
file  = open('key.key', 'rb')
key = file.read()
file.close()

#open the file to encrypt
with open ('test.txt.encrypted', 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.decrypt(data)

#write the encrypted file
with open ('test.txt.decrypted', 'wb') as f:
    f.write(encrypted)
