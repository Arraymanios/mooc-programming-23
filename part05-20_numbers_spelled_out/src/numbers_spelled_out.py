# Write your solution here
def dict_of_numbers():
  numbers = {}
  for i in range (100):
    spelled = ""
    if len(str(i)) == 1:
      if i == 0:
        spelled += "zero"
      elif i == 1:
        spelled += "one"
      elif i == 2:
        spelled += "two"
      elif i == 3:
        spelled += "three"
      elif i == 4:
        spelled += "four"
      elif i == 5:
        spelled += "five"
      elif i == 6:
        spelled += "six"
      elif i == 7:
        spelled += "seven"
      elif i == 8:
        spelled += "eight"
      elif i == 9:
        spelled += "nine"
      numbers[i] = spelled
      continue
    elif len(str(i)) == 2:
      if i < 20:
        if i == 10:
          spelled += "ten"
        elif i == 11:
          spelled += "eleven"
        elif i == 12:
          spelled += "twelve"
        elif i == 13:
          spelled += "thirteen"
        elif i == 14:
          spelled += "fourteen"
        elif i == 15:
          spelled += "fifteen"
        elif i == 16:
          spelled += "sixteen"
        elif i == 17:
          spelled += "seventeen"
        elif i == 18:
          spelled += "eighteen"
        elif i == 19:
          spelled += "nineteen"
        numbers[i] = spelled
        continue
      else:
        if (i // 10 %10) == 2:
          spelled += "twenty"
        elif (i // 10 %10) == 3:
          spelled += "thirty"
        elif (i // 10 %10) == 4:
          spelled += "forty"
        elif (i // 10 %10) == 5:
          spelled += "fifty"
        elif (i // 10 %10) == 6:
          spelled += "sixty"
        elif (i // 10 %10) == 7:
          spelled += "seventy"
        elif (i // 10 %10) == 8:
          spelled += "eighty"
        elif (i // 10 %10) == 9:
          spelled += "ninety"
        
        if (i % 10) == 1:
          spelled += "-one"
        elif (i % 10) == 2:
          spelled += "-two"
        elif (i % 10) == 3:
          spelled += "-three"
        elif (i % 10) == 4:
          spelled += "-four"
        elif (i % 10) == 5:
          spelled += "-five"
        elif (i % 10) == 6:
          spelled += "-six"
        elif (i % 10) == 7:
          spelled += "-seven"
        elif (i % 10) == 8:
          spelled += "-eight"
        elif (i % 10) == 9:
          spelled += "-nine"
    numbers[i] = spelled

  return numbers


if __name__ == "__main__":
  nb = dict_of_numbers()
  for key in nb:
    print(nb[key])