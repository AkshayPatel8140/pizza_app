import csv
import copy
import json
from abstract import *
import os

from ingredient import Ingredient
from order import Order
from pizza import Pizza
from sideDish import SideDish
from ingredient import Ingredient


class OrderRepository:
    def __init__(self) -> None:
        self.__filename = "OrderManagerData.json"

    def __str__(self) -> str:
        return f"FileName: {self.__filename}"

    def create_file(self) -> None:
        path = f"./{self.__filename}"
        check_file = os.path.isfile(path)
        if check_file == False:
            with open(self.__filename, "w", newline="") as file:
                pass

    def save_items(self, items: list[Order]) -> None:
        with open(self.__filename, "w", newline="") as file:
            jsonData = {}
            for item in items:
                itemJsonName = f"{item.order_id}"
                jsonData[itemJsonName] = item.convert_to_dict_for_db()
            json_object = json.dumps(jsonData, indent=4)
            file.write(json_object)

    def get_items(self) -> list[Order]:
        resultData = []
        with open(self.__filename, "r", newline="") as file:
            jsonData = json.load(file)
            for name in jsonData:
                data = jsonData[name]
                order = Order(data["order_id"], data["c_name"], data["c_email"], data["c_phone_no"], data["compony"], data["d_date"], data["d_time"])
                pizza_list: dict = data["pizza_list"]
                for pizzaItem in pizza_list.values():
                    create_pizza = Pizza(pizzaItem["name"], pizzaItem["description"], float(pizzaItem["basePrice"]), PizzaSize(pizzaItem["size"]), pizzaItem["recipe"], PizzaCategory(pizzaItem["category"]))
                    order.add_remove_pizza_order(create_pizza, pizzaItem["quantity"])
                sideDish_list: dict = data["sideDish_list"]
                for sideDishItem in sideDish_list.values():
                    order.add_side_dish_in_order(sideDishItem["name"], int(sideDishItem["quantity"]))
                resultData.append(order)
        return resultData
