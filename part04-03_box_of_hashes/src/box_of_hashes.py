# Copy here code of line function from previous exercise
def box_of_hashes(height):
    i = 0
    while i <= (height - 1):
        line(10, "#")
        i += 1
        
def line(nb, string):
    if string == "":
        print("*"*nb)
    else:
        char = string[0]
        print(char*nb)
    # You should call function line here with proper parameters
    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
    print()
    box_of_hashes(2)