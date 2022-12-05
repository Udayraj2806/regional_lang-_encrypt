# # Python code to demonstrate
# # decode()

# # initializing string
# str = input()

# # encoding string
# str_enc = str.encode(encodeing='utf8')

# # printing the encoded string
# print("The encoded string in base64 format is : ",)
# print(str_enc)

# # printing the original decoded string
# print("The decoded string is : ",)
# print(str_enc.decode('utf8', 'strict'))
import codecs
import pickle

from cryptography.fernet import Fernet

with codecs.open('plaintext1.txt', encoding='utf-8') as f:
    input = f.read()
message = (input)
print(message)
# # Python code to demonstrate
# # decode()

# # initializing string
# str = "geeksforgeeks"

# # encoding string
# str_enc = str.encode()

# # printing the encoded string
# print("The encoded string in base64 format is : ",)
# print(str_enc)

# # printing the original decoded string
# print("The decoded string is : ",)
# print(str_enc.decode('utf8', 'strict'))

# from cryptography.fernet import Fernet

# we will be encryting the below string.
# message = ""

# generate a key for encryptio and decryption
# You can use fernet to generate
# the key or use random key generator
# here I'm using fernet to generate key

key = Fernet.generate_key()
f = open("key.txt", "a")
# Instance the Fernet class with the key
key1 = str(key, 'UTF-8')

f.write(key1)
f1 = open('key.txt', 'r')
p11 = f1.read()
res = bytes(p11, 'utf-8')
fernet = Fernet(res)

# then use the Fernet class instance
# to encrypt the string string must
# be encoded to byte string before encryption
encMessage = fernet.encrypt(message.encode())


print("original string: ", message)
print("encrypted string: ", encMessage)

# decrypt the encrypted string with the
# Fernet instance of the key,
# that was used for encrypting the string
# encoded byte string is returned by decrypt method,
# so decode it to string with decode methods

print(type(encMessage))
p1 =str(encMessage, 'UTF-8')
print(p1)
decMessage = fernet.decrypt(encMessage).decode()

print("decrypted string: ", decMessage)

