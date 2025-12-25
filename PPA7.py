def add_period(filename):
    """
    Add a period at the end of each line

    Argument:
        filename: string; path of the file
    Return:
        None
    """
    
    with open(filename,'r') as infile, open('out.txt','w') as outfile:
        for line in infile:
            line=line.rstrip('\n')
            outfile.write(line+ '.' + '\n')
