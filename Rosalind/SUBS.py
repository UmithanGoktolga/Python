#CUG, 10 April

file = open("rosalind_subs.txt", "r")

DNA = file.readline().strip("\n")
subDNA = file.readline().strip("\n")

print DNA
print subDNA


for i in xrange(0,len(DNA)-len(subDNA)):
    if(DNA[i:(i+len(subDNA))] == subDNA):
        print i+1,

file.close()
