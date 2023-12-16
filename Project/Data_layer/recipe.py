from abstract import Display
from ingredient import Ingredient
from typing import Callable
from functools import reduce


class Recipe(Display):
    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__ingredients: list[tuple[str, int]] = []
        # self.__ingredientsNew: dict[str, int] = {"Pepperoni": 2, "Hum": 2, "Bacon": 4}
        self.__ingredientsNew: dict[str, int] = {}

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    def __str__(self) -> str:
        output = ""
        output += f"Recipe name: {self.__name}, "
        output += f"Ingredients: {self.__ingredientsNew}"
        return output

    def __eq__(self, item: object) -> bool:
        if isinstance(item, Recipe):
            return item.name.lower() == self.__name.lower()
        return False

    def __repr__(self) -> str:
        output = f"Name: {self.__name}: "
        output += f"Ingredients: {self.__ingredientsNew}"
        return "\n{ " + str(output) + " }"

    def convert_to_list_for_db(self) -> list[int | float | str]:
        lst = []
        ingredientItemList = ""
        lengthOfIngredients = len(self.__ingredientsNew)
        lst.append(self.__name)
        for i, item in enumerate(self.__ingredientsNew):
            ingredientItemList += f"{item}-{self.__ingredientsNew[item]}"
            if i < lengthOfIngredients - 1:
                ingredientItemList += "/"
        lst.append(ingredientItemList)
        return lst

    def convert_to_dict_for_db(self) -> dict:
        dct = {}
        dct["name"] = self.__name
        dct["ingredients"] = self.__ingredientsNew
        return dct

    def get_ingredient_name(self) -> str:
        listOfIngredients: str = ""
        lengthOfIngredients = len(self.__ingredientsNew)
        for i, item in enumerate(self.__ingredientsNew):
            print(item, self.__ingredientsNew[item])
            listOfIngredients += f"{item}"
            if i < lengthOfIngredients - 1:
                listOfIngredients += ", "
        return listOfIngredients

    def display(self):
        print(str(self))

    def add_ingredient(self, ingredients_name: str, quantity: int) -> bool:
        if ingredients_name in self.__ingredientsNew:
            self.__ingredientsNew[ingredients_name] += quantity
        else:
            self.__ingredientsNew[ingredients_name] = quantity
        return True

    def remove_all_ingredient(self) -> None:
        self.__ingredientsNew = {}

    def remove_ingredient(self, ingredient_name: str) -> bool:
        del self.__ingredientsNew[ingredient_name]
        return True


def main():
    print("Recipe")
    recipe = Recipe("Recipe name")
    print(recipe)


if __name__ == "__main__":
    main()
