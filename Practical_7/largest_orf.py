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
seq_list=re.findall(r'(AUG(?:...)*?)(?:UAA|UAG|UGA)',seq)
print(seq_list)
#making sure there is ORF
if seq_list:
    ORF_max=max(seq_list,key=len)
    print(f'the largest ORF is {ORF_max}')
    print("length of ORF :",len(ORF_max) )
else:
    print("There is no ORF identified in the sequence")