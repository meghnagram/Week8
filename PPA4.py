def get_dict(filename):
    """
    Convert the contents of the file into a dict

    Argument:
        filename: string, path of the file
    Return:
        result: dict; keys are strings, values are integers
    """
    
    student={}
    
    with open(filename,'r') as file:
        next(file) #ignores first line
        for line in file:
            name,age=line.strip().split(',')
            student[name] = int(age)
            
    return student
