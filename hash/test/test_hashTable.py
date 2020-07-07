from hashTable import HashTable

H = HashTable()
H[20] = 13
H[21] = 14
H[31] = 20
H[31] = 21
print(H[20])
print(H[21])
print(H[31])
print(len(H))
print(31 in H)
H.describe()