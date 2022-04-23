import re
#import re function
file_name = input('give a name to the file:')
#let users input the file name
output_file = open(file_name, 'w')
origin_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
#open file 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa' as a reading one
dir1 = {}
#set up a dictionary called dir1
for line in origin_file:
    line = line.rstrip()
#copy the string in file and store it
    if line.startswith('>'):
        gene = re.search(r'gene:(.+?\s)', line)
#search for genes' names in the line
        gene_seq = '\n' + '>' + gene.group(1)
#put gene names in a list called gene_seq
        dir1[gene_seq] = " "
#if the line is gene name, it will become white space
    else:
        dir1[gene_seq] = dir1[gene_seq] + line
#if the line is gene sequence, it will be put into the dirtionary
for i in dir1.keys():
#i represents the gene lines
    if re.search('GAATTC',dir1[i]):
        target_DNA = re.findall('GAATTC', dir1[i])
#if 'GAATTC' can be searched in these sequence, select those target ones
        fragment = str(len(dir1[i]) + 1)
#caculate the fragments of selected DNA after being cut
        DNA_and_fragment = i + " " + fragment
        DNA_and_number = DNA_and_fragment.strip()
        output_file.write(DNA_and_number + dir1[i] + '\n')
#ouput the gene names, fragments and sequences

