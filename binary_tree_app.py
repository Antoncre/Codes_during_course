from node import Node
from binary_tree import Tree

tree = Tree(Node(12))
tree.add(Node(9))
tree.add(Node(2))

tree.inorder()
print('pause')
tree.preorder()
print(tree.find(2))
