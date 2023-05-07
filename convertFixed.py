import pandas

def convertFixed(filename):
    """Converts a BLAST .txt fixed-with file (downloaded as 'Text' option) to a tab-delimited file.
    
    Parameter:
        filename:   Name of fixed-width file to be converted to tab-delimited
    
    Return value:   None; new file will be written as 'filename_tab.txt' to current directory
    """
    file = pandas.read_fwf(filename, header = None, skiprows = 9, infer_nrows = 100,
        names = ['Description',
                'Scientific Name', 
                'Common Name', 
                'Taxid', 
                'Max score',
                'Total score',
                'Query cover',
                'E value',
                'Per. Ident',
                'Acc. Len',
                'Accession'])
    file.to_csv(filename[:-4] + '_tab.txt', sep = '\t', index = None)