from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = 'here is some data'

key = get_random_bytes(32)

data = bytes(data, 'utf8')

#instantiate cipher object
cipher = AES.new(key, AES.MODE_EAX)

cipher.update(data)

encryptData = cipher.encrypt(data)

print('This is the encrypted data')
print(encryptData)

#this should initialize update?
#next = cipher.update(encryptData)

#cipher.update(encryptData)

#decryptData = cipher.decrypt(encryptData)

print('This is the decrypted data')

#print(decryptData)