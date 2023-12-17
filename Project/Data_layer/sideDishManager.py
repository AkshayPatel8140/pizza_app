from abstract import Display
from sideDish import SideDish
from sideDishRepository import SideDishRepository


class SideDishManager(Display):
    def __init__(self) -> None:
        self.__sideDishList: list[SideDish] = []
        self.__repo = SideDishRepository()
        self.__repo.create_file()
        self.read_from_db()

    def __str__(self) -> str:
        output = ""
        output += "\nSide Dish Details\n"
        output += f"Side dishes: {self.__sideDishList}"
        return output

    def save_to_db(self) -> None:
        self.__repo.save_items(self.__sideDishList)

    def read_from_db(self) -> None:
        data = self.__repo.get_items()
        self.__sideDishList = data

    def add_dish(self, sideDish: SideDish) -> None:
        if sideDish not in self.__sideDishList:
            self.__sideDishList.append(sideDish)
        else:
            for dish in self.__sideDishList:
                if dish == sideDish:
                    dish.addQuantity(sideDish.quantity)
                    break
        self.save_to_db()
        self.check_reorder_levels()

    def remove_dish(self, name: str) -> bool:
        for i, dish in enumerate(self.__sideDishList):
            if dish.name.lower() == name.lower():
                self.__sideDishList.pop(i)
                self.save_to_db()
                return True
        self.save_to_db()
        return False

    def get_sideDish_by_name(self, name) -> None | SideDish:
        for dish in self.__sideDishList:
            if dish.name.lower() == name.lower():
                return dish
        return None

    def add_quantity(self, sideDishName: str, NewQuantity: int) -> bool:
        """Add the NewQuantity only"""
        for i, dish in enumerate(self.__sideDishList):
            if dish.name == sideDishName:
                self.__sideDishList[i].addQuantity(NewQuantity)
                self.save_to_db()
                return True
        return False

    def remove_quantity(self, sideDishName: str, NewQuantity: int) -> bool:
        """Add the only Quantity which you want to remove"""
        for i, dish in enumerate(self.__sideDishList):
            if dish.name == sideDishName:
                self.__sideDishList[i].removeQuantity(NewQuantity)
                self.save_to_db()
                return True
        return False

    def update_sideDish(self, exitingDish: SideDish, name: str, quantity: int, description: str, reorder_level: int) -> None:
        for dish in self.__sideDishList:
            if dish == exitingDish:
                if name != "":
                    dish.name = name
                dish.addQuantity(quantity)
                if description != "":
                    dish.description = description
                exitingDish.reorder_level = reorder_level
                break
        self.save_to_db()
        self.check_reorder_levels()

    def list_dish(self) -> list[str]:
        dishes: list[str] = []
        for dish in self.__sideDishList:
            dishes.append(dish.name)
        return dishes

    def check_reorder_levels(self):
        for ingredient in self.__sideDishList:
            if ingredient.quantity < ingredient.reorder_level:
                print(f"\n{ingredient.name} is Low in the quantity, Please Load More!\n")

    def display(self):
        print("\nSide Dish Inventory Details\n")
        for ingredient in self.__sideDishList:
            print(f"{ingredient.name}({ingredient.quantity}): ${ingredient.price}")


def main():
    print("sideDishManager")
    sideDishManager = SideDishManager()
    # sideDishManager.display()
    # sideDishManager.add_dish(SideDish("Caesar Salad", 50, "Caesar Salad Description", 10, 2, SiDi.APPETIZERS))
    # sideDishManager.add_dish(SideDish("Tossed Salad", 50, "Tossed Salad Description", 10, 2, SiDi.APPETIZERS))
    # sideDishManager.add_dish(SideDish("Assistant Pop", 50, "Assistant Pop Description", 10, 2, SiDi.APPETIZERS))
    # sideDishManager.add_dish(SideDish("Assistant Juice", 50, "Assistant Juice Description", 10, 2, SiDi.BEVERAGES))
    # sideDishManager.add_dish(SideDish("Water", 50, "Water Description", 10, 2, SiDi.BEVERAGES))
    # sideDishManager.add_dish(SideDish("Cookies", 50, "Cookies Description", 10, 2, SiDi.DESSERTS))
    # sideDishManager.add_dish(SideDish("Cookies1", 50, "Cookies Description", 10, 2, SiDi.DESSERTS))
    sideDishManager.display()
    print(sideDishManager.list_dish())
    # sideDishManager.remove_dish("Cookies1", SiDi.DESSERTS)
    # sideDishManager.display()
    # print(sideDishManager.list_dish())


if __name__ == "__main__":
    main()
