# Write your solution here
def line(nb, string):
    if string == "":
        print("*"*nb)
    else:
        char = string[0]
        print(char*nb)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "")