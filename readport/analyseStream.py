"""Aim to use this script as a real-time decoder, which takes in one line
of input and returns the values of respective variables.""" 




#set up the empty dictionaries
def initialiseDict():
    dictIdent = {
            'T':'Tmp',
            'X':'AcX',
            'Y':'AcY',
            'Z':'AcZ',
            'x':'GyX',
            'y':'GyY',
            'z':'GyZ',
            's':'Snd',
            'e':'End'}
    
    #set up a dictionary with values
    dictVars = dict()
    for key in dictIdent:
        dictVars[dictIdent[key]] = []
    
    return dictIdent, dictVars
 


#open a file for input
file = open('output6.txt', mode='r')



#function takes in one line of coded message
#and returns dictionary of decoded variables    

def loop(line, dictIdent, dictVars):
    
    endOfLine = False
    prev = 0
    i = 0
    entries = []
    
    while endOfLine == False:     
        #this try is valid until end of line    
        try:  
            char = line[i]
            #this try checks if the character is a number
            try:
                #if it is a number, then increment the number of characters taken
                n = int(char)
                i += 1
            except ValueError:
                #if it's a minus sign, do the same thing
                if char == '-':
                    pass
                #if it is not a number, then take the characters up to the current position
                else:    
                    entries.append(line[prev:i])
                    prev = i
                #increment the current position    
                i += 1
        except IndexError:
            endOfLine = True
    #now decode each entry according to the first character        
    for j in entries:
        try:

            if j[0] in dictIdent:
                var = dictIdent[j[0]]
                try:
                    dictVars[var].append(int(j[1:]))
                #if conversion to integer fails, then pass    
                except:
                    pass
        #if j is '' then IndexError, so pass        
        except IndexError:
            pass

