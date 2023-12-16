from abc import ABC, abstractmethod
import csv
import os
import copy
from datetime import date, datetime


class Database(ABC):
    @abstractmethod
    def create_file(self) -> None:
        pass

    @abstractmethod
    def save_order(self, orders: list = []) -> None:
        pass

    @abstractmethod
    def read_orders(self) -> None:
        pass

    @abstractmethod
    def save_inventory(self, inventories: list = []) -> None:
        pass

    @abstractmethod
    def read_inventory(self) -> None:
        pass


class Data(Database):
    def __init__(self) -> None:
        self.__order_file_name = "orders.csv"
        self.__inventory_file_name = "inventory.csv"

    def __str__(self) -> str:
        output = ""
        output += f"Order file : {self.__order_file_name}\n"
        output += f"Inventory file : {self.__inventory_file_name}"
        return output

    def create_file(self) -> None:
        path = f"./{self.__order_file_name}"
        check_file = os.path.isfile(path)
        if check_file == False:
            with open(self.__order_file_name, "w", newline="") as file:
                pass
        path = f"./{self.__inventory_file_name}"
        check_file = os.path.isfile(path)
        if check_file == False:
            with open(self.__inventory_file_name, "w", newline="") as file:
                pass


def main():
    print("Library", datetime.now().date(), datetime.now().time())
    print("Library", datetime(2023, 1, 23, 5, 6, 40))
    print("Library", datetime(2023, 12, 23, 5, 6, 40)<datetime.now())
    # l = Data()
    # l.create_file()


if __name__ == "__main__":
    main()
