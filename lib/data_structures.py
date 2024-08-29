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
    return [food ["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
   for food in spicy_foods:
        name = food.get('name',)
        cuisine = food.get('cuisine')
        heat_level = food.get('heat_level', 0)
        
        
        heat_emoji = '🌶' * heat_level
        
        print(f"{name} ({cuisine}) | Heat Level: {heat_emoji}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    
    
    for food in spicy_foods:
        
        if food.get('cuisine') == cuisine:
            return food
    
    return None

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = food.get('heat_level', 0)
        if heat_level > 5:
            # Generate the string of 🌶 emojis
            peppers = '🌶' * heat_level
            # Format the string
            formatted_string = f"{food['name']} ({food['cuisine']}) | Heat Level: {peppers}"
            # Print the formatted string
            print(formatted_string)

def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0
    
    total_heat = 0
    count = 0
    
    for food in spicy_foods:
        total_heat += food.get('heat_level', 0)
        count += 1
    
    
    average_heat = total_heat // count
    
    return average_heat

def create_spicy_food(spicy_foods, new_spicy_food):
        spicy_foods.append(new_spicy_food)
        return spicy_foods

