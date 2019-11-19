import time

# Note the 'SLC' code for each Amino Acid.
# You will simulate the effects of the Single Nucleotide Polymorphism that leads to this genetic disease.
# Write a function called ‘translate’ that, when given a DNA sequence of arbitrary length,
# the program identifies and returns the amino acid sequence of the DNA using the amino acid SLC code found in that table.
# There are many different amino acids, so this may get a bit repetitive. Just do the first five Amino Acids and make any other codon be printed as the amino acid 'X' . So basically,
# you would use an if - elif - elif .... else structure to translate each codon of DNA into the correct Amino Acid.
# Note that the program must be able to handle DNA sequences that are not of a length divisible by 3.

#Function to open input file and read its contents into the program
def read_file(filename) :
    content = ""
    ifile = open(filename, "r")
    for line in ifile :
        line = line.rstrip("\n")
        content += line
    ifile.close()
    return list(content)
 

def translate(dna_seq) :
    dna_seq = list(dna_seq) 
    slc_code = ""
    while len(dna_seq) > 0 : 
        if len(dna_seq) >= 3 : 
            codon = dna_seq[0:3]
          
         
            if codon == [ "A" , "T" , "T" ] or [ "A" , "T" , "C" ] or  [ "A" , "T" , "A" ] :
                slc_code += "I"
                del dna_seq[0:3]
            if codon == [ "C" , "T" , "T"] or [ "C" , "T" , "C" ] or [ "C" , "T" , "A" ] or [ "C" , "T" , "G"] or  [ "T" , "T" , "A" ] or  [ "T" , "T" , "G" ] :
                slc_code += "L"
                del dna_seq[0:3]
            if codon == [ "G" , "T" , "T" ] or [ "G" , "T" , "C" ] or [ "G" , "T" , "A" ] or  [ "G" , "T" , "G" ] :
                slc_code += "V"
                del dna_seq[0:3]
            if codon == [ "T" , "T" , "T" ] or [ "T" , "T" , "C" ] :
                slc_code += "F"
                del dna_seq[0:3]
            if codon == [ "A" , "T" , "G"] :
                slc_code += "M"
                del dna_seq[0:3]
            else :
                slc_code += "X"
                del dna_seq[0:3]
        else :
            break 
            return slc_code
        
# Add another function to the program SickleCellDisease.py called 'mutate'. This function must read the contents of the text file named 'DNA.txt'. It must then identify the first occurrence of the lowercase letter 'a' in 'DNA.txt'.
# You must then write two new text files, one named normalDNA.txt and the other named mutatedDNA.txt.
# The file normalDNA.txt must have the same DNA sequence as DNA.txt with the 'a' changed to an 'A'.
# The file mutatedDNA.txt must have the same DNA sequence as DNA.txt with the 'a' changed to a 'T'.
# Now create a new function, ‘txtTranslate’, that calls the translate function that you wrote in Task 1, to take in text file input.
# Call it on both mutatedDNA.txt and normalDNA.txt, and output both Amino Acid sequences to the user.

def mutate(filename):
    dna_list = read_file(filename) 
    normal_dna_output = open("normalDNA.txt","w")
    mutated_dna_output = open("mutatedDNA.txt","w")
 
    for dna in range(len(dna_list)) :
        if dna_list[dna] != "a" : 
        	normal_dna_output.write(dna_list[dna])
           
        else :
            normal_dna_output.write("A") 
            mutated_dna_output.write("T")         
    mutated_dna_output.close()
    normal_dna_output.close()

def txtTranslate(filename1, filename2) :
    normal_file = read_file(filename1)
    mutated_file = read_file(filename2)
    print ("Amino Acids of normal DNA: ", translate(normal_file))
    print ("")
    print ("Amino Acids of mutated DNA: ", translate(mutated_file))
   
mutate("DNA.txt")
txtTranslate("normalDNA.txt", "mutatedDNA.txt")

time.sleep(90)
