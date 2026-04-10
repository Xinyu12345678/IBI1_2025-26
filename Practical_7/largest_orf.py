#create a string variable seq
#import library re
#find ORF sequence with stop codons ‘UAA’, ‘UAG’, and	‘UGA’ respectively (non-greedy)
#exclude the blank list
#identify the longest potential	open reading in	within gene	sequences
#report the length of that ORF in nucleotides
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
import re
#making sure the internal nucleotides is multiples of three
#take the ORF out(get rid of stop codons)
seq_list=re.findall(r'(AUG(?:...)+?)(?:UAA|UAG|UGA)',seq)
#Considering that the inner list may has more than one element or no element
#store all the sequence into a list called all_ORF
print(seq_list)
all_ORF=[]
for i in seq_list:
    all_ORF.append(i)
#making sure there is ORF
if all_ORF:
    ORF_max=max(all_ORF,key=len)
    print(f'the largest ORF is {ORF_max}')
    print("length of ORF :",len(ORF_max) )
else:
    print("There is no ORF identified in the sequence")