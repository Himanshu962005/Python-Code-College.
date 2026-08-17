# Q24.Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary.
s = input("Enter Sentence : ")
words = s.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)