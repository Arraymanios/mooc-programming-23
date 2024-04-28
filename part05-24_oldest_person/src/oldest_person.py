# Write your solution here
def oldest_person(people: list):
  elder = people[0][0]
  birth_year = people[0][1]
  for person in people:
    if person[1] < birth_year:
      birth_year = person[1]
      elder = person[0]
  return elder

if __name__ == "__main__":
  p1 = ("Adam", 1977)
  p2 = ("Ellen", 1985)
  p3 = ("Mary", 1990)
  p4 = ("Ernest", 1997)
  people = [p1, p2, p3, p4]

  print(oldest_person(people))