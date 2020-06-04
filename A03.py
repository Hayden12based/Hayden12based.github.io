


from math import sqrt , pow
from NC_045512 import sars_cov_2
from NC_004718 import sars_cov_1
from MH708124 import pig_cov
from KU182963 import bat_cov
from NC_001802 import HIV

viruses=[sars_cov_2,sars_cov_1,pig_cov,bat_cov,HIV]
names=["sars_cov_2","sars_cov_1","pig_cov","bat_cov","HIV"]


def count_of_nucleic_acid ( seq , base ):
    
    count=0
    for letter in seq:
        if letter == base:
            count=count+1
    return count

def distance_similarity ( seq1 , seq2 ):
    
    index = 0                                                       
    dist = 0  
    length = len(seq1) if len(seq1) < len(seq2) else len(seq2)      
                                                                    
    while index < length:   
                                                
        if ((seq1[index] =='T' and seq2[index]=='A') or (seq1[index] =='A' and seq2[index]=='T')) or ((seq1[index] =='T' and seq2[index]=='G') or(seq1[index] =='G' and seq2[index]=='T') ) or ((seq1[index] =='A' and seq2[index]=='C') or (seq1[index] =='C' and seq2[index]=='A')) or ((seq1[index] =='C' and seq2[index]=='G') or (seq1[index] =='G' and seq2[index]=='C')) :                              
            dist += 1 
        elif ((seq1[index] =='T' and seq2[index]=='C') or (seq1[index] =='C' and seq2[index]=='T')) or ((seq1[index] =='A' and seq2[index]=='G') or (seq1[index] =='G' and seq2[index]=='A')):   
             dist += 10
       
        index += 1   

    distance=dist / length  
  
    return distance


def match_coeff ( seq1 , seq2 ):
  
    index = 0                                                       
    score = 0                                                       
                                                                    
    length = len(seq1) if len(seq1) < len(seq2) else len(seq2)      
                                                                    
    while index < length:                                           
        if seq1[index] != seq2[index]:                              
            score += 1                                              
        index += 1                                                  
    return score / length    

def print_virus_characteristics ( seq ):
 
    sequencelength=len( seq )

    A= (count_of_nucleic_acid(seq,'A')/ sequencelength)*100
    T= (count_of_nucleic_acid(seq,'T')/ sequencelength ) *100
    G= (count_of_nucleic_acid(seq,'G')/ sequencelength) *100
    C= (count_of_nucleic_acid(seq,'C')/ sequencelength) *100
    AT = (A+T)
    GC = (G+C)
    gcContent = ((G+C)/ sequencelength)*100
    atgc_ratio = (A+T) / (G+C)
   
    print("Total length: ",len( seq ))

    print ("A: {0:.2f}".format(A),"%","G: {0:.2f}".format(G),"%" )
    print ("T: {0:.2f}".format(T),"%","C: {0:.2f}".format(C) ,"%" )
    print ("AT%: {0:.2f}".format(AT),"%","GC: {0:.2f}".format(GC) ,"%" )
    print("")
    print ("A/T Ratio: {0:.2f}".format(A/T),"  ","G/C Ratio: : {0:.1f}".format(G/C) )
    print ("gcContent: {0:.2f}".format(gcContent),"  ","AT/GC Ratio:  {0:.1f}".format(atgc_ratio) )


while True :
    run = input ("Do you want to compare two virus genomes ?\
    \ nPress enter to continue , or any key to exit .")
    if run !="":
        print (" goodbye ")   
        break

    print ("\ nChoose two sequences to compare ")
    print (" Sequences available are \
    \ nsars_cov_2 \t (1)\ nsars_cov_1 \t (2)\ npig_cov \t\t (3)\ n\
    \ bat_cov \t\t (4)\ nHIV \t\t(5)")
    seq1 = int( input (" Enter the first sequence number (1 ,2 ,3 ,4 , or 5): "))
    seq2 = int( input (" Enter the second sequence number (1 ,2 ,3 ,4 , or 5): "))
    if( seq1 not in [1 ,2 ,3 ,4 ,5] or seq2 not in [1 ,2 ,3 ,4 ,5]):
        print (" Incorrect sequence number :")
        continue
    similarity=distance_similarity(viruses[seq1-1],viruses[seq2-1])
    coeff=match_coeff(viruses[seq1-1],viruses[seq2-1])
 
    print("_________________________")
    print(names[seq1-1]," vs ",names[seq2-1])
    print("_________________________")
    print("")

    if(similarity==0):
        print("Similarity: {0:.2f}".format(similarity))
        print("The sequences are the same")
    else:
        print("Similarity: {0:.2f}".format(similarity))
        print("Match Coeff: {0:.3f}".format(coeff))

    print("********************************")
    print("Metrics sequence 1 - ",names[seq1-1])
    print("********************************")
    print_virus_characteristics(viruses[seq1-1])
    print("")
    print("********************************")
    print("Metrics sequence 2 - ",names[seq2-1])
    print("********************************")
    print_virus_characteristics(viruses[seq2-1])

    

