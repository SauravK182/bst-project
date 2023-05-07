from bst_blast import *

KEY = 0
LEFT = 1
RIGHT = 2

# An extended representation for a BST node is given as follows:
# [{key: value}, [{left node: value}], [{right node: value}]]
    # key is the root of the subtree
    # left is the left child node
    # right is the right child node
# If there is no left or right node, its value is [ ]

def insertRecursive(root, key, value):
    """Insert a new key into the BST with the given root via a recursive algorithm.

    Parameters:
        root:   a list representing the BST
        key:    the key to insert
        value:  the value to assign to the associated key  
    
    Return value: None
    """
    if root == [ ]:
        root.extend([{key: value}, [ ], [ ]])
        return
    
    keyValPair = root[KEY]
    nodeKey = next(iter(keyValPair))

    if key <= nodeKey:
        insertRecursive(root[LEFT], key, value)
    else:
        insertRecursive(root[RIGHT], key, value)


def searchRecursive(root, key):
    """Search for a target key recursively in the BST with the given root.

    Parameters:
        root: a list representing the BST
        key: the key to search for

    Return value: the value associated with the key, or None if the key is not in the BST
    """
    if root == [ ]:
        return None
    
    keyValPair = root[KEY]
    nodeKey = next(iter(keyValPair))

    if key < nodeKey:
        return searchRecursive(root[LEFT], key)
    elif key > nodeKey:
        return searchRecursive(root[RIGHT], key)
    else:
        return root[KEY][nodeKey]

def bstSort(root):
    """Sort an extended BST recursively based on its nodes.
    
    Parameter:
        root:   A list representing a BST
    
    Return value:   List of sorted nodes
    """
    if root == [ ]:
        return [ ]

    keyValPair = root[KEY]
    nodeKey = next(iter(keyValPair))
    
    return bstSort(root[LEFT]) + [nodeKey] + bstSort(root[RIGHT])


def main():
    bst = blastToBST("hemoglobinB.txt", "species-alignment-HB.txt", 100)
    test = bstSort(bst)
    assert (test[i] < test[i + 1] for i in range(len(test) - 1))
    print("Passed test!")

if __name__ == '__main__':
    main()