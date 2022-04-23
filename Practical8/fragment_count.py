import re
#import re function
seq = 'ATGCCATCGACTACGATCAATCGAGGGCC'
#set up seq
cut = re.findall(r'GAATTC', seq)
#find all 'GAATTC' sequence in 'seq' and put them in a list called 'cut'
print('the fragment number =', len(cut)+1)
#use 'len' function to count how many cuts are there

