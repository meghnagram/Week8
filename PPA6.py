def write_AP(a_1, d, n):
    """
    Write the AP to a file

    Arguments:
        a_1: first term, integer
        d: common difference, integer
        n: number of terms, integer
    Return:
        None
    """
    
    with open('out.txt','w') as file:
        for i in range(n):
            term = a_1+i*d 
            file.write(str(term)+'\n')
