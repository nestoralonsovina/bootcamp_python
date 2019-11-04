options = {
    1: {'text': "Add a recipe", 'func': ''},
    2: {'text': "Delete a recipe", 'func': ''},
    3: {'text': "Print a recipe", 'func': ''},
    4: {'text': "Print the cookbook", 'func': ''},
    5: {'text': 'Quit', 'func': ''},
}

def prompt(message = None):
    if message:
        print(message)
    return input(">> ")

def prompt_select():
    print("Please select an option by typing the corresponding number:")

    for (key, option) in options.items():
        print(f"{key}: " + option['text'])

    try:
        n = int(prompt())
        if n not in options:
            raise ValueError()
    except ValueError:
        print("This option does not exist, please type the corresponding number.\n" + "To exit, enter 5")
        prompt_select()
    else:
        return n

def prompt_recipe():
    return prompt("Recipe name:"), {
        "ingredients": prompt("Ingredients separated by space:").split(),
        "meal": prompt("Meal:"),
        "prep_time": prompt("Preparation time in minutes:")
    }

recipes = {

}

def add_recipe():
    name, recipe = prompt_recipe()
    recipes[name] = recipe

def delete_recipe():
    print("Please enter the recipe's name to delete:")
    recipe = prompt()
    if recipe in recipes:
        del recipes[recipe]
    else:
        print("This recipe doesn't exist.")



def print_cookbook():
    for name, recipe in recipes.items():
        print("\n")
        print(f"Recipe for {name}:")
        print("Ingredients list: " + str(recipe['ingredients']))
        print("To be eaten for " + recipe['meal'] + ".")
        print(f"Takes {recipe['prep_time']} minutes of cooking")
        print("\n")

def print_recipe():
    print("Please enter the recipe's name to get its details:")
    recipe = prompt()
    if recipe in recipes:
        print(f"Recipe for {recipe}:")
        print("Ingredients list: " + str(recipes[recipe]['ingredients']))
        print("To be eaten for " + recipes[recipe]['meal'] + ".")
        print(f"Takes {recipes[recipe]['prep_time']} minutes of cooking")
    else:
        print("This recipe doesn't exist.")

options = {
    1: {'text': "Add a recipe", 'func': add_recipe},
    2: {'text': "Delete a recipe", 'func': delete_recipe},
    3: {'text': "Print a recipe", 'func': print_recipe},
    4: {'text': "Print the cookbook", 'func': print_cookbook},
    5: {'text': 'Quit', 'func': exit},
}

def main():
    while True:
        options[prompt_select()]['func']()


if __name__ == "__main__":
    main()