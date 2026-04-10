#ask users to input a stop codon
#error if input is not a stop codon
#create an empty dict to store codons and the times they appear
#open the file
#ceate curr_seq/_gene to store 
#the same as the former task(differnce:find )
#
#
#
import re
stop=input("input a stop codon (TAA,TAG or TGA):")
if not stop in ["TAA","TAG","TGA"]:
    print(f"{stop} is not a stop codon") 
    exit()
codon_counts={}
with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r') as infile:
    curr_seq=[]
    curr_gene=""
    for line in infile:
        line=line.strip()
        if line.startswith(">"):
            if curr_gene:
                full_seq=''.join(curr_seq)
                all_ORF=re.findall(r"(ATG(?:...)*?)(TAA|TAG|TGA)",full_seq)
                valid_ORFs=[]
                for ORF, stop_cod in all_ORF:
                    if stop_cod==stop:
                        valid_ORFs.append(ORF)
                if valid_ORFs:
                    longest_ORF=max(valid_ORFs,key=len)
                    ORF_codons=[longest_ORF[i:i+3] for i in range(0,len(longest_ORF),3)]
                    for cod in ORF_codons:
                        if cod in codon_counts:
                            codon_counts[cod]=codon_counts[cod]+1
                        else:
                            codon_counts[cod]=1
                else:
                    continue
            curr_gene=line.split()[0][1:]
            curr_seq=[]
        else:
            curr_seq.append(line)
    if curr_gene:
        full_seq=''.join(curr_seq)
        all_ORF=re.findall(r"(ATG(?:...)*?)(TAA|TAG|TGA)",full_seq)
        valid_ORFs=[]
        for ORF, stop_cod in all_ORF:
            if stop_cod==stop:
                valid_ORFs.append(ORF)
        if valid_ORFs:
            longest_ORF=max(valid_ORFs,key=len)
            ORF_codons=[longest_ORF[i:i+3] for i in range(0,len(longest_ORF),3)]
            for cod in ORF_codons:
                if cod in codon_counts:
                    codon_counts[cod]=codon_counts[cod]+1
                else:
                    codon_counts[cod]=1
import matplotlib.pyplot as plt
import numpy as np
codon_counts=dict(sorted(codon_counts.items(),key=lambda x:x[1]))
plt.figure(figsize=(12,12))
plt.pie(codon_counts.values(),labels=None,autopct='%1.1f%%',startangle=90,textprops={'fontsize':8},pctdistance=0.85)
plt.legend(codon_counts.keys(),ncol=2,loc="center left",bbox_to_anchor=(1,0.5))
plt.title(f"Codon distribution for genes ending in {stop}")
plt.savefig("codon_pie.png",dpi=300)