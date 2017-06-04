file = open("rosalind_rna.txt", "r")

string = file.read()

rnaList = list(string)

for i in range(len(rnaList)):
    if(rnaList[i] == 'T'):
        rnaList[i] = 'U'

rnaString = ''.join(rnaList)

print rnaString

file.close()

