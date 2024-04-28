# Write your solution here
def first_word(sentence):
    first = ""
    i = 0
    while i <= len(sentence) - 1 and sentence[i] != " ":
        first += sentence[i]
        i += 1
    return first

def second_word(sentence):
    second = ""
    i = 0
    while sentence[i] != " ":
        i += 1
    i += 1
    sentence = sentence[i:]
    return first_word(sentence)

def last_word(sentence):
    last = ""
    i = -1
    while sentence[i] != " ":
        i -= 1
    i += 1
    sentence = sentence[i:]
    return sentence
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))