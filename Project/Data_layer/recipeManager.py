from abstract import Display
from ingredientManager import IngredientManager
from recipe import Recipe
from ingredient import Ingredient
from functools import reduce

from recipeRepository import RecipeRepository


class RecipeManager(Display):
    def __init__(self) -> None:
        self.__recipeList: list[Recipe] = []
        self.repo = RecipeRepository()
        self.repo.create_file()
        self.read_from_db()

    def __str__(self) -> str:
        output = ""
        output += "\nRecipe Inventory Details\n"
        output += f"Recipes: {self.__recipeList}"
        return output

    def save_to_db(self) -> None:
        self.repo.save_items(self.__recipeList)
        self.read_from_db()

    def read_from_db(self) -> None:
        data = self.repo.get_items()
        self.__recipeList = data

    def add_recipe(self, recipe: Recipe) -> bool:
        if recipe not in self.__recipeList:
            self.__recipeList.append(recipe)
            self.save_to_db()
            return True
        return False

    def remove_recipe(self, recipe_name: str) -> bool:
        for i, recipeItem in enumerate(self.__recipeList):
            if recipeItem.name.lower() == recipe_name.lower():
                self.__recipeList.pop(i)
                self.save_to_db()
                return True
        return False

    def get_recipe_by_name(self, name) -> None | Recipe:
        for recipe in self.__recipeList:
            if recipe.name.lower() == name.lower():
                return recipe
        return None

    def update_recipe(self, recipe: Recipe, newName: str, newIngredients: dict[str, int]):
        for recipeItem in self.__recipeList:
            if recipeItem == recipe:
                if newName != "":
                    recipeItem.name = newName
                for ingredient in newIngredients:
                    recipeItem.add_ingredient(ingredient, newIngredients[ingredient])
        self.save_to_db()

    def list_recipe(self) -> list[str]:
        recipes: list[str] = []
        for recipe in self.__recipeList:
            recipes.append(recipe.name)
        return recipes

    def display(self):
        print("\nRecipe Inventory Details\n")
        for recipe in self.__recipeList:
            print(recipe)


def main():
    print("RecipeManager")
    recipeManager = RecipeManager()
    ingredientManager = IngredientManager()
    recipeManager.display()
    recipe1 = Recipe("test1")
    recipeManager.add_recipe(recipe1)
    # ing1 = ingredientManager.get_ingredient_by_name("Pepperoni")
    # if ing1 is not None:
    #     recipe1.add_ingredient("Pepperoni", 2)
    # ing1 = ingredientManager.get_ingredient_by_name("Hum")
    # if ing1 is not None:
    #     recipe1.add_ingredient("Hum", 2)
    # recipeManager.add_recipe(recipe1)
    recipeManager.update_recipe(recipe1, "", {"Pepperoni": 2, "Hum": 2})

    recipe2 = Recipe("test2")
    recipeManager.add_recipe(recipe2)
    recipeManager.update_recipe(recipe2, "", {"Onion": 13, "Black Olives": 3})
    # ing1 = ingredientManager.get_ingredient_by_name("Onion")
    # if ing1 is not None:
    #     recipe2.add_ingredient("Onion", 3)
    # ing1 = ingredientManager.get_ingredient_by_name("Black Olives")
    # if ing1 is not None:
    #     recipe2.add_ingredient("Black Olives", 3)

    recipeManager.display()

    getRecipe = recipeManager.get_recipe_by_name("test2")
    if getRecipe is not None:
        recipeManager.update_recipe(getRecipe, "test4", {"Onion": 2})
    recipeManager.display()


if __name__ == "__main__":
    main()
