from BinarySearchTree import BinarySearchTree
from BSTNode import BSTNode
from RBTNode import RBTNode
from RedBlackTree import RedBlackTree

def main():
    rbt = RedBlackTree()
    A = [27,1,6,-54,22,34,30,132,0]
    for x in A:
        rbt.rbInsert(RBTNode(x))
        rbt.inOrderWalk()
        print("--------")
if __name__ == '__main__':
    main()
