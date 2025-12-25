def improvement(filename):
    """
    Find all students who have shown an improvement
    
    Argument:
        filename: string, path to file
    Return: 
        count: integer
    """
    n=0
    with open(filename,'r') as file:
        next(file)
        
        for line in file:
            parts=line.strip().split(',')
            if len(parts)!=5:
                continue
            _ , _, ct,python,pdsa = parts
            ct,python,pdsa =int(ct),int(python),int(pdsa)
            if ct<python<pdsa:
                n+=1
                
    return n
