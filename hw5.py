#Chengbin Hu done
#06/24/2014
from urllib2 import urlopen, URLError

def fetch_uniprot(uniID):
    """
    https://docs.python.org/2/tutorial/errors.html
    https://docs.python.org/2/library/urllib2.html
    
    Description: Given a uniprot ID, goes to uniprot.org, fetches the fasta entry

    inputs:
        uniID: uniprot ID as a string
        
    returns: fasta entry (file object) or, if there is an error in retrieval, return False
    """
    url = "http://www.uniprot.org/uniprot/" + uniID + ".fasta"
    try:
        fasta = urlopen(url)
        return fasta
    except URLError as e:
        print "Error: ", e, " ", uniID
        return False    


def get_uni_seq(fasta):
    """
    Description: given a single fasta entry as a file object, return the sequence
    without newline characters, and the uniprot ID. 
    
    inputs:
        fasta: a file object with one fasta entry
        
    returns: 
        seq: the amino acid sequence without new line characters
        uni: the uniprot ID
    """
    if fasta: #no need to do anything if fasta is false
        fasta_list = fasta.readlines()
        uni = fasta_list[0][4:10]
        seq = ''
        for i in range(1, len(fasta_list)):
            seq = seq + fasta_list[i].strip()
        return uni, seq
        

def index_calc(AAstring):
    """
    TO DO: Write this function! 
    - Do not use the same AAind used in the example.
    - make sure you return both the final value AND the AAind dictionary
    
    Description: Given an amino acid string, calculate the sum of the associated 
    amino acid values, and then calculate the average (divide by the length of 
    the protein).
    
    example:
    example_AAstring = 'MCDE'
    AAind = {'A': -0.591, 'C': -1.343, 'D': 1.05, 'E': 1.357, 
    'F': -1.006, 'G': -0.384, 'H': 0.336,'I': -1.239, 'K': 1.831, 
    'L': -1.019, 'M': -0.663, 'N': 0.945, 'P': 0.189, 'Q': 0.931, 
    'R': 1.538, 'S': -0.228, 'T': -0.032, 'V': -1.337, 'W': -0.595, 
    'Y': 0.26, '-': 0}
    return (-0.591 + -1.343 + 1.05 + 1.357)/4, AAind
    
    inputs:
        AAstring: an amino acid string with no newline characters
        
    returns:
        avg_ind:
            The sum of the amino acid values divided by the length (a float value)
        AAind: 
            A dictionary containing the amino acid indices
    
    """
    total_value = 0.0
    AAindex = {'A': 0.357, 'C': 0.346, 'D': 0.511, 'E': 0.497, 
    'F': 0.314, 'G': 0.544, 'H': 0.323,'I': 0.462, 'K': 0.466, 
    'L': 0.365, 'M': 0.295, 'N': 0.463, 'P': 0.509, 'Q': 0.493, 
    'R': 0.529, 'S': 0.507, 'T': 0.444, 'V': 0.386, 'W': 0.305, 
    'Y': 0.420, '-': 0}#Entry: BHAR880101 Average flexibility indices (Bhaskaran-Ponnuswamy, 1988)
    for aa in AAstring:
        total_value+=AAindex[aa]#add each value of AAstring together
    return total_value/len(AAstring), AAindex
        

def fetch_index_calc(uniID):
    """
    TO DO: Write this function! 
    
    Description: Given a uniID, go to uniprot.org and fetch the sequence
    (you may use the functions fetch_uniprot and get_uni_seq or create your own).
    Once you have the sequence, Use index_calc to calculate the avg_ind.    
    
    inputs:
        uniID: A string which contains the uniprotID
        
    returns:
        avg_ind:
            The sum of the amino acid values divided by the length (a float value)
    """
    x= fetch_uniprot(uniID)
    if x:                       #if x is not false
        unid, sequ = get_uni_seq(x)
        avg_ind, di =index_calc(sequ)
        x.close() #I think we need to close file obj
        return avg_ind
def fetch_list_index_calc(ls):
    avg_ls=[]
    for items in ls: #every ID
        avg_ls.append(fetch_index_calc(items)) #append avg_ind to list
    return avg_ls
def fetch_organism(unids):
    orgms=[]
    for items in unids:
        x = fetch_uniprot(items)# open each fasta file from web as x
        if x:
            f=x.readlines() #read to f
            x.close()#close x
            orgms.append(f[0].split("_")[1].split()[0]) #the organism info is after first "_" and before a white space.
            #so we use f[0] get first line. split("_")[1] get the part after "_".split()[0] get the part before whitespace
    return orgms

def main():
    # An example for testing purposes. You should modify this!
    value, AAind = index_calc('LLLLLLLKTTWW')
    print value
    print AAind
    
    # some example uniprot IDs
    uniIDs = ['P13726', 'Q28198', 'P99029', 'badtest']
    id2= fetch_index_calc('Q28198')
    print id2
    lst=fetch_list_index_calc(uniIDs)
    print lst
    lst1=fetch_organism(uniIDs)
    print lst1
    # An example for iterating through a list of uniprot IDs
    #for uni in uniIDs:
     #   result = fetch_uniprot(uni)
      #  if result:
       #     uni, seq = get_uni_seq(result)
        #    print uni
         #   print seq            
    

if __name__ == '__main__':
    main()