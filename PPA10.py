def number_grid(m, n):
    """
    Write a number grid to a file

    Arguments:
        m, n: positive integers
    Return:
        None
    """
    c=0
    line=''
    with open('numgrid.csv','w') as outfile:
        for i in range(m):
            for j in range(n):
                c=c+1
                line=line+str(c)
                if j==n-1:
                    continue
                else:
                    line=line+','
            line=line+'\n'
            
        outfile.write(line)
                
