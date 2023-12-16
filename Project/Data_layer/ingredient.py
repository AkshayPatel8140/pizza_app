from abstract import Display, IngredientCategory
from datetime import date


class Ingredient(Display):
    def __init__(self, name: str, quantity: int, unit: str, reorder_level: int, category: IngredientCategory):
        self.__name = name
        self.__quantity = quantity
        self.__unit = unit
        self.__reorder_level = reorder_level
        self.__category = category

    @property
    def name(self) -> str:
        return self.__name

    @property
    def unit(self) -> str:
        return self.__unit

    @property
    def quantity(self) -> float:
        return self.__quantity

    @quantity.setter
    def quantity(self, value: float) -> None:
        self.__quantity = value

    @property
    def reorder_level(self) -> int:
        return self.__reorder_level

    def __str__(self) -> str:
        output = ""
        output += f"\nname: {self.__name}, "
        output += f"Quantity: {self.__quantity}, "
        output += f"Unit: {self.__unit}, "
        output += f"Reorder Level: {self.__reorder_level}, "
        output += f"Category: {self.__category.value}"
        return output

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, item: object) -> bool:
        if isinstance(item, Ingredient):
            return self.__name.lower() == item.__name.lower()
        return False

    def convert_to_dict_for_db(self) -> dict:
        dct = {}
        dct["name"] = self.__name
        dct["quantity"] = self.__quantity
        dct["unit"] = self.__unit
        dct["reorderLevel"] = self.__reorder_level
        dct["category"] = self.__category.value
        return dct

    def display(self):
        print(self)

    def add_quantity(self, new_quantity):
        self.__quantity += new_quantity

    def remove_quantity(self, new_quantity):
        if self.__quantity < new_quantity:
            self.__quantity = 0
        else:
            self.__quantity -= new_quantity

    def update_quantity(self, new_quantity):
        self.__quantity = new_quantity

    def update_price(self, new_price):
        if self.__price != new_price:
            self.__price = new_price


def main():
    print("Ingredient")


if __name__ == "__main__":
    main()
