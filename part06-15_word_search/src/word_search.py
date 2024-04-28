# Write your solution here
def find_words(search_term: str):
  match = []
  word = []
  with open("words.txt", "r") as dictionary:
    if '.' in search_term:
      pass
    elif '*' in search_term:
      for line in dictionary:
        if search_term.startswith('*'):
          word.insert(len(word), search_term[1:]) 
          if line.endswith(word[len(word) - 1]):
            match.append(line)
        elif search_term.endswith('*'):
          word.insert(len(word), search_term[0:(len(search_term) - 1)]) 
          for line in dictionary:
            if line.startswith(word[len(word) - 1]):
              match.append(line)
  
  return match

if __name__ == "__main__":
  find_words("*vokes")
  # print(find_words("ca*"))