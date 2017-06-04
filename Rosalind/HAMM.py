file = open("rosalind_hamm.txt","r")

one = file.readline()
#print "#1 = ", one
#print "len one = " , len(one)

second = file.readline()
#print "#2 = ", second
#print "len second = " , len(one)

hammingDist = 0

for i in range(len(one)):
   if(one[i] != second[i]):
       hammingDist += 1
    
print hammingDist

file.close()        