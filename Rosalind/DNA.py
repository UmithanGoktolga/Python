file = open("rosalind_dna.txt", "r")

string = file.read()

print type(string)

cntrA = 0
cntrC = 0
cntrG = 0
cntrT = 0
for char in string:
    if(char == 'A'):
        cntrA += 1
    elif(char == 'C'):
        cntrC += 1
    elif(char == 'G'):
        cntrG += 1
    elif(char == 'T'):
        cntrT += 1

print "%d %d %d %d" % (cntrA,cntrC,cntrG,cntrT)

file.close()
    