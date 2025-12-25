def extract_lines(filename):
    """
    Get all males who have scored at least 70 marks in Python
    
    Argument:
        filename: string
    Return:
        None
    """
    
    with open(filename,'r')as infile, open('python.csv','w') as outfile:
        next(infile) #ignores first 
        outfile.write('SeqNo,Name,Gender,CT,Python,PDSA\n')
        
        for line in infile:
            parts=line.strip().split(',')
            seq,name,sex,CT,py,pdsa=parts
            
            if sex=="M" and int(py)>=70:
                newline=f"{seq},{name},{sex},{CT},{py},{pdsa}"
                outfile.write(newline+ '\n')
