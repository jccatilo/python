#this code is to show a method of having a user input so he has same key everytime.

import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password_provided = "password" #this is input in the form of a string
password = password_provided.encode() #convert to type bytes

#generate salt by typing the ff in shell
#import os
#os.urandom(16)

salt = b'\x86Z\x12t"w\x02\x95\xe2\xb0\x0c\xc6\xbc\xdaek'

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length = 32,
    salt=salt,
    iterations = 100000,
    backend=default_backend()
    )
key = base64.urlsafe_b64encode(kdf.derive(password)) #can only use kdf once
print (key)
