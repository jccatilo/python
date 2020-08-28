import os
import shutil
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def encryptFiles():
    inputFolderName = input("Absolute path of folder/directory you want to encrypt: ");
    folderName = f"{inputFolderName}"
    inputUser = input("Choose a password (WARNING: DO NOT FORGET! You will not be able to decrypt folder if you will forget the password): ")
    password_provided = f"{inputUser}"
    password = password_provided.encode()
    salt = b'\xa2*\xd5\xa6\x16\x0b\x90\xc2\x8db"\xcc]F\xb4\xe9'
    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length = 32,
        salt = salt,
        iterations = 100000,
        backend=default_backend()
        )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    #print(key)

    file = open ('key.key','wb')
    file.write(key)
    file.close()
    #print("key file generated. See Key.key ...")
    file = open('key.key', 'rb');
    key = file.read()
    file.close()

    folders = [j for j in os.listdir(folderName) if os.path.isfile(os.path.join(folderName, j))] #displays files onleh
    for j in folders:
        x = "\\"
        z = folderName+x+j
        with open (z, 'rb') as f:
            data = f.read()
        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)
        os.remove(z)
        with open (z, 'wb') as f:
            f.write(encrypted)
        print(z)
        z = folderName
    print("files in folder successfully encrypted")
    os.remove('key.key')


def decryptFiles():    
    inputFolderName = input("Absolute path of folder/directory you want to decrypt: ");
    folderName = f"{inputFolderName}"
    inputUser = input("Enter password that you used during encryption: ")
    password_provided = f"{inputUser}"
    password = password_provided.encode()

    salt = b'\xa2*\xd5\xa6\x16\x0b\x90\xc2\x8db"\xcc]F\xb4\xe9'
    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length = 32,
        salt = salt,
        iterations = 100000,
        backend=default_backend()
        )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    #print(key)
    file = open ('key.key','wb')
    file.write(key)
    file.close()
    #print("key file generated. See Key.key ...")
    file = open('key.key', 'rb');
    key = file.read()
    file.close()
    folders = [j for j in os.listdir(folderName) if os.path.isfile(os.path.join(folderName, j))] #displays files onleh
    for j in folders:
        x = "\\"
        z = folderName+x+j    
        with open (z, 'rb') as f:
            #print(fileName)
            data = f.read()
        fernet = Fernet(key)
        decrypted = fernet.decrypt(data)
        
        os.remove(z)
        with open (z, 'wb') as f:
            f.write(decrypted)    
    print("Files in folder successfully decrypted! Enjoy!")
    os.remove('key.key')
    
def main():
    inputUser =  input("Press 1 to Encrypt files. Press 2 to Decrypt files: ")
    userInput = f"{inputUser}"
    if userInput == "1":
        encryptFiles()
    elif userInput == "2":
        decryptFiles()
    else:
        print("invalid input.")


main()
