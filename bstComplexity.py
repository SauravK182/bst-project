import time
import random
import matplotlib.pyplot as pyplot
from bst import *
from bst_recursive import *

def bstComplexity():
    """Tests the time complexity of creating and sorting a BST."""
    # Initialize random list of {key: value} pairs and bst
    randList = [(random.random(), random.random()) for n in range(200000)]
    sliceSize = [20000 * 2 ** i for i in range(4)]
    bst = [ ]
    
    # Get list of keys from randList, shuffle list
    keys = [ ]
    for entry in randList:
        keys.append(entry[0])
    random.shuffle(keys)
    
    # For each of the 4 slice sizes:
    #   - create a BST of the given size
    #   - sort the BST
    #   - time the entire process
    times = [ ]
    for num in sliceSize:
        listForBst = randList[:num]
        begin = time.time()
        for entry in listForBst:
            insert(bst, entry[0], entry[1])
        bstSort(bst)
        end = time.time()
        times.append(end - begin)
    print(times)
    
    # Plot times vs. size of list
    pyplot.plot(sliceSize, times)
    pyplot.xlabel("Size of list to create and sort BST")
    pyplot.ylabel("Time (s)")
    pyplot.show()

bstComplexity()