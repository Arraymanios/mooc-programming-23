# Write your solution here

def search_by_name(filename: str, word: str):
  with open(filename) as new_file:
    recipes = []
    recipe = []
    names = []

    for line in new_file:
      line = line.strip()
      if line:
        recipe.append(line)
      else:
        recipes.append(recipe)
        recipe = []
    if recipe:
      recipes.append(recipe)

    for recipe in recipes:
      if word in str(recipe[0]).lower():
        names.append(recipe[0])
  return names

def search_by_time(filename: str, prep_time: int):
  with open(filename) as new_file:
    recipes = []
    recipe = []
    data = []

    for line in new_file:
      line = line.strip()
      if line:
        recipe.append(line)
      else:
        recipes.append(recipe)
        recipe = []
    if recipe:
      recipes.append(recipe)
    
    for recipe in recipes:
      if int(recipe[1]) <= prep_time:
        data.append((recipe[0], recipe[1]))
  return data

def search_by_ingredient(filename: str, ingredient: str):
  with open(filename) as new_file:
    recipes = []
    recipe = []
    data = []

    for line in new_file:
      line = line.strip()
      if line:
        recipe.append(line)
      else:
        recipes.append(recipe)
        recipe = []
    if recipe:
      recipes.append(recipe)

    for recipe in recipes:
      if ingredient in recipe:
        data.append((recipe[0], recipe[1]))
  return data


if __name__ == "__main__":

  found_recipes = search_by_name("recipes1.txt", "cake")

  for recipe in found_recipes:
    print(recipe)

  found_recipes = search_by_time("recipes1.txt", 20)

  for recipe in found_recipes:
    print(f"{recipe[0]}, preparation time {recipe[1]} min")

  found_recipes = search_by_ingredient("recipes1.txt", "eggs")

  for recipe in found_recipes:
    print(f"{recipe[0]}, preparation time {recipe[1]} min")