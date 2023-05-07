from bst_blast import *
from bst_recursive import *

def queryBLAST(bst):
    """An interactive query for a BST created from downloaded BLAST data for a given gene or protein.
    
    Parameter:
        bst:        A list representation of a binary search tree, where nodes are represented as {key: value} pairs.
    
    Return value:   None. Will continue to prompt for a query based on genus to present BLAST information until user quits.
    """
    key = input("Please enter a genus or species name to begin (e.g. Homo). Type 'q' to quit, or type 'keys' to see a list of all possible data identifiers: ")
    species = bstSort(bst)
    while key != 'q':
        if key == 'keys':
            print('\n'.join(species))
        else:
            keyBST = ''
            for entry in species:                   # Downloaded species names cuts off in file; adjust query key for this to avoid error
                if (entry.lower() in key.lower()) or (key.lower() in entry.lower()):
                    keyBST = entry
            values = searchRecursive(bst, keyBST)
            if values != None:                      # If key exists in BST
                numAccession = int(len(values) / 5) # BST stores accession + 4 other attributes per accession
                if numAccession > 1:                # if there is more than one associated accession
                    accessions = [str(i + 1) + ') ' + values[5 * i] + '\n' for i in range(numAccession)]
                    print("There is more than one accession associated with " + key + " for this data:" + '\n' +
                        ''.join(accessions) + 
                        "Each accession represents a distinct isoform for the gene. ")
                    flag = input("Please pick an accession to examine using the numbers 1 through " +
                                str(numAccession) + ". " "Type 'all' to view all simultaneously: ")
                    try:
                        flag = int(flag)
                    except ValueError:
                        pass
                    while flag != "all" and flag not in list(range(1, numAccession + 1)):      # if flag is not one of the presented options
                        flag = input("Please use the provided numbers to view data for an accession, or type 'all' to view all simultaneously: ")
                        try:
                            flag = int(flag)
                        except ValueError:
                            pass
                    if flag == 'all':
                        isoformIndex = [5 * i for i in range(numAccession)]
                    else:
                        isoformIndex = [5 * (int(flag) - 1)]
                else:
                    isoformIndex = [0]    
                for index in isoformIndex:          # Print information for user
                    print('\n' + "Organism (genus or species): " + key + '\n' +
                        "Accession code: " + values[index] + '\n' +
                        "Percent sequence identity: " + values[index + 1] + '\n' + 
                        "Number of mismatches between sequences: " + values[index + 2] + '\n' + 
                        "Number of gap opens between sequences: " + values[index + 3] + '\n' + 
                        "Expect value (measure of statistical significance): " + values[index + 4] + '\n')
            else:
                print("Sequence similarity associated with the desired genus or species was not found. Please try again.")
        key = input("Please enter a genus or species name to begin (e.g. Homo). Type 'q' to quit, or type 'keys' to see a list of all possible data identifiers: ")

def main():
    bst = blastToBST("hemoglobinB.txt", "species-alignment-HB.txt", 100)
    queryBLAST(bst)

if __name__ == '__main__':
    main()