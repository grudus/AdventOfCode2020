from collections import defaultdict
import re

def first_star(foods):
    _, ingredients_occurences = find_menu(foods)
    return sum([occurence for _, occurence in ingredients_occurences])

def second_star(foods):
    known_ingredients, _ = find_menu(foods)
    return ",".join([ingredient for ingredient, _ in sorted(known_ingredients, key = lambda entry: entry[1])])


def find_menu(foods):
    food_pattern = re.compile(r"(.*) \(contains (.*)\)")
    foods = [(ingredients.split(), allergens.replace(",", "").split()) 
    for food in foods 
    for ingredients, allergens in food_pattern.findall(food)]
    
    allergens_to_possible_ingredients = defaultdict(lambda: defaultdict(int))
    ingredients_occurences = defaultdict(int)

    for ingredients, allergens in foods:
        for ingredient in ingredients:
            ingredients_occurences[ingredient] += 1
            for allergen in allergens:
                allergens_to_possible_ingredients[allergen][ingredient] += 1

    
    known_ingredients = {}
    is_known_ingredient = lambda ingr: ingr in known_ingredients.keys()
    num_of_allergens = len(allergens_to_possible_ingredients.keys())

    while len(known_ingredients) != num_of_allergens:

        for allergen, ingredients_count in list(allergens_to_possible_ingredients.items()):
            ingredients_count = [entry for entry in ingredients_count.items() if not is_known_ingredient(entry[0])]
            max_count = max([count for ingredient, count in ingredients_count])
            best_ingredients_for_allergen = [ingredient for ingredient, count in ingredients_count if count == max_count]
            
            if len(best_ingredients_for_allergen) == 1:
                ingredient = best_ingredients_for_allergen[0]
                known_ingredients[ingredient] = allergen
                del allergens_to_possible_ingredients[allergen]
                del ingredients_occurences[ingredient]
    
    return known_ingredients.items(), ingredients_occurences.items()

if __name__ == "__main__":
    foods = open('src/main/resources/day21/input.txt', 'r').read().split("\n")
    print(first_star(foods))
    print(second_star(foods))