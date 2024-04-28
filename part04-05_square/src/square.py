# Copy here code of line function from previous exercise
def line(nb, string):
    if string == "":
        print("*"*nb)
    else:
        char = string[0]
        print(char*nb)

def square(size, character):
    # You should call function line here with proper parameters
    i = 0
    while i <= (size - 1):
        line(size, character)
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "*")
    print()
    square(3, "o")