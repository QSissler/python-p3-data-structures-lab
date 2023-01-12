spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    list_of_names = [item["name"] for item in spicy_foods]
    return list_of_names

def get_spiciest_foods(spicy_foods):
    spicy_only = [item for item in spicy_foods if item["heat_level"] > 5]
    return spicy_only

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    spicy_only = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spicy_only)

def get_average_heat_level(spicy_foods):
    spice_levels = [food["heat_level"] for food in spicy_foods]
    return sum(spice_levels) / len(spice_levels)
        
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods