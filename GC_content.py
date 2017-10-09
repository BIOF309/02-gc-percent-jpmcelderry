print("Enter sequence below to check for GC content:")
seq=input()

upperseq= seq.upper() #this line makes the program insensitive to case
GC_count= upperseq.count('G')+upperseq.count('C') #count the number of G's and C's
total_length= len(upperseq) #count the total length of the sequence
GCATUs= upperseq.count('G')+upperseq.count('C')+upperseq.count('A')+upperseq.count('T')+upperseq.count('U') #total the number of g's,c's,t's,a's and u's for the sake of proofreading

if GCATUs != total_length : #check to make sure that the sequence only contained bases g,c,t,a, and u. The program will still give the gc content based on total sequence length, but will warn the user about the extra characters.
    print("\n**WARNING: Your sequence contained characters other than G,C,A,T, and U. The answer below is based on all characters in your sequence. You may want to double check your sequence for accuracy.**")

final=(GC_count/total_length)*100 #calculate percentage
print("\nThe GC content of your sequence is {}%".format(round(final,2))) #give % to the user, rounded to 2 decimal places
