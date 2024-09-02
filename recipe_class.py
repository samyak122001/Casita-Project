class Recipe:
    
    # Define constructor for Recipe object
    def __init__(self, name, ingredients, servings):
        self.name = name
        self.ingredients = ingredients
        self.servings = servings
    
    # Define how instance Recipe class is printed
    def __repr__(self):
        return self.name # just show the recipe name
