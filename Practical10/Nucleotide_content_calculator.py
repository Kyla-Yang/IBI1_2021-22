DNA_input = input("Please input your DNA sequenece:")
#let users to input a DNA sequence
import re
#imort re function
DNA_sequence = ''.join(re.findall(r'[a-zA-Z]', DNA_input))
#extract DNA sequence and store it in a list called 'DNA_sequence'
A_sequence = re.findall(r'A', DNA_sequence)
#find all 'A's in DNA_sequence and store them in a list called A_sequence
G_sequence = re.findall(r'G', DNA_sequence)
#find all 'G's in DNA_sequence and store them in a list called G_sequence
C_sequence = re.findall(r'C', DNA_sequence)
#find all 'C's in DNA_sequence and store them in a list called C_sequence
T_sequence = re.findall(r'T', DNA_sequence)
#find all 'T's in DNA_sequence and store them in a list called T_sequence
def f(x):
    y = x/len(DNA_sequence)
    return y
#define a function named f(x), which calculate the percentage of every base
x = len(A_sequence)
#use len to calculate the number of 'A' in the DNA sequence
print(f(x), "is the percentage of A")
#calculate the percentage of 'A'
x = len(G_sequence)
#use len to calculate the number of 'G' in the DNA sequence
print(f(x), "is the percentage of G")
#calculate the percentage of 'G'
x = len(C_sequence)
#use len to calculate the number of 'C' in the DNA sequence
print(f(x), "is the percentage of C")
#calculate the percentage of 'C'
x = len(T_sequence)
#use len to calculate the number of 'T' in the DNA sequence
print(f(x), "is the percentage of T")
#calculate the percentage of 'T'
#take an example:
#input:AGCAGTCAGACGGACTGC
#print:
#0.2777777777777778 is the percentage of A
#0.3333333333333333 is the percentage of G
#0.2777777777777778 is the percentage of C
#0.1111111111111111 is the percentage of T
