# Write your solution here
def same_chars(string, nb1, nb2):
    if nb1 >= len(string) or nb2 >= len(string) or nb1 < 0 or nb2 < 0:
        return False
    if string[nb1] == string[nb2]:
        return True
    else:
        return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
    print(same_chars("coder", -3, 2))