# Write your solution here
def spruce(size):
    print("a spruce!")
    i = 1
    nb = 1
    spaces = size - 1
    while i <= size:
        print(" "*spaces + "*"*nb)
        spaces -= 1
        nb += 2
        i += 1
    spaces = size - 1
    print(" "*spaces + "*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)
    print()
    spruce(3)