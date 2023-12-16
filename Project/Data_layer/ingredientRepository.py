import json
import os
from abstract import *
from ingredient import Ingredient


class IngredientRepository:
    def __init__(self) -> None:
        self.__filename = "IngredientManagerData.json"

    def __str__(self) -> str:
        return f"FileName: {self.__filename}"

    def create_file(self) -> None:
        path = f"./{self.__filename}"
        check_file = os.path.isfile(path)
        if check_file == False:
            with open(self.__filename, "w", newline="") as file:
                pass

    def save_items(self, itemsIngredient: dict[str, Ingredient]) -> None:
        with open(self.__filename, "w", newline="") as file:
            jsonData = {}
            for item in itemsIngredient:
                jsonData[item] = itemsIngredient[item].convert_to_dict_for_db()
            json_object = json.dumps(jsonData, indent=4)
            file.write(json_object)

    def get_items(self) -> dict[str, Ingredient]:
        resultData = {}
        with open(self.__filename, "r", newline="") as file:
            jsonData = json.load(file)
            for name in jsonData:
                data = jsonData[name]
                resultData[name] = Ingredient(data["name"], data["quantity"], data["unit"], data["reorderLevel"], IngredientCategory(data["category"]))
            return resultData
