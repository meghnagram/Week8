def read_line(filename, n):
    """
    Read the nth line of the file

    Argument:
        filename: string, name of the file to be read
    Return:
        string: return nth line of the file
    """
    c=0
    with open(filename,'r') as file:
        
        for line in file:
            c +=1
            if c==n:
                return line
    return None
