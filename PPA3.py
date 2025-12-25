def get_max_line(filename):
    """
    Get the line that houses the maximum value

    Argument:
        filename: string, path to the file
    Return:
        result: integer
    """
    
    with open(filename,'r') as file:
        max_value= None
        max_line_number=0
        line_number=0
        
        for line in file:
            line_number +=1
            value=int(line.strip())
            
            if max_value == None or value> max_value:
                max_value=value
                max_line_number=line_number
        return max_line_number
