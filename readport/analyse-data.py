import numpy as np
import matplotlib.pyplot as plt

Tmp = []
AcX = []
AcY = []
AcZ = []
GyX = []
GyY = []
GyZ = []
Snd = []

dictIdent = {
        'Tmp':'T',
        'AcX':'X',
        'AcY':'Y',
        'AcZ':'Z',
        'GyX':'x',
        'GyY':'y',
        'GyZ':'z',
        'Snd':'s',
        'End':'e'}
#set up a dictionary with values
dictVars = dict()
for key in dictIdent:
    dictVars[key] = []

#set up a separators dictionary
dictSep = dict()
for key in dictIdent:
    dictSep[key] = 0
    
dictIdentRev = dict()
for key in dictIdent:
    dictIdentRev[dictIdent[key]] = key


#open a file for input
file = open('output6.txt', mode='r')

"""
#iterate through file
for line in file:
    #if the first letter in line is T, then it is a "temperature line"
    if line[0] == 'T':
        templine = True
    #if the first letter in line is x, then it's a gyro line
    elif line[0] == 'x':
        templine = False
    #else, the message is missing the beginning
    else:
        templine = None
    
    if templine:
            
        for k in range(len(line)):
#            if line[k] in dictIdentRev:
#                var = dictIdentRev[line[k]]
#                dictSep[var] = k
            if line[k] == 'T':
                tempsep = k
            elif line[k] == 'X':
                acxsep = k
            elif line[k] == 'Y':
                acysep = k
            elif line[k] == 'Z':
                aczsep = k
            elif line[k] == 'e':
                end = k
#        for var in dictSep:
#            dictVars[var].append(line[dictSep])
        Tmp.append(line[tempsep+1:acxsep])
        AcX.append(line[acxsep+1:acysep])
        AcY.append(line[acysep+1:aczsep])
        AcZ.append(line[aczsep+1:end])
        
    elif not templine:
        for k in range(len(line)):
            
            if line[k] == 'x':
                gyxsep = k
            elif line[k] == 'y':
                gyysep = k
            elif line[k] == 'z':
                gyzsep = k
            elif line[k] == 's':
                sndsep = k
            elif line[k] == 'e':
                end = k
        GyX.append(line[gyxsep+1:gyysep])
        GyY.append(line[gyysep+1:gyzsep])
        GyZ.append(line[gyzsep+1:sndsep])
        Snd.append(line[sndsep+1:end])
    
variables = [Tmp, AcX, AcY, AcZ, GyX, GyY, GyZ, Snd]

for var in variables:
    for entry in var:
        if entry == '':
            var.remove(entry)
            
Tmp = np.array(Tmp, dtype = float)

AcX = np.array(AcX, dtype = float)
AcY = np.array(AcY, dtype = float)
AcZ = np.array(AcZ, dtype = float)
GyX = np.array(GyX, dtype = float)
GyY = np.array(GyY, dtype = float)
GyZ = np.array(GyZ, dtype = float)
Snd = np.array(Snd, dtype = float)

plt.plot(AcZ)

"""

dictRevSep = {
        's':Snd,
        'X':AcX,
        'Y':AcY,
        'Z':AcZ,
        'x':GyX,
        'y':GyY,
        'z':GyZ,
        'T':Tmp}

dictRevSep = {
        's':[],
        'X':[],
        'Y':[],
        'Z':[],
        'x':[],
        'y':[],
        'z':[],
        'T':[]}

#iterate through the file
for line in file:
    
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
                #if it is not a number, then take the previous characters
                else:    
                    entries.append(line[prev:i])
                    prev = i
                #increment the current position    
                i += 1
        except IndexError:
            endOfLine = True

    for j in entries:
        try:

            if j[0] in dictRevSep:
                var = dictRevSep[j[0]]
               
                dictRevSep[j[0]].append(j[1:])
        except IndexError:
            pass

for k in dictRevSep:
    dictRevSep[k] = np.array(dictRevSep[k], dtype = float)

#print(dictRevSep['T'])
plt.plot(dictRevSep['Z'])
#
#data = open('output.txt', mode='r')
#
#temp = []
#acx = []
#acy = []
#acz = []
#
#i = 0
#
#for line in data:
#    if i%4 == 1:
#        temp.append(line)
#    elif i%4 == 2:
#        acx.append(line)
#    elif i%4 == 3:
#        acy.append(line)
#    elif i%4 == 0:
#        acz.append(line)
#    else:
#        raise RuntimeError()
#    i += 1
#    
#data.close()
#
#T = np.array(temp)
#AcX = np.array(acx)
#AcY = np.array(acy)
#AcZ = np.array(acz)
#
#"""
#f1, (ax11, ax12) = plt.subplots(1,2, sharey = True)
#
#ax11.plot(T1)
#ax11.set_ylim((20,30))
#ax12.plot(T2)
#
#plt.show()
#
#f2, (ax21, ax22) = plt.subplots(1,2, sharey=True)
#
#ax21.plot(AcX1)
#ax22.plot(AcX2)
#plt.show()
#
#f3, (ax31, ax32) = plt.subplots(1,2,sharey=True)
#
#ax31.plot(AcY1)
#ax32.plot(AcY2)
#plt.show()
#
#f4, (ax41, ax42) = plt.subplots(1,2,sharey=True)
#
#ax41.plot(AcZ1)
#ax42.plot(AcZ2)
#plt.show()
#
#print(AcZ2.min())
#print(AcZ1.min())
#"""
