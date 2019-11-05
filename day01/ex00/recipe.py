class Recipe:

    name = ""
    cooking_lvl = range(1, 6)
    cooking_time = 0
    ingredients = []
    description = ""
    recipe_type = ""

    def __init__(self, **kwargs):

        required_args = {
            'name': None, 'cooking_lvl': range(1, 6), 'cooking_time': 0,
            'ingredients': [], 'recipe_type': ["startes", "lunch", "dessert"]
        }

        if not all([True if x in kwargs else False for x in required_args]):
            raise ValueError('Missing required arguments')

        for key in kwargs:

            if key == "recipe_type" and not kwargs[key] in required_args[key]:
                raise ValueError(f'Invalid valueof recipe_type, has to be one of {required_args[key]}')

            if key == "cooking_lvl" and not kwargs[key] in required_args[key]:
                raise ValueError('cooking_lvl no in range 1-5')

            if key == "cooking_time" and kwargs[key] <= 0:
                raise ValueError('Invalid cooking time')

            if key == "name" and not isinstance(kwargs[key], str):
                raise ValueError('Invalid name input')

            if key == "ingredients" and (not isinstance(kwargs[key], list) or not all(map(lambda x: isinstance(x, str), kwargs[key]))):
                raise ValueError('Invalid ingredients input')

            setattr(self, key, kwargs[key])


    def __str__(self):
        """ Return the string to print with the recipe info """
        return f"Name: {self.name}" +\
               f"Cooking level: {self.cooking_lvl}" +\
               f"Cooking time: {self.cooking_time}" +\
               f"Ingredients: {str(self.ingredients)}" +\
               f"Description: {self.description}" +\
               f"Recipe type: {self.recipe_type}"