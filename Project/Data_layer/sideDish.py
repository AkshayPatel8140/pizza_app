from typing import Optional
from abstract import Display, SideDishesCategory as SiDi
from recipe import Recipe
from ingredient import Ingredient
from functools import reduce


class SideDish(Display):
    def __init__(self, name: str, quantity: int, description: str, price: float, reorder_level: int, category: SiDi) -> None:
        self.__name = name
        self.__quantity = quantity
        self.__description = description
        self.__reorder_level = reorder_level
        self.__price = price
        self.__category = category

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def quantity(self) -> int:
        return self.__quantity

    @property
    def description(self) -> str:
        return self.__description

    @property
    def price(self) -> float:
        return self.__price

    @description.setter
    def description(self, value: str) -> None:
        self.__description = value

    @quantity.setter
    def quantity(self, value: int) -> None:
        self.__quantity = value

    @property
    def reorder_level(self) -> int:
        return self.__reorder_level

    @reorder_level.setter
    def reorder_level(self, value: int) -> None:
        self.__reorder_level = value

    @property
    def category(self) -> SiDi:
        return self.__category

    def __str__(self) -> str:
        output = ""
        output += f"Name: {self.__name}, "
        output += f"Quantity: {self.__quantity}, "
        output += f"Price: {self.__price}, "
        output += f"Reorder level: {self.__reorder_level}, "
        output += f"Description: {self.__description}, "
        output += f"Category: {self.__category.value}"
        return output

    def __eq__(self, item: object) -> bool:
        if isinstance(item, SideDish):
            return self.__name == item.name and self.__category == item.__category
        return False

    def __repr__(self) -> str:
        return "\n{ " + str(self) + " }"

    def addQuantity(self, quantity: int = 0) -> None:
        self.__quantity += quantity

    def removeQuantity(self, quantity: int = 0) -> None:
        self.__quantity -= quantity

    def display(self):
        return print(str(self))

    def convert_to_list_for_db(self) -> list[int | float | str]:
        lst = []
        lst.append(self.__name)
        lst.append(self.__quantity)
        lst.append(self.__description)
        lst.append(self.__price)
        lst.append(self.__reorder_level)
        lst.append(self.__category.value)
        return lst

    def convert_to_dict_for_db(self) -> dict:
        dct = {}
        dct["name"] = self.__name
        dct["quantity"] = self.__quantity
        dct["description"] = self.__description
        dct["price"] = self.__price
        dct["reorderLevel"] = self.__reorder_level
        dct["category"] = self.__category.value
        return dct


# class Appetizers(SideDish):
#     def __init__(self, name: str, quantity: int, description: str, price: float, reorder_level: int) -> None:
#         super().__init__(name, quantity, description, price, reorder_level)
#         self.__category = SiDi.APPETIZERS


# class Desserts(SideDish):
#     def __init__(self, name: str, quantity: int, description: str, price: float, reorder_level: int) -> None:
#         super().__init__(name, quantity, description, price, reorder_level)
#         self.__category = SiDi.DESSERTS


# class Beverages(SideDish):
#     def __init__(self, name: str, quantity: int, description: str, price: float, reorder_level: int) -> None:
#         super().__init__(name, quantity, description, price, reorder_level)
#         self.__category = SiDi.BEVERAGES


# class SideDishFactory:
#     @staticmethod
#     def get_product(product: SiDi, name: str, quantity: int, description: str, price: float, reorder_level: int) -> Optional[SideDish]:
#         if product == SiDi.APPETIZERS:
#             return Appetizers(name, quantity, description, price, reorder_level)
#         elif product == SiDi.DESSERTS:
#             return Desserts(name, quantity, description, price, reorder_level)
#         elif product == SiDi.BEVERAGES:
#             return Beverages(name, quantity, description, price, reorder_level)
#         else:
#             return None


def main():
    pass
    # sideDishFactory = SideDishFactory()
    # appetizers = sideDishFactory.get_product(SiDi.APPETIZERS, "Caesar Salad", 15, "Caesar Salad Description", 4.30, 5)


if __name__ == "__main__":
    main()
