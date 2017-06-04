file = open("rosalind_revc.txt", "r")

string = file.read()

listS = list(string)

listS.reverse()

for i in range(len(listS)):
    if(listS[i] == 'A'):
        listS[i] = 'T'
    elif(listS[i] == 'T'):
        listS[i] = 'A'
    elif(listS[i] == 'C'):
        listS[i] = 'G'
    elif(listS[i] == 'G'):
        listS[i] = 'C'

newStr = ''.join(listS)

print newStr

file.close()
    