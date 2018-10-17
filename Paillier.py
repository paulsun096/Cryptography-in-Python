from phe import paillier
'''
In this example, find existing bloom filters to act the meta-data
to be encrypted by Paillier encryption.

The generation of meta-data by finding the union and intersection of multi-sets as
described in the paper will be replaced by using a python library that uses bitarrays
to generate bloomfilters, in order to demonstrate how paillier encryption will work.

Once this example is finished, the next task is to generate the bloom-filters
using the AES, intersection and union technique as described in the paper.

'''
#Paillier secret (private) key: sk, public key: pk

#GENERATE PUBLIC KEY AND PRIVATE KEY PAIRS

pk, sk = paillier.generate_paillier_keypair()

print(pk)
print(sk)

sec_num1 = 2.0
sec_num2 = 4.0

enc_num1 = pk.encrypt(sec_num1)
enc_num2 = pk.encrypt(sec_num2)

result = sec_num1 + 10
result2 = sec_num2 + sec_num1
result3 = sec_num1 * 10

print("enc + scalar: " + str(result))
print("enc + enc: " + str(result2))
print("enc * scalar: " + str(result3))

#BLOOMFILTER SET OF DOCUMENTS AS META-DATA: Ld = (Ld1, Ld2, ... Ldi)
#FOR SINGLE EXAMPLE DOCUMENT: Ld

#META DATA FOR STRING: TODAY IS GOING TO BE GREAT
#Ld
