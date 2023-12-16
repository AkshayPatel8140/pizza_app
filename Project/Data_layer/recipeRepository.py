import csv
import copy
import json
from abstract import *
import os
from ingredientManager import IngredientManager

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

            # reader = csv.reader(file)
            # for row in reader:
            #     recipeIngredient = row[1].split("/")
            #     recipe = Recipe(row[0])
            #     for recipeIngredientItem in recipeIngredient:
            #         [name, quantity] = recipeIngredientItem.split("-")
            #         recipe.add_ingredient(name, int(quantity))
            #     resultData.append(recipe)
        # return resultData


# class RecipeRepository:
#     def __init__(self) -> None:
#         self.__filename = "RecipeManagerData.csv"

#     def __str__(self) -> str:
#         return f"FileName: {self.__filename}"

#     def create_file(self) -> None:
#         path = f"./{self.__filename}"
#         check_file = os.path.isfile(path)
#         if check_file == False:
#             with open(self.__filename, "w", newline="") as file:
#                 pass

#     def save_items(self, items: list[Recipe]) -> None:
#         with open(self.__filename, "w", newline="") as file:
#             writer = csv.writer(file)
#             for item in items:
#                 writer.writerow(item.convert_to_list_for_db())

#     def get_items(self) -> list[Recipe]:
#         resultData = []
#         with open(self.__filename, "r", newline="") as file:
#             reader = csv.reader(file)
#             for row in reader:
#                 recipeIngredient = row[1].split("/")
#                 recipe = Recipe(row[0])
#                 for recipeIngredientItem in recipeIngredient:
#                     [name, quantity] = recipeIngredientItem.split("-")
#                     recipe.add_ingredient(name, int(quantity))
#                 resultData.append(recipe)
#         return resultData
