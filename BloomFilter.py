from bloom_filter import BloomFilter


'''
#Instantiate custom bloomfilter

bloom = BloomFilter(max_elements=500, error_rate=0.1)

#Test whether bloom-filter has seen a key
assert 'test-key' in bloom is False

#Mark the key as seen
bloom.add('test-key')

#check again
assert 'test-key' in bloom is True
'''

'''
filter = BloomFilter()

def generateFilter(inputData):

    map = inputData in filter

    print('this is the data to be converted into a bloomfilter'.format(inputData, map))
    print('H3llo, {}'.format(inputData))

#iteratively populate bloomfilter

def addToFilter(inputData):
    filter.add(inputData)
    print('Format input data: ')
    print(format(inputData))
    print('')
    
for inputData in ['Hannah', 'Eric']:
    generateFilter(inputData)
    addToFilter(inputData)
'''

# In the paper, multi-sets are  converted into sets
# single data set to be translated into bloom-filter, Sn denotes multiple sets
S = ['entry one', 'entry two', 'entry three', 'entry four', 'entry five', 'entry six']

# Instantiate bloom-filter, Ld denotes bloom-filters
L = BloomFilter(max_elements=1000, error_rate=0.01)


arr = []

# Populate Bloom-filter with data
for inputData in S:
    filter.add(inputData)
    map = inputData in filter
    arr.append(map)

print(arr)

