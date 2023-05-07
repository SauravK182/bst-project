from bst_blast import *

KEY = 0
LEFT = 1
RIGHT = 2

def bstPrint(bst):
    """Creates a list for printing a BST in the terminal.
    
    Parameter:
        bst:        A list representing a BST, where entries are {key: value} dictionaries
    
    Return value:   A list of elements in the BST, with indents equating to the level of depth in the tree at which they are found.
    """
    current = bst
    
    if current == [ ]:
        return [ ]
    
    keyValPair = current[KEY]
    nodeKey = next(iter(keyValPair))

    return [nodeKey] +  ['\t' + i for i in bstPrint(current[LEFT])] + ['\t' + i for i in bstPrint(current[RIGHT])]

def main():
    bst = blastToBST("hemoglobinB.txt", "species-alignment-HB.txt", 100)
    for entry in bstPrint(bst):
        print(entry)    

if __name__ == "__main__":
    main()