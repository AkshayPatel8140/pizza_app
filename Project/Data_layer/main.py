from ingredientManager import IngredientManager
from orderManager import OrderManager
from pizzaManager import PizzaManager
from recipeManager import RecipeManager
from sideDishManager import SideDishManager


def mainmenu():
    print("\n=====SFBU Pizza Store=====")
    print("1. Ingredient Management")
    print("2. Pizza Management")
    print("3. Recipe Management")
    print("4. SideDish Management")
    print("5. Order Management")
    print("6. Exit")


def ingredientMenu():
    print("\n=== Ingredient Management ===")
    print("1. Get list of Ingredient")
    print("2. Search Ingredient by name")
    print("3. Add Ingredient")
    print("4. Delete Ingredient")
    print("5. Exit")


def ingredientManagement():
    while True:
        ingredientMenu()
        ingredientMenuChoice = input("Please select you choice: ")
        if ingredientMenuChoice.isdigit():
            ingredientMenuChoice = int(ingredientMenuChoice)
            if ingredientMenuChoice == 1:
                pass
            elif ingredientMenuChoice == 2:
                pass
            elif ingredientMenuChoice == 3:
                pass
            elif ingredientMenuChoice == 4:
                pass
            elif ingredientMenuChoice == 5:
                break
            else:
                print("\n!!Please Enter proper choice to manage Ingredient !!")
        else:
            print("\n!! Please enter proper value to manage Ingredient !!")
    return False


def main():
    orderManager = OrderManager()
    count = True
    while count is True:
        mainmenu()
        mainmenuChoice = input("Please select you choice: ")
        if mainmenuChoice.isdigit():
            mainmenuChoice = int(mainmenuChoice)
            if mainmenuChoice == 1:
                ingredientMenuResponse = ingredientMenu()
            elif mainmenuChoice == 2:
                pass
            elif mainmenuChoice == 3:
                pass
            elif mainmenuChoice == 4:
                pass
            elif mainmenuChoice == 5:
                pass
            elif mainmenuChoice == 6:
                count = False
            else:
                print("\n!!Please Enter proper choice !!")
        else:
            print("\n!! Please enter proper choice !!")


if __name__ == "__main__":
    main()
