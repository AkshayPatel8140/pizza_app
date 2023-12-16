import csv
import copy
import json
from abstract import *
import os

from ingredient import Ingredient
from sideDish import SideDish


class SideDishRepository:
    def __init__(self) -> None:
        self.__filename = "SideDishManagerData.json"

    def __str__(self) -> str:
        return f"FileName: {self.__filename}"

    def create_file(self) -> None:
        path = f"./{self.__filename}"
        check_file = os.path.isfile(path)
        if check_file == False:
            with open(self.__filename, "w", newline="") as file:
                pass

    def save_items(self, items: list[SideDish]) -> None:
        with open(self.__filename, "w", newline="") as file:
            jsonData = {}
            for i, item in enumerate(items):
                itemJsonName = f"sideDish_{i}"
                jsonData[itemJsonName] = item.convert_to_dict_for_db()
            json_object = json.dumps(jsonData, indent=4)
            file.write(json_object)

    def get_items(self) -> list[SideDish]:
        resultData = []
        with open(self.__filename, "r", newline="") as file:
            jsonData = json.load(file)
            for name in jsonData:
                data = jsonData[name]
                resultData.append(SideDish(data["name"], data["quantity"], data["description"], data["price"], data["reorderLevel"], SideDishesCategory(data["category"])))
        return resultData


# class SideDishRepository:
#     def __init__(self) -> None:
#         self.__filename = "SideDishManagerData.csv"

#     def __str__(self) -> str:
#         return f"FileName: {self.__filename}"

#     def create_file(self) -> None:
#         path = f"./{self.__filename}"
#         check_file = os.path.isfile(path)
#         if check_file == False:
#             with open(self.__filename, "w", newline="") as file:
#                 pass

#     def save_items(self, items: list[SideDish]) -> None:
#         with open(self.__filename, "w", newline="") as file:
#             writer = csv.writer(file)
#             for item in items:
#                 writer.writerow(item.convert_to_list_for_db())

#     def get_items(self) -> list[SideDish]:
#         resultData = []
#         with open(self.__filename, "r", newline="") as file:
#             reader = csv.reader(file)
#             for row in reader:
#                 resultData.append(SideDish(row[0], int(row[1]), row[2], float(row[3]), int(row[4]), SideDishesCategory(row[5])))
#         return resultData
