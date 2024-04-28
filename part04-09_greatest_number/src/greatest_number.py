# Write your solution here
def greatest_number(nb1, nb2, nb3):
    if nb1 >= nb2 and nb1 >= nb3:
        return nb1
    if nb2 >= nb1 and nb2 >= nb3:
        return nb2
    if nb3 >= nb1 and nb3 >= nb2:
        return nb3
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)