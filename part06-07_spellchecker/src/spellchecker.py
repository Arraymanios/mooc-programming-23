# write your solution here
char = '*'
sentence = []
string = input("Write text: ")
sentence = string.split(' ')

with open("wordlist.txt") as new_file:
  wordlist = new_file.read().split() # Can't check the content of a file directly, one must create a list to do so

for i in range(len(sentence)):
  if sentence[i].lower() not in wordlist:
    sentence[i] = char + sentence[i] + char # Strings are immutable hence the relying on indexes

for word in sentence:
  print(word, end=" ")