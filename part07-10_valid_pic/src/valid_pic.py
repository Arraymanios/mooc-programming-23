# Write your solution here
from datetime import datetime

def check_birthdate(birthdate: str, marker: str):
  existing = True
  day = int(birthdate[0] + birthdate[1])
  month = int(birthdate[2] + birthdate[3])
  if marker == '+':
    year = 1800 + int(birthdate[4] + birthdate[5])
  elif marker == '-':
    year = 1900 + int(birthdate[4] + birthdate[5])
  elif marker == 'A':
    year = 2000 + int(birthdate[4] + birthdate[5])

  try:
    datetime(year, month, day)
  except ValueError:
    existing = False
    
  return existing

def check_century(marker: str):
  if marker == '+':
    return True
  elif marker == '-':
    return True
  elif marker == 'A':
    return True
  return False

def check_control_character(digits: str, control_character: str):
  characters = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','H','J','K','L','M','N','P','R','S','T','U','V','W','X','Y']
  digits = int(digits)
  remaining = digits % 31
  if 0 <= remaining <= 30 and characters[remaining] == control_character:
    return True
  return False

def is_it_valid(pic: str):
  if len(pic) == 11 and check_century(pic[6]) and check_birthdate(pic[0:6], pic[6]) and check_control_character(pic[0:6] + pic[7:10], pic[10]):
    return True
  return False

if __name__ == "__main__":
  print(is_it_valid("230827-906F"))
  print(is_it_valid("120488+246L"))
  print(is_it_valid("310823A9877"))