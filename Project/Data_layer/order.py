from pizza import Pizza
from sideDish import SideDish
from abstract import Display, PizzaCategory, PizzaSize, SideDishesCategory
from recipe import Recipe
from datetime import date, datetime
from functools import reduce

from sideDishManager import SideDishManager


class Order(Display):
    def __init__(self, order_id: int, name: str, email: str, phone_no: str, compony: str, date: str, time: str) -> None:
        self.__order_id: int = order_id
        self.__c_name: str = name
        self.__c_email: str = email
        self.__c_phone_no: str = phone_no
        self.__compony: str = compony
        self.__order_pizzas: list[tuple[Pizza, int]] = []
        self.__sideDishes: list[tuple[str, int, float]] = []
        self.__total_price: float = self.get_total_price()
        self.__d_date: str = date  # Delivery date
        self.__d_time: str = time  # Delivery time
        self.sideDishesManager = SideDishManager()

    @property
    def order_id(self) -> int:
        return self.__order_id

    @property
    def c_name(self) -> str:
        return self.__c_name

    @property
    def c_email(self) -> str:
        return self.__c_email

    @property
    def c_phone_no(self) -> str:
        return self.__c_phone_no

    @property
    def compony(self) -> str:
        return self.__compony

    @property
    def total_price(self) -> float:
        return self.__total_price

    @property
    def d_date(self) -> str:
        return self.__d_date

    @property
    def d_time(self) -> str:
        return self.__d_time

    def __str__(self) -> str:
        output = ""
        output += f"Order ID: {self.__order_id}\n"
        # output += f"Order Delivery date: {self.__d_datetime.strftime('%m-%d-%Y')}\n"
        output += f"Order Delivery date: {self.__d_date}\n"
        # output += f"Order Delivery time: {self.__d_datetime.strftime('%I:%M:%S %p')}\n"
        output += f"Order Delivery time: {self.__d_time}\n"
        output += f"Customer's Name: {self.__c_name}\n"
        output += f"Customer's Email: {self.__c_email}\n"
        output += f"Customer's Phone Number: {self.__c_phone_no}\n"
        output += f"Compony: {self.__compony}\n"
        output += f"Order Pizza: \n"
        for pizzaItem in self.__order_pizzas:
            output += " { "
            output += f"Name: {pizzaItem[0].name}({pizzaItem[0].size.value}), "
            output += f"Description: {pizzaItem[0].description}" + " } * "
            output += f"Quantity: {pizzaItem[1]} -> "
            output += f"Price: {pizzaItem[0].get_price_based_on_size() * pizzaItem[1]}\n"
        if len(self.__sideDishes) > 0:
            output += f"Order Side Dishes: \n"
            for sideItem in self.__sideDishes:
                sideDish = self.sideDishesManager.get_sideDish_by_name(sideItem[0])
                if sideDish != None:
                    output += f" Name: {sideDish.name} * "
                    output += f"Quantity: {sideItem[1]} -> "
                    output += f"Price: {sideDish.price * sideItem[1]}\n"

        output += f"Total price: {self.__total_price}\n"
        return output

    def __repr__(self) -> str:
        return "\n{ " + str(self) + " }\n"

    def display(self):
        print(str(self))

    def convert_to_list_for_db(self) -> list[int | float | str]:
        lst = []
        lst.append(self.__order_id)
        lst.append(self.__c_name)
        lst.append(self.__c_email)
        lst.append(self.__c_phone_no)
        lst.append(self.__compony)
        lst.append(self.__total_price)
        lst.append(self.__d_date)
        return lst

    def convert_to_dict_for_db(self) -> dict:
        dct = {}
        dct["order_id"] = self.__order_id
        dct["c_name"] = self.__c_name
        dct["c_email"] = self.__c_email
        dct["c_phone_no"] = self.__c_phone_no
        dct["compony"] = self.__compony
        dct["total_price"] = self.__total_price
        dct["d_date"] = self.__d_date
        dct["d_time"] = self.__d_time
        pizzaListData = {}
        for i, item in enumerate(self.__order_pizzas):
            itemJsonName = f"pizza_{i}"
            pizzaListData[itemJsonName] = item[0].convert_to_dict_for_db()
            pizzaListData[itemJsonName]["quantity"] = item[1]
        dct["pizza_list"] = pizzaListData
        sideDishData = {}
        for i, item in enumerate(self.__sideDishes):
            itemJsonName = f"sideDish_{i}"
            sideDishData[itemJsonName] = {"name": item[0], "quantity": item[1]}
        dct["sideDish_list"] = sideDishData
        return dct

    def pizza_convert_to_list(self) -> list[Pizza]:
        pizzaList = []
        for pizza in self.__order_pizzas:
            pizzaList.append(pizza)
        return pizzaList

    def find_order_pizza_index(self, item: Pizza):
        for i, order_pizza_item in enumerate(self.__order_pizzas):
            if order_pizza_item[0] == item:
                return i
        return -1

    def add_remove_pizza_order(self, item: Pizza, quantity: int = 1):
        index: int = self.find_order_pizza_index(item)
        if index == -1:
            self.__order_pizzas.append((item, quantity))
        else:
            new_quantity = self.__order_pizzas[index][1] + quantity
            if new_quantity > 0:
                self.__order_pizzas[index] = (item, new_quantity)
            else:
                self.__order_pizzas.pop(index)
        self.__total_price = self.get_total_price()

    def find_order_side_dish_index(self, item_name: str):
        for i, order_dish in enumerate(self.__sideDishes):
            if order_dish[0].lower() == item_name.lower():
                return i
        return -1

    def add_side_dish_in_order(self, item_name: str, quantity: int = 1):
        index: int = self.find_order_side_dish_index(item_name)
        sideDishItem = self.sideDishesManager.get_sideDish_by_name(item_name)
        if sideDishItem is not None:
            if index == -1:
                itemTotalPrice = sideDishItem.price * quantity
                self.__sideDishes.append((item_name, quantity, itemTotalPrice))
            else:
                new_quantity = self.__sideDishes[index][1] + quantity
                itemTotalPrice = sideDishItem.price * new_quantity
                self.__sideDishes[index] = (item_name, new_quantity, itemTotalPrice)
            self.sideDishesManager.useSideDish(sideDishItem, quantity)
            return True
        else:
            return False

    def remove_side_dish_in_order(self, item_name: str, quantity: int = 1):
        index: int = self.find_order_side_dish_index(item_name)
        if index == -1:
            # Item is not in the list
            pass
        else:
            sideDishItem = self.sideDishesManager.get_sideDish_by_name(item_name)
            if sideDishItem is not None:
                new_quantity = self.__sideDishes[index][1] - quantity
                if new_quantity <= 0:
                    self.sideDishesManager.unUseSideDish(sideDishItem, self.__sideDishes[index][1])
                    self.__sideDishes.pop(index)
                else:
                    itemTotalPrice = sideDishItem.price * new_quantity
                    self.__sideDishes[index] = (item_name, new_quantity, itemTotalPrice)
                    self.sideDishesManager.unUseSideDish(sideDishItem, quantity)
                return True
            else:
                return False

    def get_total_price(self) -> float:
        pizza_total: float = reduce(lambda value, x: value + (x[0].get_price_based_on_size() * x[1]), self.__order_pizzas, 0)
        side_dish_total: float = reduce(lambda value, x: value + x[2], self.__sideDishes, 0)
        total: float = pizza_total + side_dish_total
        return total


def main():
    order = Order(1, "Akshay", "ak@gmail.com", "+233454233", "compony", "12/31/2023", "11:59 PM")
    order.add_remove_pizza_order(Pizza("test", "test D", 30, PizzaSize.SMALL, "test2", PizzaCategory.VEGETARIAN))
    order.add_remove_pizza_order(Pizza("test", "test D", 30, PizzaSize.SMALL, "test2", PizzaCategory.VEGETARIAN))
    order.add_remove_pizza_order(Pizza("test", "test D", 30, PizzaSize.MEDIUM, "test2", PizzaCategory.VEGETARIAN))
    order.add_side_dish_in_order("Caesar Salad", 47)
    order.add_side_dish_in_order("Assistant Pop", 2)
    order.remove_side_dish_in_order("Assistant Pop", 3)
    print("🚀 ~ file: order.py:60 ~ order:", order)
    print("🚀 ~ file: order.py:60 ~ order:", order.sideDishesManager)


if __name__ == "__main__":
    main()
