import pandas as pd
import re
#import pandas and re function
sequence = ''
def read_file(file):
    for lines in file:
        if not lines.startswith('>'):
            sequence = lines
    sequence = re.sub(r'\s+','', sequence)
    sequence = re.sub(r'\n','', sequence)
    return sequence
#define a function to select the amino sequence from lines in files
file1 = read_file(open('DLX5_human.fa'))
print(file1)
file2 = read_file(open('DLX5_mouse.fa'))
print(file2)
file3 = read_file(open('RandomSeq(1).fa'))
print(file3)
# Read the 3 files and extract their DNA sequence
BLOSUM_62 = {'A':[4,-1,-2,-2,0,-1,-1,0,-2,-1,-1,-1,-1,-2,-1,1,0,-3,-2,0,-2,-1,0,-4],'R':[-1,5,0,-2,-3,1,0,-2,0,-3,-2,2,-1,-3,-2,-1,-1,-3,-2,-3,-1,0,-1,-4],
           'N':[-2,0,6,1,-3,0,0,0,1,-3,-3,0,-2,-3,-2,1,0,-4,-2,-3,3,0,-1,-4],'D':[-2,-2,1,6,-3,0,2,-1,-1,-3,-4,-1,-3,-3,-1,0,-1,-4,-3,-3,4,1,-1,-4],
           'C':[0,-3,-3,-3,9,-3,-4,-3,-3,-1,-1,-3,-1,-2,-3,-1,-1,-2,-2,-1,-3,-3,-2,-4],'Q':[-1,1,0,0,-3,5,2,-2,0,-3,-2,1,0,-3,-1,0,-1,-2,-1,-2,0,3,-1,-4],
           'E':[-1,0,0,2,-4,2,5,-2,0,-3,-3,1,-2,-3,-1,0,-1,-3,-2,-2,1,4,-1,-4],'G':[0,-2,0,-1,-3,-2,-2,6,-2,-4,-4,-2,-3,-3,-2,0,-2,-2,-3,-3,-1,-2,-1,-4],
           'H':[-2,0,1,-1,-3,0,0,-2,8,-3,-3,-1,-2,-1,-2,-1,-2,-2,2,-3,0,0,-1,-4],'I':[-1,-3,-3,-3,-1,-3,-3,-4,-3,4,2,-3,1,0,-3,-2,-1,-3,-1,3,-3,-3,-1,-4],
           'L':[-1,-2,-3,-4,-1,-2,-3,-4,-3,2,4,-2,2,0,-3,-2,-1,-2,-1,1,-4,-3,-1,-4],'K':[-1,2,0,-1,-3,1,1,-2,-1,-3,-2,5,-1,-3,-1,0,-1,-3,-2,-2,0,1,-1,-4],
           'M':[-1,-1,-2,-3,-1,0,-2,-3,-2,1,2,-1,5,0,-2,-1,-1,-1,-1,1,-3,-1,-1,-4],'F':[-2,-3,-3,-3,-2,-3,-3,-3,-1,0,0,-3,0,6,-4,-2,-2,1,3,-1,-3,-3,-1,-4],
           'P':[-1,-2,-2,-1,-3,-1,-1,-2,-2,-3,-3,-1,-2,-4,7,-1,-1,-4,-3,-2,-2,-1,-2,-4],'S':[1,-1,1,0,-1,0,0,0,-1,-2,-2,0,-1,-2,-1,4,1,-3,-2,-2,0,0,0,-4],
           'T':[0,-1,0,-1,-1,-1,-1,-2,-2,-1,-1,-1,-1,-2,-1,1,5,-2,-2,0,-1,-1,0,-4],'W':[-3,-3,-4,-4,-2,-2,-3,-2,-2,-3,-2,-3,-1,1,-4,-3,-2,11,2,-3,-4,-3,-2,-4],
           'Y':[-2,-2,-2,-3,-2,-1,-2,-3,2,-1,-1,-2,-1,3,-3,-2,-2,2,7,-1,-3,-2,-1,-4],'V':[0,-3,-3,-3,-1,-2,-2,-3,-3,3,1,-2,1,-1,-2,-2,0,-3,-1,4,-3,-2,-1,-4],
           'B':[-2,-1,3,4,-3,0,1,-1,0,-3,-4,0,-3,-3,-2,0,-1,-4,-3,-3,4,1,-1,-4],'Z':[-1,0,0,1,-3,3,4,-2,0,-3,-3,1,-1,-3,-1,0,-1,-3,-2,-2,1,4,-1,-4],
           'X':[0,-1,-1,-1,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2,0,0,-2,-1,-1,-1,-1,-1,-4],'*':[-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,1]}
# Read BLOSUM_62. obtained from the "https://github.com/Raha-Kheirinia/BLOSUM62/blob/master/BLOSUM62.txt" and write them in a dictionary
BLOSUM_62 = pd.DataFrame(BLOSUM_62, columns = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V','B','Z','X','*'],
                       index = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V','B','Z','X','*'])
# pd.DataFrame is a function that can turn the dictionary format into the dataframe format, so we can see it clearly
print(BLOSUM_62)
total_score1 = 0
#give a value to total_score1
for i in range(len(file1)):
    score1 = BLOSUM_62.loc[file1[i],file2[i]]
#use BLOSM_62 to score the alignment in human and mouse DLX5 sequence
    total_score1 = total_score1 + score1
print("The score for alignment in human and mouse DLX5 sequence is:", total_score1)
total_score2 = 0
#give a value to total_score2
for i in range(len(file1)):
    score2 = BLOSUM_62.loc[file1[i],file3[i]]
#use BLOSM_62 to score the alignment in human DLX5 and random sequence
    total_score2 = total_score2 + score2
print("The score for alignment in human DLX5 and random sequence is:", total_score2)
total_score3 = 0
#give a value to total_score3
for i in range(len(file2)):
    score3 = BLOSUM_62.loc[file2[i],file3[i]]
#use BLOSM_62 to score the alignment in mouse DLX5 and random sequence
    total_score3 = total_score3 + score3
print("The score for alignment in mouse DLX5 and random sequence is:", total_score2)
similarity1 = 0
for i in range(len(file1)):
    if file1[i] == file2[i]:
        similarity1 += 1
percentage1 = similarity1/len(file1)
#calculate the percentage of the similarity between human and mouse DLX5 sequence
print("The percentage of identical amino acids for the comparison between human and mouse DLX5 sequence is", percentage1)
similarity2 = 0
for i in range(len(file1)):
    if file1[i] == file3[i]:
        similarity2 += 1
percentage2 = similarity2/len(file1)
#calculate the percentage of the similarity between human DLX5 and random sequence
print("The percentage of identical amino acids for the comparison between human DLX5 and random sequence is", percentage2)
similarity3 = 0
for i in range(len(file2)):
    if file2[i] == file3[i]:
        similarity3 += 1
percentage3 = similarity3/len(file2) 
#calculate the percentage of the similarity between mouse DLX5 and random sequence
print("The percentage of identical amino acids for the comparison between mouse DLX5 and random sequence is", percentage3)

