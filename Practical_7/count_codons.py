#ask users to input a stop codon
#error if input is not a stop codon
#create an empty dict to store codons and the times they appear
#define a function to find the longest ORF ending with the specified stop codon
#open the file
#create curr_seq/_gene to store
#the same as the former task
#find the longest ORF ending with the specified stop codon in each gene
#count codons in the longest ORF
#print codon counts
#stop if no ORFs were found
#generate well labelled pie chart from codon counts
#save the pie chart
stop=input("input a stop codon (TAA,TAG or TGA):")
if not stop in ["TAA","TAG","TGA"]:
    print(f"{stop} is not a stop codon") 
    exit()
codon_counts={}
def find_longest_orf(seq, target_stop):
    longest_orf = ""

    for start in range(len(seq) - 2):
        if seq[start:start+3] == "ATG":

            for pos in range(start + 3, len(seq) - 2, 3):
                codon = seq[pos:pos+3]

                if codon == target_stop:
                    orf = seq[start:pos]

                    if len(orf) > len(longest_orf):
                        longest_orf = orf

    return longest_orf

with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r') as infile:
    curr_seq=[]
    curr_gene=""
    for line in infile:
        line=line.strip()
        if line.startswith(">"):
            if curr_gene:
                full_seq=''.join(curr_seq)
                longest_ORF=find_longest_orf(full_seq,stop)
                if longest_ORF:
                    ORF_codons=[longest_ORF[i:i+3] for i in range(0,len(longest_ORF),3)]
                    for cod in ORF_codons:
                        if cod in codon_counts:
                            codon_counts[cod]=codon_counts[cod]+1
                        else:
                            codon_counts[cod]=1
            curr_gene=line.split()[0][1:]
            curr_seq=[]
        else:
            curr_seq.append(line)
    if curr_gene:
        full_seq=''.join(curr_seq)
        longest_ORF=find_longest_orf(full_seq,stop)
        if longest_ORF:
            ORF_codons=[longest_ORF[i:i+3] for i in range(0,len(longest_ORF),3)]
            for cod in ORF_codons:
                if cod in codon_counts:
                    codon_counts[cod]=codon_counts[cod]+1
                else:
                    codon_counts[cod]=1
print(f"Codon counts upstream of {stop}:")
for codon, count in sorted(codon_counts.items()):
    print(codon, ":", count)

if not codon_counts:
    print(f"No ORFs ending with {stop} were found.")
    exit()

import matplotlib.pyplot as plt
total = sum(codon_counts.values())
threshold = 0.007
filtered_counts = {}
others_count = 0
for codon, count in codon_counts.items():
    if count / total >= threshold:
        filtered_counts[codon] = count
    else:
        others_count += count
if others_count > 0:
    filtered_counts["Others"] = others_count
sorted_counts=dict(sorted(filtered_counts.items(),key=lambda x:x[1]))
if "Others" in sorted_counts:
    sorted_counts["Others"] = sorted_counts.pop("Others")
plt.figure(figsize=(12,14))
plt.pie(sorted_counts.values(),labels=None,autopct='%1.1f%%',startangle=90,textprops={'fontsize':8},pctdistance=1.15)
plt.legend(sorted_counts.keys(),ncol=1,loc="center left",bbox_to_anchor=(1,0.5))
plt.title(f"Codon distribution for genes ending in {stop}\n(Rare codons are grouped as Others)")
plt.savefig("codon_pie.png",dpi=300)