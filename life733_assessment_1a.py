# LIFE733 Assessment 1 Part 1A - Working with strings

dna_seq_1 = input("Enter DNA sequence 1:\n")  # user inputs first DNA sequence
dna_seq_2 = input("Enter DNA sequence 2:\n ")  # user inputs Second DNA sequence
dna_seq_3 = dna_seq_1.upper() + dna_seq_2.upper()
# converts the two sequences into upper case and concatenatess them together
print("\nDNA length =", len(dna_seq_3))  # prints the numerical length of the string
print(dna_seq_3)  # prints the DNA sequence in uppercase
reverse_complement = dna_seq_3.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
# multi-step function: replaces the uppercase basepairs with their complementary bases in lowercase to
# avoid overwriting, then converts the string to uppercase, then reverses the string via slicing
print('\nReverse Complement:\n', reverse_complement)  # prints the reverse compliment
polya = 'AAAAAAA'  # polyA tail to be added onto the RNA sequence
rna_seq = dna_seq_3.replace('T', 'U')  # replaces the 'C's in the sequence with 'U's
rna_seq_tail = rna_seq + polya  # Concatenating the RNA sequence with the polyA tail
print("\nRNA length =", len(rna_seq_tail))  # prints the numerical length of the string
print(rna_seq_tail)  # prints the RNA sequence in uppercase
