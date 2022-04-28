from BinarySearchTree import BinarySearchTree
from BSTNode import BSTNode
from RBTNode import RBTNode
from RedBlackTree import RedBlackTree

def main():
    rbt = RedBlackTree()
    A = [27,1,6,-54,22,34,30,132,0]
    B = [13,15,7,6,2,20,18,1,9,52]
    C = [10,9,8,7,6,5,4,3,2,1]
    for x in C:
        rbt.rbInsert(RBTNode(x))
        rbt.inOrderWalk()
        print("--------")
    found, node = rbt.recursiveSearch(9)
    children = node.getChildren()
    children[0].print()
    children[1].print()
    node.getFather().print()

if __name__ == '__main__':
    main()
