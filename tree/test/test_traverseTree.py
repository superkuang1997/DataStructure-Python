from binaryTreeV2 import BinaryTree

t = BinaryTree(0)
t.insertLeft(4)
t.insertLeft(3)
t.insertLeft(5)
t.insertRight(4)
t.insertRight(56)

print("---preorder---")
t.preorder(t)
print("---inorder---")
t.inorder(t)
print("---postorder---")
t.postorder(t)