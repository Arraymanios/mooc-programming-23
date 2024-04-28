# write your solution here
def read_fruits():
  fruit_market = {}
  with open("fruits.csv") as new_file:
    for line in new_file:
      line = line.replace("\n", "")
      parts = line.split(";")
      name = parts[0]
      price = float(parts[1])
      fruit_market[name] = price
  return fruit_market

if __name__ == "__main__":
  print("Fruits and their respective prices :")
  print(read_fruits())