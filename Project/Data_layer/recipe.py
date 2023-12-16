from abstract import Display
from ingredient import Ingredient
from typing import Callable
from functools import reduce


class Recipe(Display):
    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__ingredients: dict[str, int] = {}

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    def __str__(self) -> str:
        output = ""
        output += f"Recipe name: {self.__name}, "
        output += f"Ingredients: {self.__ingredients}"
        return output

    def __eq__(self, item: object) -> bool:
        if isinstance(item, Recipe):
            return item.name.lower() == self.__name.lower()
        return False

    def __repr__(self) -> str:
        output = f"Name: {self.__name}: "
        output += f"Ingredients: {self.__ingredients}"
        return "\n{ " + str(output) + " }"

    def convert_to_dict_for_db(self) -> dict:
        dct = {}
        dct["name"] = self.__name
        dct["ingredients"] = self.__ingredients
        return dct

    def get_ingredient_name(self) -> str:
        listOfIngredients: str = ""
        lengthOfIngredients = len(self.__ingredients)
        for i, item in enumerate(self.__ingredients):
            print(item, self.__ingredients[item])
            listOfIngredients += f"{item}"
            if i < lengthOfIngredients - 1:
                listOfIngredients += ", "
        return listOfIngredients

    def remove_ingredient_quantity_in_db(self, db) -> None:
        for ingredients_name in self.__ingredients:
            db.remove_quantity(ingredients_name, self.__ingredients[ingredients_name])

    def add_ingredient_quantity_in_db(self, db) -> None:
        for ingredients_name in self.__ingredients:
            db.add_quantity(ingredients_name, self.__ingredients[ingredients_name])

    def display(self):
        print(str(self))

    def add_ingredient(self, ingredients_name: str, quantity: int) -> bool:
        if ingredients_name in self.__ingredients:
            self.__ingredients[ingredients_name] += quantity
        else:
            self.__ingredients[ingredients_name] = quantity
        return True

    def remove_all_ingredient(self) -> None:
        self.__ingredients = {}

    # def remove_ingredient(self, ingredient_name: str) -> bool:
    #     del self.__ingredients[ingredient_name]
    #     return True


def main():
    print("Recipe")
    recipe = Recipe("Recipe name")
    print(recipe)


if __name__ == "__main__":
    main()
