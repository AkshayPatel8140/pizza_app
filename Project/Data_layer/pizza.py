from abstract import Display, PizzaCategory, PizzaSize


class Pizza(Display):
    def __init__(self, name: str, description: str, basePrice: float, size: PizzaSize, recipe: str, category: PizzaCategory) -> None:
        self.__name = name
        self.__description = description
        self.__basePrice = basePrice
        self.__size = size
        self.__recipe = recipe
        self.__category = category

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def basePrice(self) -> float:
        return self.__basePrice

    @property
    def size(self) -> PizzaSize:
        return self.__size

    @size.setter
    def size(self, value: PizzaSize) -> None:
        self.__size = value

    @property
    def recipe(self) -> str:
        return self.__recipe

    @property
    def category(self) -> PizzaCategory:
        return self.__category

    def __str__(self) -> str:
        output = ""
        output += f"Name: {self.__name}, "
        output += f"Description: {self.__description}, "
        output += f"Price: {self.__basePrice}, "
        output += f"Size: {self.__size.value}, "
        output += f"Recipe: {self.__recipe}, "
        output += f"Category: {self.__category.value}"
        return output

    def __eq__(self, item: object) -> bool:
        if isinstance(item, Pizza):
            return self.name == item.name and self.category == item.category and self.size == item.size
        return False

    def __repr__(self) -> str:
        return "\n{ " + str(self) + " }"

    def get_price_based_on_size(self) -> float:
        if self.__size.value == PizzaSize.MEDIUM.value:
            return self.__basePrice * 2
        elif self.__size.value == PizzaSize.LARGE.value:
            return self.__basePrice * 3
        elif self.__size.value == PizzaSize.EXTRA_LARGE.value:
            return self.__basePrice * 4
        else:
            return self.__basePrice

    def check_by_category(self, category: PizzaCategory) -> bool:
        return self.category.value == category.value

    def display(self):
        print(str(self))

    def convert_to_dict_for_db(self) -> dict:
        dct = {}
        dct["name"] = self.__name
        dct["description"] = self.__description
        dct["basePrice"] = self.__basePrice
        dct["size"] = self.__size.value
        dct["recipe"] = self.__recipe
        dct["category"] = self.__category.value
        return dct


def main():
    pizza = Pizza("Vegetarian", "Mushrooms, Olives, Onion, Peppers, Tomato", 19.50, PizzaSize.SMALL, "testDemo", PizzaCategory.VEGETARIAN)
    print("🚀 ~ file: pizza.py:67 ~ pizza:", pizza)


if __name__ == "__main__":
    main()
