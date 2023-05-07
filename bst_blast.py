from bst import *
from convertFixed import *

# BLAST Hit Data does not include species name
# Download normal .txt file (fixed-width formatting) to include species for each hit

def blastToBST(dataFile, speciesFile, numEntries, bst = [ ]):
    """Reads a .txt data file from the BLAST database into a BST.
    
    Parameter:
        dataFile:       Name of downloaded BLAST file in tab-separated format
        speciesFile:    Downloaded BLAST file containing species names for dataFile
        numEntries:     Number of entries to be read from dataFile
        bst (optional): Optional pre-existing binary search tree to add to; if no BST is passed, function will create and return a BST.
    
    Return values:      - BST of data, with species as identifiers. Satellite data includes E-value, % identity, and accession number(s).
                        - List of species names found in data
    """
    # Open data file and read each line
    hitFile = open(dataFile, 'r', encoding = 'utf-8')
    data = hitFile.readlines()
    hitFile.close()

    # Use convertFixed() to convert species file into tab-separated
    convertFixed(speciesFile)

    # Open species file and read each line
    suppFile = open(speciesFile[:-4] + '_tab.txt', 'r', encoding = 'utf-8')
    speciesTxt = suppFile.readlines()
    suppFile.close()

    # Read fields to determine column number of species name
    fields = speciesTxt[0].split('\t')
    numSci = fields.index("Scientific Name")

    # Read and save species from file
    species = [ ]
    for line in speciesTxt[1 : numEntries + 1]:
        lineSplt = line.split('\t')
        speciesName = lineSplt[numSci].replace('...', '')
        species.append(speciesName)
    
    # Parse data read from hitFile
    good = False
    j = 0
    while not good:
        if "hits found" in data[j]:     # line before data starts
            good = True
        j = j + 1
    data = data[j:]                     # keep only data
    data[:] = [line for line in data if line.strip() != '']     # remove empty lines

    # Extract data for each species
    counterDict = dict()
    indexOfInt = [1, 2, 4, 5, 10]       # column indices to keep for values
    for index in range(numEntries):
        dataSplit = data[index].split('\t')
        key = species[index]            # match species with sequence similarity data
        value = [dataSplit[i] for i in indexOfInt]
        if key not in counterDict:
            counterDict[key] = value
        else:
            counterDict[key].extend(value)
    
    # Add data to BST
    for organism in counterDict:
        insert(bst, organism, counterDict[organism])
    
    return bst