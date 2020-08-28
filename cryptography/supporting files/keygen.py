import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

inputUser = input("Enter Password that you want (WARNING: DO NOT FORGET!, You will not be able to decrypt file if you will forget the password): ")
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
print(key)

file = open ('key.key','wb')
file.write(key)
file.close()
print("key file generated. See Key.key ...")
