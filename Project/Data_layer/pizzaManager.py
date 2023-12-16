from typing import Optional
from abstract import Display, PizzaCategory
from pizzaRepository import PizzaRepository
from pizza import Pizza


class PizzaManager(Display):
    def __init__(self) -> None:
        self.__pizzaList: list[Pizza] = []
        self.__repo = PizzaRepository()
        self.__repo.create_file()
        self.read_from_db()

    def __str__(self) -> str:
        output = "/nPizza Inventory Data\n"
        output += f"Pizza list: {self.__pizzaList}"
        return output

    def save_to_db(self) -> None:
        self.__repo.save_items(self.__pizzaList)
        self.read_from_db()

    def read_from_db(self) -> None:
        data = self.__repo.get_items()
        self.__pizzaList = data

    def add_new_pizza(self, pizza: Pizza) -> None:
        if pizza not in self.__pizzaList:
            self.__pizzaList.append(pizza)
            self.save_to_db()

    def remove_pizza(self, pizza: Pizza) -> bool:
        for i, pizzaItem in enumerate(self.__pizzaList):
            if pizza == pizzaItem:
                self.__pizzaList.pop(i)
                self.save_to_db()
                return True
        return False

    def search_by_name(self, name: str) -> Optional[Pizza]:
        for pizzaItem in self.__pizzaList:
            if name == pizzaItem.name:
                return pizzaItem
        return None

    def update_pizza(self, name: str, newPizza: Pizza):
        for i, pizzaItem in enumerate(self.__pizzaList):
            if name == pizzaItem.name:
                self.__pizzaList[i] = newPizza
        self.save_to_db()

    def get_pizzaList(self) -> list[Pizza]:
        return self.__pizzaList.copy()

    def get_pizza_by_category(self, category: PizzaCategory) -> list[Pizza]:
        resultList: list[Pizza] = []
        for pizzaItem in self.__pizzaList:
            if pizzaItem.check_by_category(category):
                resultList.append(pizzaItem)
        return resultList

    def display(self):
        print(str(self))


def main():
    pizzaManager = PizzaManager()
    # recipe = Recipe("testDemo")
    # pizza = Pizza("Vegetarian", "Mushrooms, Olives, Onion, Peppers, Tomato", 19.50, PizzaSize.SMALL, "test1", PizzaCategory.VEGETARIAN)
    # pizza1 = Pizza("Vegetarian", "Mushrooms, Olives, Onion, Peppers, Tomato", 15.50, PizzaSize.SMALL, "test1", PizzaCategory.VEGETARIAN)
    # pizza2 = Pizza("Vegetarian2", "Olives, Onion, Peppers, Tomato", 20.50, PizzaSize.MEDIUM, "test2", PizzaCategory.VEGETARIAN)
    # pizza3 = Pizza("Vegetarian3", "Onion, Peppers, Tomato", 25.50, PizzaSize.LARGE, "test2", PizzaCategory.VEGETARIAN)
    # pizzaManager.add_new_pizza(pizza1)
    # pizzaManager.add_new_pizza(pizza2)
    # pizzaManager.add_new_pizza(pizza3)
    print(f"pizza list {PizzaCategory.VEGETARIAN}", pizzaManager.get_pizza_by_category(PizzaCategory.VEGETARIAN))
    pizzaManager.display()


if __name__ == "__main__":
    main()
