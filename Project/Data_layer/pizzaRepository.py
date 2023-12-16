import json
import os
from abstract import *
from pizza import Pizza


class PizzaRepository:
    def __init__(self) -> None:
        self.__filename = "PizzaManagerData.json"

    def __str__(self) -> str:
        return f"FileName: {self.__filename}"

    def create_file(self) -> None:
        path = f"./{self.__filename}"
        check_file = os.path.isfile(path)
        if check_file == False:
            with open(self.__filename, "w", newline="") as file:
                pass

    def save_items(self, items: list[Pizza]) -> None:
        with open(self.__filename, "w", newline="") as file:
            jsonData = {}
            for i, item in enumerate(items):
                itemJsonName = f"pizza_{i}"
                jsonData[itemJsonName] = item.convert_to_dict_for_db()
            json_object = json.dumps(jsonData, indent=4)
            file.write(json_object)

    def get_items(self) -> list[Pizza]:
        resultData = []
        with open(self.__filename, "r", newline="") as file:
            jsonData = json.load(file)
            for name in jsonData:
                data = jsonData[name]
                resultData.append(Pizza(data["name"], data["description"], data["basePrice"], PizzaSize(data["size"]), data["recipe"], PizzaCategory(data["category"])))
        return resultData
