def gp_to_fasta(gpfile):#transfer gp file to fasta function
    gp=open(gpfile,"r") #open gpfile first
    x=gp.readlines()   # read all the lines as a list
    title = ">" #title line begin with a >
    title = title+x[0].split()[1]+"|"+x[1][11:-2]+"\n" #the fasta file seems has one space before the definiation name so I use index 11 and there is no '.'in title. again all definition should be at 2nd line.
    for line in x: #this loop will find the sequence lines
        if line[:6]=="ORIGIN":
            start_line=x.index(line)+1#start line of sequence
        if line[:2]=="//":
            end_line=x.index(line)#end lines of sequence so x[start_line:end_line] will contain sequence information
    sque = x[start_line:end_line]
    Faseq=''
    for lines in sque:
        eachl = lines.split()#by test this split will delete the '\n'
        for s in range(len(eachl)):
            if s: #same as if s>0:
                Faseq=Faseq+eachl[s] #add every sequence except first number
        Faseq=Faseq+'\n'#sperate each line
    fastafile = title+Faseq.upper()#upper case all the sequence
    print fastafile
    with open("output.fasta", "w") as f:
        f.write(fastafile)
    
    
    
    
if __name__ == '__main__':
    gp_to_fasta("p21.gp")