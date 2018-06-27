import numpy as np
import matplotlib.pyplot as plt

a1 = np.fromfile('output4.txt', sep='\n')


T1 = a1[0:-1:4]
AcX1 = a1[1:-1:4]
AcY1 = a1[2:-1:4]
AcZ1 = a1[3:-1:4]

a2 = np.fromfile('output5.txt', sep='\n')


T2 = a2[0:-1:4]
AcX2 = a2[1:-1:4]
AcY2 = a2[2:-1:4]
AcZ2 = a2[3:-1:4]


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

f1, (ax11, ax12) = plt.subplots(1,2, sharey = True)

ax11.plot(T1)
ax11.set_ylim((20,30))
ax12.plot(T2)

plt.show()

f2, (ax21, ax22) = plt.subplots(1,2, sharey=True)

ax21.plot(AcX1)
ax22.plot(AcX2)
plt.show()

f3, (ax31, ax32) = plt.subplots(1,2,sharey=True)

ax31.plot(AcY1)
ax32.plot(AcY2)
plt.show()

f4, (ax41, ax42) = plt.subplots(1,2,sharey=True)

ax41.plot(AcZ1)
ax42.plot(AcZ2)
plt.show()

print(AcZ2.min())
print(AcZ1.min())