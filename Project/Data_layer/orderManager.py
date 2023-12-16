from abstract import Display, SideDishesCategory as SiDi
from pizza import Pizza
from pizzaManager import PizzaManager
from recipe import Recipe
from ingredient import Ingredient
from functools import reduce
from sideDish import SideDish
from order import Order
from orderRepository import OrderRepository
from sideDishManager import SideDishManager


class OrderManager(Display):
    def __init__(self) -> None:
        self.__orderList: list[Order] = []
        self.repo = OrderRepository()
        self.repo.create_file()
        self.read_from_db()

    def __str__(self) -> str:
        output = ""
        output += "\nOrders Details\n"
        output += f"Orders : {self.__orderList}"
        return output

    def save_to_db(self) -> None:
        # pass
        self.repo.save_items(self.__orderList)

    def read_from_db(self) -> None:
        data = self.repo.get_items()
        self.__orderList = data

    def add_order(self, newOrder: Order) -> bool:
        for i, oldOrder in enumerate(self.__orderList):
            if oldOrder.order_id == newOrder.order_id:
                self.__orderList[i] = newOrder
                self.save_to_db()
                return True
        self.__orderList.append(newOrder)
        self.save_to_db()
        return False

    def remove_order(self, order_id: int) -> bool:
        for i, order in enumerate(self.__orderList):
            if order.order_id == order_id:
                self.__orderList.pop(i)
                return True
        self.save_to_db()
        return False

    def get_order_by_name(self, name: str) -> list[Order]:
        resultOrders = []
        for order in self.__orderList:
            if order.c_name.lower() == name.lower():
                resultOrders.append(order)
        return resultOrders

    def get_order_by_order_id(self, id: int) -> list[Order]:
        resultOrders = []
        for order in self.__orderList:
            if order.order_id == id:
                resultOrders.append(order)
        return resultOrders

    def display(self):
        print(str(self))


def main():
    print("orderManager")
    orderManager = OrderManager()
    orderManager.display()
    pizzaManager = PizzaManager()
    sideDishManager = SideDishManager()
    print("pizzaManager", pizzaManager.get_pizzaList())
    print("sideDishManager", sideDishManager.list_dish())
    VegetarianPizza = pizzaManager.search_by_name("Vegetarian")
    order_1 = Order(101, "test101", "t101@gmail.comm", "123456789", "C_test101", "12/31/2023", "11:59 PM")
    if VegetarianPizza is not None:
        order_1.add_remove_pizza_order(VegetarianPizza, 1)
    order_1.add_side_dish_in_order("Caesar Salad", 3)
    orderManager.add_order(order_1)
    orderManager.display()


if __name__ == "__main__":
    main()
