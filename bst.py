KEY = 0
LEFT = 1
RIGHT = 2

# An extended representation for a BST node is given as follows:
# [{key: value}, [{left node: value}], [{right node: value}]]
    # key is the root of the subtree
    # left is the left child node
    # right is the right child node
# If there is no left or right node, its value is [ ]

def insert(root, key, value):
    """Insert a new key into the BST with the given root.

    Parameters:
        root:   a list representing the BST
        key:    the key to insert
        value:  the value to assign to the associated key  
    
    Return value: None
    """
    current = root
    while current != [ ]:
        keyValPair = current[KEY]           # current[KEY] is a single-key dictionary of the form {key: value}
        nodeKey = next(iter(keyValPair))    # use next(iter()) to get the key from dictionary
        if key <= nodeKey:
            current = current[LEFT]
        else:
            current = current[RIGHT]
    current.extend([{key: value}, [ ], [ ]])

def search(root, key):
    """Search for a target key in the BST with the given root.

    Parameters:
        root: a list representing the BST
        key: the key to search for

    Return value: the value associated with the key, or None if the key is not in the BST
    """
    current = root
    keyValPair = current[KEY]
    nodeKey = next(iter(keyValPair))            # initialize nodeKey

    while nodeKey != key:                       # while we haven't reached desired node
        if key < nodeKey:
            current = current[LEFT]
        else:
            current = current[RIGHT]
        if current != [ ]:                      # if current non-empty, continue; else, stop
            keyValPair = current[KEY]
            nodeKey = next(iter(keyValPair))
        else:
            return None
    return current[KEY][nodeKey]                     # if we have reached this code, we have found desired key