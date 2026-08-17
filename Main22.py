# Q21.Python Program to Count the Occurrences of Each Word in a Given String Sentence.
s = input("Enter Sentence : ")
words = s.split()
for word in set(words):
    print(word, ":", words.count(word))