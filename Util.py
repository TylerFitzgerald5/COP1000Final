##These are Utility functions used in pokemon.py
##They are for altering string values to extract important information from lines



#Pipe cuts and returns everything after the pipe
#Can be called multiple times using reps. Defaults to 1
def PCutAfter(input, reps = 1):
    output = input
    for i in range(reps):
        index = output.find("|") + 1
        output = output[index:]
    return output

#Pipe cuts and returns everything before the pipe
def PCutBefore(input):
    index = input.find("|")
    return input[:index]