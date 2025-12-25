def read_file(filename):
    """
    Read the file and print each line

    Argument:
        filename: string, name of the file to be read
    Return:
        None
    """
    
      
    with open(filename,'r') as file: # with- file will close for sure
        for line in file:
            print (line.rstrip()) #no space at end
