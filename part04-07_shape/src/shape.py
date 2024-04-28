# Copy here code of line function from previous exercise and use it in your solution
def line(nb, string):
    if string == "":
        print("*"*nb)
    else:
        char = string[0]
        print(char*nb)

def shape(size, char, width, filler):
    i = 1
    while i <= size:
        line(i, char)
        i += 1

    i = 1
    if width == 0:
        print("")
    while i <= width:
        line(size, filler)
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")
    shape(3, ".", 0, ",")