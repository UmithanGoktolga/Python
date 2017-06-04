
file = open("rosalind_gc.txt","r")


ID = []
perc = [0,0,0,0,0,0,0,0,0,0]
DNA = 'a'
cntr = -1

#cntrLine = 1
for line in file:
    if(line[0] == ">"):
        #print "G+C SAYISI = " , perc[cntr]
        
        perc[cntr] = (perc[cntr] * 100) / float(len(DNA))
        #cntrLine = 0
        DNA = ''
        #print "Yeni bi label" 
        ID.append(line.strip("\n").strip(">")) 
        cntr += 1
    else:
        #cntrLine += 1
        #print "Line " ,line
        
        DNA += line.strip("\n")
        #print "DNA =   " , DNA
        
        Gs = line.count("G")    
        #print "G sayisi = " , Gs
         
        Cs = line.count("C")
        #print "C sayisi = " , Cs
        
        #perc[cntr] += ((Gs+Cs) * 100) / float(len(line))
        #print ((Gs+Cs) * 100) / float(len(line))
        perc[cntr] += (Gs+Cs) 
        #print "Else G+C SAYISI = " , perc[cntr]

perc[cntr] = (perc[cntr] * 100) / float(len(DNA))   
        

print ID
print perc
#print perc.index(max(perc))
print ID[perc.index(max(perc))]
print "%.6f" % max(perc)

file.close()