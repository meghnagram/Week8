def get_freq(filename):
    f = open(filename, 'r')
    freq = dict()
    for line in f:
        word = line.strip()
        if word not in freq:
            freq[word] = 0
        freq[word] += 1
    f.close()
    return freq


# Another Approach
# def get_freq(filename):
#     """
#     Extract frequency information from the file

#     Argument:
#         filename: string, path to file
#     Return:
#         result: dictionary; keys are strings, values are integers
#     """
    
#     d={}
    
#     with open(filename,'r') as infile:
#         for line in infile:
#             if line.strip() not in d.keys():
#                 d[line.strip()] =1
#             else:
#                 d[line.strip()] +=1
#     return d
