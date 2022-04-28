import threading

from BinarySearchTree import BinarySearchTree
from BSTNode import BSTNode
from RBTNode import RBTNode
from RedBlackTree import RedBlackTree
from timeit import default_timer as timer
import sys


# def main():
#     rbt = RedBlackTree()
#     A = [27,1,6,-54,22,34,30,132,0]
#     B = [13,15,7,6,2,20,18,1,9,52]
#     C = [10,9,8,7,6,5,4,3,2,1]
#     for x in C:
#         rbt.rbInsert(RBTNode(x))
#         rbt.inOrderWalk()
#         print("--------")
#     found, node = rbt.recursiveSearch(9)
#     children = node.getChildren()
#     children[0].print()
#     children[1].print()
#     node.getFather().print()

def main():
    #caso peggiore: arrivo dei valori ordinati in ordine crescente (sarebbe analogo con ordine decrescente)
    bst = BinarySearchTree()
    for x in range (1,960,1):
        bst.insert(BSTNode(x))
    start = timer()
    bst.insert(BSTNode(961))
    end = timer()
    print(end-start)
    print (" seconds needed")

    rbt = RedBlackTree()
    for x in range (1,960,1):
        rbt.rbInsert(RBTNode(x))
    start = timer()
    rbt.rbInsert(BSTNode(961))
    end = timer()
    print(end-start)
    print (" seconds needed")



if __name__ == '__main__':
    #sys.setrecursionlimit(1000)
    #threading.stack_size(2000000)
    #thread = threading.Thread(target=main())
    #thread.start()
    main()
