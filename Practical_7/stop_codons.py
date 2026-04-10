#open and read the input file, open and write the output file
#use curr_gene to store gene names(str)
#use an empty list to store every line of one gene.
#delete the \n in every line
#combine lines under every > to be one line 
#search for the lines that has at least one in frame stop codon
#identify and store all the different end codons
#write them into the output file
#add the last gene(do not have > at its end)
import re
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') as infile, open("stop_genes.fa","w") as outfile:
    curr_seq=[]
    curr_gene=""
    for line in infile:
        line=line.strip()
        if line.startswith(">"):
            if curr_gene:
                full_seq="".join(curr_seq)
                seq=re.findall('(ATG(?:...)*?)(TAA|TAG|TGA)',full_seq)
                stops={i[1] for i in seq} 
                if stops:
                    full_seq='\n'.join([full_seq[i:i+80] for i in range(0,len(full_seq),80)])
                    outfile.write(f">{curr_gene};{','.join(stops)}\n{full_seq}\n")
            curr_gene=line.split()[0][1:]
            curr_seq=[]
        else:
            curr_seq.append(line)
    full_seq=''.join(curr_seq)
    seq=re.findall('(ATG(?:...)*?)(TAA|TAG|TGA)',full_seq)
    stops={i[1] for i in seq} 
    if stops:
        full_seq='\n'.join([full_seq[i:i+80] for i in range(0,len(full_seq),80)])
        outfile.write(f">{curr_gene};{','.join(stops)}\n{full_seq}\n")