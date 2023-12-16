from abstract import *
from ingredient import Ingredient
from ingredientManager import IngredientManager
from order import Order
from orderManager import OrderManager
from pizza import Pizza
from pizzaManager import PizzaManager
from recipe import Recipe
from recipeManager import RecipeManager
from sideDish import SideDish
from sideDishManager import SideDishManager


class PizzaApp:
    def __init__(self) -> None:
        self.__ingredientManager = IngredientManager()
        self.__sideDishManager = SideDishManager()
        self.__recipeManager = RecipeManager()
        self.__pizzaManager = PizzaManager()
        self.__orderManager = OrderManager()

    def show_program_title(self) -> None:
        print("\n===!! SFBU Pizza system !!===\n")

    def show_main_menu(self) -> None:
        print("\n=====SFBU Pizza Store=====")
        print("1. Ingredient Management")
        print("2. SideDish Management")
        print("3. Recipe Management")
        print("4. Pizza Management")
        print("5. Order Management")
        print("6. Exit")

    # Ingredient methods
    def show_Menu_Ingredient_Management(self) -> None:
        print("\n=== Ingredient Management ===")
        print("1. Get list of Ingredient")
        print("2. Search Ingredient by name")
        print("3. Add New Ingredient")
        print("4. Add Ingredient quantity")
        print("5. Remove Ingredient quantity")
        print("6. Delete Ingredient")
        print("7. Exit for Ingredient menu")

    def get_ingredient_category(self) -> IngredientCategory:
        while True:
            print("Select the category of the Ingredient: ")
            print(f"A. {IngredientCategory.BASE.value}")
            print(f"B. {IngredientCategory.TOPING.value}")
            ingredientCategoryChoice = input("Please select you choice: ")
            if ingredientCategoryChoice.lower() == "a":
                return IngredientCategory.BASE
            elif ingredientCategoryChoice.lower() == "b":
                return IngredientCategory.TOPING
            else:
                print("\n!! Please enter the proper choice for Ingredient category !!\n")

    def createIngredient(self) -> Ingredient | None:
        name = input("Please enter name of ingredient: ")
        quantity = input("Please enter quantity of ingredient: ")
        unit = input("Please enter unit of ingredient: ")
        reorderLevelQuantity = input("Please enter reorder level of ingredient: ")
        category = self.get_ingredient_category()

        if name == "":
            print("Name not should be blank")
            return None
        elif unit == "":
            print("unit not should be blank")
            return None
        elif reorderLevelQuantity.isdigit() == False:
            print("Reorder Quantity should be digit")
            return None
        elif quantity.isdigit() == False:
            print("Quantity should be digit")
            return None
        elif int(quantity) <= 0:
            print("Quantity not should be 0")
            return None
        else:
            return Ingredient(name, int(quantity), unit, int(reorderLevelQuantity), category)

    def add_remove_ingredient_quantity_by_name(self, for_add_Quantity=True) -> None:
        ingredient_name = input("Please enter name of ingredient: ")
        if ingredient_name == "":
            print("Name not should be blank")
        quantityMSG = "new added quantity" if for_add_Quantity else "quantity to remove"
        ingredient_new_quantity = input(f"Please enter {quantityMSG} of ingredient: ")
        if ingredient_new_quantity.isdigit() == False:
            print("New Quantity should be digit")
        else:
            result = False
            if for_add_Quantity == True:
                result = self.__ingredientManager.add_quantity(ingredient_name, int(ingredient_new_quantity))
            else:
                result = self.__ingredientManager.remove_quantity(ingredient_name, int(ingredient_new_quantity))
            if result == True:
                print("\nIngredient quantity added successfully\n")
            else:
                print(f"Ingredient not found with the {ingredient_name} name")

    def delete_ingredient_by_name(self) -> None:
        ingredient_name = input("Please enter name of ingredient: ")
        if ingredient_name == "":
            print("Name not should be blank")
        result = self.__ingredientManager.delete_ingredient(ingredient_name)
        if result == True:
            print("\nIngredient deleted added successfully\n")
        else:
            print(f"Ingredient not found with the {ingredient_name} name")

    # SideDish methods
    def show_Menu_SideDish_Management(self) -> None:
        print("\n=== SideMenu Management ===")
        print("1. Get list of SideDish")
        print("2. Search SideDish by name")
        print("3. Add New SideDish")
        print("4. Add SideDish quantity")
        print("5. Remove SideDish quantity")
        print("6. Delete SideDish")
        print("7. Exit for SideDish menu")

    def get_sideDish_category(self) -> SideDishesCategory:
        while True:
            print("Select the category of the sideDish: ")
            print(f"A. {SideDishesCategory.APPETIZERS.value}")
            print(f"B. {SideDishesCategory.BEVERAGES.value}")
            print(f"C. {SideDishesCategory.DESSERTS.value}")
            sideDishesCategoryChoice = input("Please select you choice: ")
            if sideDishesCategoryChoice.lower() == "a":
                return SideDishesCategory.APPETIZERS
            elif sideDishesCategoryChoice.lower() == "b":
                return SideDishesCategory.BEVERAGES
            elif sideDishesCategoryChoice.lower() == "c":
                return SideDishesCategory.DESSERTS
            else:
                print("\n!! Please enter the proper choice for sideDish category !!\n")

    def createSideDish(self) -> SideDish | None:
        name = input("Please enter name of SideDish: ")
        quantity = input("Please enter quantity of sideDish: ")
        description = input("Please enter description of sideDish: ")
        price = input("Please enter price of sideDish: ")
        reorderLevelQuantity = input("Please enter reorder level of sideDish: ")
        category = self.get_sideDish_category()

        if name == "":
            print("Name not should be blank")
            return None
        elif description == "":
            print("Description not should be blank")
            return None
        elif reorderLevelQuantity.isdigit() == False:
            print("Reorder Quantity should be digit")
            return None
        elif quantity.isdigit() == False:
            print("Quantity should be digit")
            return None
        elif is_number_float(price) == False:
            print("Price should be digit")
            return None
        elif int(quantity) <= 0:
            print("Quantity not should be 0")
            return None
        else:
            return SideDish(name, int(quantity), description, float(price), int(reorderLevelQuantity), category)

    def add_remove_sideDish_quantity_by_name(self, for_add_Quantity=True) -> None:
        sideDish_name = input("Please enter name of sideDish: ")
        if sideDish_name == "":
            print("Name not should be blank")
        quantityMSG = "new added quantity" if for_add_Quantity else "quantity to remove"
        ingredient_new_quantity = input(f"Please enter {quantityMSG} of ingredient: ")
        if ingredient_new_quantity.isdigit() == False:
            print("New Quantity should be digit")
        else:
            result = False
            if for_add_Quantity == True:
                result = self.__sideDishManager.add_quantity(sideDish_name, int(ingredient_new_quantity))
            else:
                result = self.__sideDishManager.remove_quantity(sideDish_name, int(ingredient_new_quantity))
            if result == True:
                print("\nSideDish quantity added successfully\n")
            else:
                print(f"SideDish not found with the {sideDish_name} name")

    def delete_sideDish_by_name(self) -> None:
        sideDishName = input("Please enter name of SidDish: ")
        if sideDishName == "":
            print("Name not should be blank")
        result = self.__sideDishManager.remove_dish(sideDishName)
        if result == True:
            print("\nSidDish deleted added successfully\n")
        else:
            print(f"SidDish not found with the {sideDishName} name")

    # Recipe Methods
    def show_Recipe_Management(self) -> None:
        print("\n=== Recipe Management ===")
        print("1. Get list of Recipes")
        print("2. Search Recipe by name")
        print("3. Add New Recipe")
        print("4. Delete Recipe")
        print("5. Update the Recipe")
        print("6. Exit for Recipe menu")

    def addIngredientInRecipe(self, recipe: Recipe) -> Recipe | None:
        confirmCount = True
        while confirmCount:
            print("Ingredient list : ")
            self.__ingredientManager.display()
            ingredientName = input("Please enter the name of the ingredient : ")
            searchIngredient = self.__ingredientManager.get_ingredient_by_name(ingredientName)
            if searchIngredient is not None:
                ingredientQuantity = input(f"Please enter the quantity of the ingredient for the {recipe.name} : ")
                if ingredientQuantity.isdigit():
                    recipe.add_ingredient(searchIngredient.name, int(ingredientQuantity))
                else:
                    print("Quantity should be digit")
            else:
                print(f"ingredient not found with the name : {ingredientName}")

            confirmStatus = input("Do you want add the Ingredient in the recipe? [Y/N]: ")
            if confirmStatus.lower() == "n":
                confirmCount = False

        if confirmCount == False:
            return recipe

    def createRecipe(self):
        name = input("Please enter name of Recipe: ")
        if name == "":
            print("Name not should be blank")
            return None
        searchRecipe = self.__recipeManager.get_recipe_by_name(name)
        if searchRecipe is None:
            recipe = Recipe(name)
            return self.addIngredientInRecipe(recipe)
        else:
            print(f"{name} is already present in the database")
            return None

    def delete_recipe_by_name(self) -> None:
        recipeName = input("Please enter name of recipe: ")
        if recipeName == "":
            print("Name not should be blank")
        result = self.__recipeManager.remove_recipe(recipeName)
        if result == True:
            print("\nRecipe deleted added successfully\n")
        else:
            print(f"Recipe not found with the {recipeName} name")

    def ingredient_list_for_recipe_update(self, recipe: Recipe) -> dict[str, int]:
        newIngredients = {}
        confirmCount = True
        while confirmCount:
            print("Ingredient list : ")
            self.__ingredientManager.display()
            ingredientName = input("Please enter the name of the ingredient : ")
            searchIngredient = self.__ingredientManager.get_ingredient_by_name(ingredientName)
            if searchIngredient is not None:
                ingredientQuantity = input(f"Please enter the quantity of the ingredient for the {recipe.name} : ")
                if ingredientQuantity.isdigit():
                    newIngredients[ingredientName] = ingredientQuantity
                else:
                    print("Quantity should be digit")
            else:
                print(f"ingredient not found with the name : {ingredientName}")

            confirmStatus = input("Do you want add the Ingredient in the recipe? [Y/N]: ")
            if confirmStatus.lower() == "n":
                confirmCount = False

        return newIngredients

    def update_Recipe(self) -> None:
        recipeName = input("Please enter name of recipe: ")
        if recipeName == "":
            print("Name not should be blank")
        searchRecipe = self.__recipeManager.get_recipe_by_name(recipeName)
        if searchRecipe is not None:
            recipeNewName = input("Please enter new name of recipe (blank for no change): ")
            newIngredient = self.ingredient_list_for_recipe_update(searchRecipe)
            self.__recipeManager.update_recipe(searchRecipe, recipeNewName, newIngredient)
        else:
            print(f"{recipeName} is not present in the database")

    # Pizza Methods
    def show_Pizza_Management(self) -> None:
        print("\n=== Pizza Management ===")
        print("1. Get list of Pizza")
        print("2. Search Pizza by name")
        print("3. Add New Pizza")
        print("4. Delete Pizza")
        print("5. Exit for Pizza menu")

    def get_pizza_size(self) -> PizzaSize:
        while True:
            print("Select the size of the Pizza: ")
            print(f"A. {PizzaSize.SMALL.value}")
            print(f"B. {PizzaSize.MEDIUM.value}")
            print(f"C. {PizzaSize.LARGE.value}")
            print(f"D. {PizzaSize.EXTRA_LARGE.value}")
            pizzaSizeChoice = input("Please select you choice: ")
            if pizzaSizeChoice.lower() == "a":
                return PizzaSize.SMALL
            elif pizzaSizeChoice.lower() == "b":
                return PizzaSize.MEDIUM
            elif pizzaSizeChoice.lower() == "c":
                return PizzaSize.LARGE
            elif pizzaSizeChoice.lower() == "d":
                return PizzaSize.EXTRA_LARGE
            else:
                print("\n!! Please enter the proper choice for pizza size !!\n")

    def get_recipe_for_pizza(self) -> str:
        print("Recipe: ", self.__recipeManager.list_recipe())
        while True:
            name = input("\nPlease enter name of Recipe: ")
            if name == "":
                print("Name not should be blank")
            searchRecipe = self.__recipeManager.get_recipe_by_name(name)
            if searchRecipe is not None:
                return searchRecipe.name
            else:
                print(f"{name} is not present in the database")

    def get_category_for_pizza(self) -> PizzaCategory:
        while True:
            print("Select the category of the Pizza: ")
            print(f"A. {PizzaCategory.MEAT_LOVERS.value}")
            print(f"B. {PizzaCategory.SPECIALTY.value}")
            print(f"C. {PizzaCategory.VEGETARIAN.value}")
            pizzaCategoryChoice = input("Please select you choice: ")
            if pizzaCategoryChoice.lower() == "a":
                return PizzaCategory.MEAT_LOVERS
            elif pizzaCategoryChoice.lower() == "b":
                return PizzaCategory.SPECIALTY
            elif pizzaCategoryChoice.lower() == "c":
                return PizzaCategory.VEGETARIAN
            else:
                print("\n!! Please enter the proper choice for pizza Category !!\n")

    def createPizza(self) -> Pizza | None:
        name = input("Please enter name of Pizza: ")
        if name == "":
            print("Name not should be blank")
            return None
        description = input("Please enter description of pizza: ")
        if description == "":
            print("Description not should be blank")
            return None
        basePrice = input("Please enter basePrice of pizza: ")
        if is_number_float(basePrice) == False:
            print("Price should be digit")
            return None
        elif float(basePrice) <= 0:
            print("Price should not be 0")
            return None
        pizzaSize = self.get_pizza_size()
        pizzaRecipe = self.get_recipe_for_pizza()
        pizzaCategory = self.get_category_for_pizza()

        return Pizza(name, description, float(basePrice), pizzaSize, pizzaRecipe, pizzaCategory)

    def deletePizza(self) -> None:
        name = input("Please enter name of Pizza: ")
        if name == "":
            print("Name not should be blank")
            return None
        searchedItem = self.__pizzaManager.search_by_name(name)
        if searchedItem is not None:
            self.__pizzaManager.remove_pizza(searchedItem)
            print("\n!! Pizza removed !!")
        else:
            print("Pizza not found")

    # Order Methods
    def show_Order_Management(self) -> None:
        print("\n=== Order Management ===")
        print("1. Get list of Order")
        print("2. Search Order by name")
        print("3. Search Order by order Id")
        print("4. Add New Order")
        print("5. Delete Order")
        print("6. Exit for Order menu")

    def get_sideDish_for_Order(self) -> dict[str, int]:
        sideDishList = {}
        print("SideDishes :", self.__sideDishManager.list_dish())
        confirmStatus = True
        while confirmStatus:
            name = input("\nPlease enter name of SideDish: ")
            checkSideDish = self.__sideDishManager.get_sideDish_by_name(name)
            if checkSideDish is None:
                print(f"\n{name} dish is not found in the store")
            else:
                sideDishQuantity = input(f"Please enter the quantity of the side dish for the {name} : ")
                if sideDishQuantity.isdigit():
                    sideDishList[name] = int(sideDishQuantity)
                else:
                    print("Quantity should be digit and not in point values")
            confirmStatusValue = input("Do you want to add other the side dish in the order? [Y/N]: ")
            if confirmStatusValue.lower() == "n":
                confirmStatus = False
        return sideDishList

    def get_pizza_for_order(self) -> list[tuple[Pizza, int]]:
        pizzaList = []
        pre_pizza_list = self.__pizzaManager.get_pizzaList()
        pre_pizza_list_length = len(pre_pizza_list)
        for i, pre_pizza in enumerate(pre_pizza_list):
            print(f"{i+1}) Name: {pre_pizza.name}, Size: {pre_pizza.size.value},  Description: {pre_pizza.description} -> Price: ${pre_pizza.basePrice}")
        confirmStatus = True
        while confirmStatus:
            selectedPizzaIndex = input(f"Please select the pizza from above list (1 to {pre_pizza_list_length}): ")
            if selectedPizzaIndex.isdigit():
                pizzaSize = self.get_pizza_size()
                pizzaQuantity = input("Enter the quantity of the pizza : ")
                if pizzaQuantity.isdigit():
                    selectedPizza = self.__pizzaManager.search_by_name(pre_pizza_list[int(selectedPizzaIndex) - 1].name)
                    if selectedPizza is not None:
                        selectedPizza.size = pizzaSize
                        pizzaList.append((selectedPizza, int(pizzaQuantity)))
                else:
                    print("quantity should be in digit")
            else:
                print("Please enter proper selection")
            confirmStatusValue = input("Do you want to add other the pizza in the order? [Y/N]: ")
            if confirmStatusValue.lower() == "n":
                confirmStatus = False
        return pizzaList

    def get_custom_pizza_for_order(self) -> list[tuple[Pizza, int]]:
        pizzaList = []
        confirmStatus = True
        while confirmStatus:
            selectedPizza = self.createPizza()
            pizzaQuantity = input("Enter the quantity of the pizza : ")
            if pizzaQuantity.isdigit():
                pizzaList.append((selectedPizza, int(pizzaQuantity)))
            else:
                print("quantity should be in digit")
            confirmStatusValue = input("Do you want to add other the pizza in the order? [Y/N]: ")
            if confirmStatusValue.lower() == "n":
                confirmStatus = False
        return pizzaList

    def createOrder(self) -> Order | None:
        order_id = self.__orderManager.getLastOrderId() + 1
        c_name = input("Enter customer name : ")
        if c_name == "":
            print("customer name not should be blank")
            return None
        c_email = input("Enter customer email : ")
        if c_email == "":
            print("customer email not should be blank")
            return None
        c_phone_no = input("Enter customer phone number : ")
        if c_phone_no == "":
            print("customer phone Number not should be blank")
            return None
        compony = input("Enter customer compony name : ")
        if compony == "":
            print("customer compony name not should be blank")
            return None
        date = input("Enter order delivery date (MM/DD/YYYY): ")
        if date == "":
            print("order delivery date not should be blank")
            return None
        time = input("Enter order delivery time (HH:MM AM): ")
        if time == "":
            print("order delivery time not should be blank")
            return None

        sideDishList = self.get_sideDish_for_Order()
        prePizzaList = self.get_pizza_for_order()
        confirmForCustomPizza = input("Do you want to add custom pizza in the order? [Y/N]: ")
        customPizzaList = []
        if confirmForCustomPizza.lower() == "y":
            customPizzaList = self.get_custom_pizza_for_order()
        order = Order(order_id, c_name, c_email, c_phone_no, compony, date, time)
        for dish in sideDishList:
            order.add_side_dish_in_order(dish, sideDishList[dish])
            self.__sideDishManager.remove_quantity(dish, sideDishList[dish])
        for pizzaData in prePizzaList:
            order.add_remove_pizza_order(pizzaData[0], pizzaData[1])
            recipeData = self.__recipeManager.get_recipe_by_name(pizzaData[0].recipe)
            if recipeData is not None:
                for i in range(pizzaData[1]):
                    recipeData.remove_ingredient_quantity_in_db(self.__ingredientManager)
        for customPizzaData in customPizzaList:
            order.add_remove_pizza_order(customPizzaData[0], customPizzaData[1])
            recipeData = self.__recipeManager.get_recipe_by_name(customPizzaData[0].recipe)
            if recipeData is not None:
                for i in range(customPizzaData[1]):
                    recipeData.remove_ingredient_quantity_in_db(self.__ingredientManager)
        return order

    def process_command(self, command: int) -> bool:
        count = True
        if command == 1:  # Ingredient Management
            while True:
                self.show_Menu_Ingredient_Management()
                ingredientMenuChoice = input("Please select you choice: ")
                if ingredientMenuChoice.isdigit():
                    ingredientMenuChoice = int(ingredientMenuChoice)
                    if ingredientMenuChoice == 1:  # print the list of the ingredient
                        self.__ingredientManager.read_from_db()
                        self.__ingredientManager.display()
                    elif ingredientMenuChoice == 2:  # Search the ingredient by name
                        search_name = input("Please enter name of ingredient: ")
                        searchedItem = self.__ingredientManager.get_ingredient_by_name(search_name)
                        if searchedItem is not None:
                            searchedItem.display()
                        else:
                            print("Ingredient not found")
                    elif ingredientMenuChoice == 3:  # Add New Ingredient
                        newIngredient = self.createIngredient()
                        if newIngredient is not None:
                            self.__ingredientManager.add_ingredient(newIngredient)
                            print("\nIngredient added successfully\n")
                    elif ingredientMenuChoice == 4:  # Add Ingredient Quantity
                        self.add_remove_ingredient_quantity_by_name(True)
                    elif ingredientMenuChoice == 5:  # Remove Ingredient Quantity
                        self.add_remove_ingredient_quantity_by_name(False)
                    elif ingredientMenuChoice == 6:  # Delete Ingredient
                        self.delete_ingredient_by_name()
                    elif ingredientMenuChoice == 7:
                        break
                    else:
                        print("\n!!Please Enter proper choice to manage Ingredient !!")
                else:
                    print("\n!! Please enter proper value to manage Ingredient !!")
        elif command == 2:  # SideDish Management
            while True:
                self.show_Menu_SideDish_Management()
                sideDishMenuChoice = input("Please select you choice: ")
                if sideDishMenuChoice.isdigit():
                    sideDishMenuChoice = int(sideDishMenuChoice)
                    if sideDishMenuChoice == 1:  # Get list of SideDish
                        self.__sideDishManager.read_from_db()
                        self.__sideDishManager.display()
                    elif sideDishMenuChoice == 2:  # Search SideDish by name
                        search_name = input("Please enter name of sideDish: ")
                        searchedItem = self.__sideDishManager.get_sideDish_by_name(search_name)
                        if searchedItem is not None:
                            searchedItem.display()
                        else:
                            print("SideDish not found")
                    elif sideDishMenuChoice == 3:  # Add New SideDish
                        newSideDish = self.createSideDish()
                        if newSideDish is not None:
                            self.__sideDishManager.add_dish(newSideDish)
                            print("\nIngredient added successfully\n")
                    elif sideDishMenuChoice == 4:  # Add SideDish quantity
                        self.add_remove_sideDish_quantity_by_name(True)
                    elif sideDishMenuChoice == 5:  # Remove SideDish quantity
                        self.add_remove_sideDish_quantity_by_name(False)
                    elif sideDishMenuChoice == 6:  # Delete SideDish
                        self.delete_sideDish_by_name()
                    elif sideDishMenuChoice == 7:  # Exit
                        break
                    else:
                        print("\n!!Please Enter proper choice to manage SideDish !!")
                else:
                    print("\n!! Please enter proper value to manage SideDish !!")
        elif command == 3:  # Recipe Management
            while True:
                self.show_Recipe_Management()
                recipeMenuChoice = input("Please select you choice: ")
                if recipeMenuChoice.isdigit():
                    recipeMenuChoice = int(recipeMenuChoice)
                    if recipeMenuChoice == 1:  # Get list of Recipes
                        self.__recipeManager.read_from_db()
                        self.__recipeManager.display()
                    elif recipeMenuChoice == 2:  # Search Recipes by Name
                        search_name = input("Please enter name of recipe: ")
                        searchedItem = self.__recipeManager.get_recipe_by_name(search_name)
                        if searchedItem is not None:
                            searchedItem.display()
                        else:
                            print("Recipe not found")
                    elif recipeMenuChoice == 3:  # Add New Recipes
                        newRecipe = self.createRecipe()
                        if newRecipe is not None:
                            self.__recipeManager.add_recipe(newRecipe)
                            print("\nRecipe added successfully\n")
                    elif recipeMenuChoice == 4:  # Delete Recipes
                        self.delete_recipe_by_name()
                    elif recipeMenuChoice == 5:  # Update Recipes
                        self.update_Recipe()
                    elif recipeMenuChoice == 6:  # Exit
                        break
                    else:
                        print("\n!!Please Enter proper choice to manage Recipe !!")
                else:
                    print("\n!! Please enter proper value to manage Recipe !!")
        elif command == 4:  # Pizza Management
            while True:
                self.show_Pizza_Management()
                pizzaMenuChoice = input("Please select you choice: ")
                if pizzaMenuChoice.isdigit():
                    pizzaMenuChoice = int(pizzaMenuChoice)
                    if pizzaMenuChoice == 1:  # Get list of Pizza
                        self.__pizzaManager.read_from_db()
                        self.__pizzaManager.display()
                    elif pizzaMenuChoice == 2:  # Get Pizza by name
                        search_name = input("Please enter name of Pizza: ")
                        searchedItem = self.__pizzaManager.search_by_name(search_name)
                        if searchedItem is not None:
                            searchedItem.display()
                        else:
                            print("Pizza not found")
                    elif pizzaMenuChoice == 3:  # Add New Pizza
                        newPizza = self.createPizza()
                        if newPizza is not None:
                            self.__pizzaManager.add_new_pizza(newPizza)
                    elif pizzaMenuChoice == 4:  # Delete Pizza
                        self.deletePizza()
                    elif pizzaMenuChoice == 5:  # Exit
                        break
                    else:
                        print("\n!!Please Enter proper choice to manage Pizza !!")
                else:
                    print("\n!! Please enter proper value to manage Pizza !!")
        elif command == 5:  # Order Management
            # self.__orderManager.read_from_db()
            while True:
                self.show_Order_Management()
                orderMenuChoice = input("Please select you choice: ")
                if orderMenuChoice.isdigit():
                    orderMenuChoice = int(orderMenuChoice)
                    if orderMenuChoice == 1:  # Get list of order
                        self.__orderManager.display()
                    elif orderMenuChoice == 2:  # Search order by name
                        search_name = input("Please enter name of customer: ")
                        searchedOrders = self.__orderManager.get_order_by_name(search_name)
                        if len(searchedOrders) > 0:
                            print("Orders:", searchedOrders)
                        else:
                            print("Order not found")
                    elif orderMenuChoice == 3:  # Search order by order Id
                        search_order_id = input("Please enter order Id: ")
                        if search_order_id.isdigit():
                            searchedOrders = self.__orderManager.get_order_by_order_id(int(search_order_id))
                            if len(searchedOrders) > 0:
                                print("Orders:", searchedOrders)
                            else:
                                print("Order not found")
                        else:
                            print("\n! Please enter proper order Id !")
                    elif orderMenuChoice == 4:  # Add new order
                        newOrder = self.createOrder()
                        if newOrder is not None:
                            self.__orderManager.add_order(newOrder)
                            print("\n!! Order added successfully !!")
                            self.__ingredientManager.check_reorder_levels()
                    elif orderMenuChoice == 5:  # Delete order
                        search_order_id = input("Please enter order Id: ")
                        if search_order_id.isdigit():
                            self.__orderManager.remove_order(int(search_order_id))
                            print("\n!! Order removed successfully !!")
                        else:
                            print("\n! Please enter proper order Id !")
                    elif orderMenuChoice == 6:  # Exit
                        break
                    else:
                        print("\n!!Please Enter proper choice to manage Pizza !!")
                else:
                    print("\n!! Please enter proper value to manage Pizza !!")
        elif command == 6:
            count = False
        else:
            print("\n!!Please Enter proper choice !!")
            count = True

        return count


def main():
    pizzaApp = PizzaApp()
    pizzaApp.show_program_title()
    count = True
    while count is True:
        pizzaApp.show_main_menu()
        mainmenuChoice = input("Please select you choice: ")
        if mainmenuChoice.isdigit():
            mainmenuChoice = int(mainmenuChoice)
            count = pizzaApp.process_command(mainmenuChoice)
        else:
            print("\n!! Please enter proper choice !!")


if __name__ == "__main__":
    main()
