from ingredient import Ingredient
from abstract import Display, IngredientCategory
from ingredientRepository import IngredientRepository
from recipe import Recipe


class IngredientManager(Display):
    def __init__(self) -> None:
        self.__ingredients: dict[str, Ingredient] = {}
        self.repo = IngredientRepository()
        self.repo.create_file()
        self.read_from_db()

    def __str__(self) -> str:
        output = ""
        output += "\nIngredient Inventory Details\n"
        for ingredient in self.__ingredients.values():
            output += f"{ingredient.name}: {ingredient.quantity}{ingredient.unit}\n"
        return output

    def save_to_db(self) -> None:
        self.repo.save_items(self.__ingredients)

    def read_from_db(self) -> None:
        data = self.repo.get_items()
        self.__ingredients = data

    def get_ingredient_by_name(self, name) -> None | Ingredient:
        self.read_from_db()
        for ingredientItem in self.__ingredients.values():
            if ingredientItem.name.lower() == name.lower():
                return ingredientItem
        return None

    def add_ingredient(self, ingredient: Ingredient) -> None:
        if ingredient.name in self.__ingredients:
            self.__ingredients[ingredient.name].add_quantity(ingredient.quantity)
        else:
            self.__ingredients[ingredient.name] = ingredient
        self.save_to_db()

    def add_quantity(self, ingredientName: str, NewQuantity: int) -> bool:
        """Add the NewQuantity only"""
        if ingredientName in self.__ingredients:
            self.__ingredients[ingredientName].add_quantity(NewQuantity)
            self.save_to_db()
            return True
        else:
            return False

    def remove_quantity(self, ingredientName: str, NewQuantity: int) -> bool:
        """Add the only Quantity which you want to remove"""
        if ingredientName in self.__ingredients:
            self.__ingredients[ingredientName].remove_quantity(NewQuantity)
            self.save_to_db()
            return True
        else:
            return False

    def use_ingredient(self, ingredient: Ingredient, quantity: float) -> None:
        self.__ingredients[ingredient.name].quantity -= quantity
        self.save_to_db()
        self.check_reorder_levels()

    def delete_ingredient(self, ingredientName: str) -> bool:
        if ingredientName in self.__ingredients:
            del self.__ingredients[ingredientName]
            self.save_to_db()
            return True
        return False

    def check_reorder_levels(self):
        for ingredient in self.__ingredients.values():
            if ingredient.quantity < ingredient.reorder_level:
                print(f"{ingredient.name} is Low in the quantity, Please Load More!")

    def display(self):
        print("\nIngredient Inventory Details\n")
        for ingredient in self.__ingredients.values():
            print(f"{ingredient.name}: {ingredient.quantity} {ingredient.unit}")


def main():
    ingredientManager = IngredientManager()
    print(ingredientManager)
    # ingredientManager.add_ingredient(Ingredient("Pepperoni", 50, "peas", 5, IngredientCategory.TOPING))
    # ingredientManager.add_ingredient(Ingredient("Hum", 50, "peas", 5, IngredientCategory.TOPING))
    # ingredientManager.add_ingredient(Ingredient("Bacon", 50, "peas", 5, IngredientCategory.TOPING))
    # ingredientManager.add_ingredient(Ingredient("Mushroom", 50, "peas", 5, IngredientCategory.TOPING))
    # ingredientManager.add_ingredient(Ingredient("Onion", 50, "peas", 5, IngredientCategory.TOPING))
    # ingredientManager.add_ingredient(Ingredient("Black Olives", 50, "pack", 5, IngredientCategory.TOPING))
    # ingredientManager.add_ingredient(Ingredient("Tomato Slices", 50, "peas", 5, IngredientCategory.TOPING))
    # ingredientManager.add_ingredient(Ingredient("Extra Cheese", 50, "peas", 5, IngredientCategory.TOPING))
    # ingredientManager.add_ingredient(Ingredient("Pineapple", 50, "pack(10 peas)", 5, IngredientCategory.TOPING))
    ingredientManager.display()


if __name__ == "__main__":
    main()
