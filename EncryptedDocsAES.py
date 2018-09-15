from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

header = "header"

#data should not be visible in code
class Main():
    def __init__(self, data):

        data = bytes(data, 'utf8')

        #Randomly generated key, set to fixed key for constant value
        key = get_random_bytes(32)

        print(key)

        #instantiate cipher object
        cipher = AES.new(key, AES.MODE_EAX)

        cipher.update(data)

        self.encryptData = cipher.encrypt(data)

        print('This is the encrypted data')
        print(self.encryptData)

        #this should initialize update?
        self.next = cipher.update(self.encryptData)

        cipher.update(self.encryptData)

        self.decryptData = cipher.decrypt(self.encryptData)

        print('This is the decrypted data')
        print(self.decryptData)

    #Encrypt data using AES, generating ciphertext and tag for verification

    #ciphertext, tag = cipher.encrypt_and_digest(data)

data = Main('here is some data')

print(Main.encryptData)