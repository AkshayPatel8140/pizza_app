import json
import os
from abstract import *
from recipe import Recipe


class RecipeRepository:
    def __init__(self) -> None:
        self.__filename = "RecipeManagerData.json"

    def __str__(self) -> str:
        return f"FileName: {self.__filename}"

    def create_file(self) -> None:
        path = f"./{self.__filename}"
        check_file = os.path.isfile(path)
        if check_file == False:
            with open(self.__filename, "w", newline="") as file:
                pass

    def save_items(self, items: list[Recipe]) -> None:
        # print("🚀 ~ file: recipeRepository.py:25 ~ items:", items)
        with open(self.__filename, "w", newline="") as file:
            jsonData = {}
            for i, item in enumerate(items):
                itemJsonName = f"recipe_{i}"
                jsonData[itemJsonName] = item.convert_to_dict_for_db()
            json_object = json.dumps(jsonData, indent=4)
            file.write(json_object)

    def get_items(self) -> list[Recipe]:
        resultData = []
        with open(self.__filename, "r", newline="") as file:
            jsonData = json.load(file)
            for name in jsonData:
                data = jsonData[name]
                recipe = Recipe(data["name"])
                Ingredients = data["ingredients"]
                for ingredientItem in Ingredients:
                    recipe.add_ingredient(ingredientItem, Ingredients[ingredientItem])
                resultData.append(recipe)
            return resultData
