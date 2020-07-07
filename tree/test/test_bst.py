from binarySearchTree import BinarySearchTree

bst = BinarySearchTree()
bst[17] = 10
bst[5] = 4
bst[3] = 3
bst[11] = 1
bst[9] = 2
bst[16] = 3
bst[7] = 4
bst[8] = 5

print("before deletion:", bst[5])
print("len(bst):", len(bst))
del bst[5]
print("after deletion:", bst[5])
print("len(bst):", len(bst))

####################
print('-' * 30)
print('root.key:', bst.root.key)
for key in bst:
    print(key)