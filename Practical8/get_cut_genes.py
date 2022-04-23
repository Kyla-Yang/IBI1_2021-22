import re
#import re function
file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
#open file 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa' as a reading one
dir1 = {}
#set up a dictionary called dir1
for line in file:
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
output_file = open('cut_genes.fa', 'w')
#open the output file as a writing one
for i in dir1.keys():
#i represents the gene lines
    if re.search('GAATTC',dir1[i]):
        target_DNA = re.findall('GAATTC', dir1[i])
#if 'GAATTC' can be searched in these sequence, select those target ones
        length = str(len(dir1[i]))
#caculate the length of selected DNA
        DNA_and_length = i + " " + length
        DNA_and_number = DNA_and_length.strip()
#delete the white spaces before the gene names
        output_file.write(DNA_and_length + dir1[i] + '\n')
#ouput the gene names, lengthes and sequences 

