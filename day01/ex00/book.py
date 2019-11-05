from recipe import Recipe
import datetime


class Book():

    name = ""
    last_update = datetime
    creation_date = datetime
    recipes_list = {
        "starter": [],
        "lunch": [],
        "dessert": []
    }

    def add_recipe(self, recipe):
        """ Add a recipe to the book and update last_update """
        if not isinstance(recipe, Recipe):
            raise ValueError('Input is not an instance of Recipe')



