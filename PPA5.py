def get_matrix(filename):
    """
    Convert the contents of the file into a matrix

    Argument:
        filename: string
    Return:
        matrix: list of lists
    """
    
    matrix=[]
    with open(filename,'r') as file:
        for line in file:
            row=[int(x) for x in line.strip().split(',')]
            matrix.append(row)
            
    return matrix
