
file = open("rosalind_ini5.txt", "r+")

fileR = open("result_ini5.txt", "w")
cntr = 1
for line in file:
    if(cntr % 2 == 0):
        print line,
        fileR.write(line)
    cntr +=1
        
               
file.close()
fileR.close()