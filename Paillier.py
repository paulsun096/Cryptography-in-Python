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

#BLOOMFILTER SET OF DOCUMENTS AS META-DATA: Ld = (Ld1, Ld2, ... Ldi)
#FOR SINGLE EXAMPLE DOCUMENT: Ld

#META DATA FOR STRING: TODAY IS GOING TO BE GREAT
#Ld








