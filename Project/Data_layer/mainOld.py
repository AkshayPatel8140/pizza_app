import datetime
import mysql.connector
from pizzaManager import PizzaManager
from pizza import Pizza
import tkinter as tk
from tkinter import ttk, messagebox
import time
from tkinter import *
from abc import ABC, abstractmethod
from typing import Optional
from functools import reduce
from functools import partial


class MainWindow(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.__pizzaManager = PizzaManager()
        self.__order_price: float = 0
        self.__pizzaListMenuForOrder: list[tuple[Pizza, Optional[int]]] = []

    def get_total_price_of_order(self, price: float, isAdd: bool = TRUE):
        if isAdd:
            self.__order_price += price
        else:
            self.__order_price -= price

    # def on_entry_change(self, value):
    #     for i, pizzaListItem in enumerate(self.__pizzaListMenuForOrder):
    #         if pizzaListItem[1].get()

    #     print("entry change", value)

    def show_window(self):
        self.wm_title("SFBU Pizza")
        self.geometry(f"{800}x{800}")
        self.grid_columnconfigure([0], weight=1, minsize=100)
        frame = Frame(self)
        frame.pack()

        headerFrame = Frame(self)
        headerFrame.pack(side=TOP)
        title = tk.Label(headerFrame, text="Choose your pizza(s), call, fax or bring this order to SFBU voice or fax 510-555-7777")
        title.pack(side="top")
        subTitle = tk.Label(headerFrame, text="Minimum suggested notice 48 hours")
        subTitle.pack(side="top")

        dateFrame = Frame(self)
        dateFrame.pack(side=TOP)

        delivery_date_label = tk.Label(dateFrame, text="Delivery Date")
        delivery_date_label.pack(side=LEFT)
        delivery_date_input = tk.Entry(dateFrame)
        delivery_date_input.pack(side=LEFT)

        delivery_time_label = tk.Label(dateFrame, text="Delivery time")
        delivery_time_label.pack(side=LEFT)
        delivery_time_input = tk.Entry(dateFrame)
        delivery_time_input.pack(side=LEFT)

        pizzaListTitle = tk.Label(self, text="DeliWorks Feature Combination")
        pizzaListTitle.pack(side=TOP)

        pizzaListFrame = Frame(self)
        pizzaListFrame.pack(side=TOP)

        pizzaList = self.__pizzaManager.get_pizzaList()
        if len(pizzaList) > 0:
            pizzaListMenu: list[tuple[Pizza, Optional[int]]] = list(map(lambda x: (x, 0), pizzaList))
            row_index = 0
            titleQuantity = tk.Label(pizzaListFrame, text="Quantity")
            titleQuantity.grid(row=row_index, column=0)
            titleName = tk.Label(pizzaListFrame, text="Name")
            titleName.grid(row=row_index, column=1)
            titleDescription = tk.Label(pizzaListFrame, text="Description")
            titleDescription.grid(row=row_index, column=2)
            titlePrice = tk.Label(pizzaListFrame, text="Price")
            titlePrice.grid(row=row_index, column=3)
            row_index += 1
            for i, pizzaListItem in enumerate(pizzaListMenu):
                enterQuantity = tk.Entry(pizzaListFrame, width=5)
                enterQuantity.grid(row=row_index, column=0)
                # enterQuantity.bind("<FocusOut>", self.on_entry_change)

                name = tk.Label(pizzaListFrame, text=pizzaListItem[0].name)
                name.grid(row=row_index, column=1)

                description = tk.Label(pizzaListFrame, text=pizzaListItem[0].description, padx=20)
                description.grid(row=row_index, column=2)

                price = tk.Label(pizzaListFrame, text=pizzaListItem[0].get_price_based_on_size())
                price.grid(row=row_index, column=3)

                pizzaListItem = (pizzaListItem[0], enterQuantity)
                row_index += 1
        else:
            Error = tk.Label(self, text="No Pizza Found")
            Error.pack(side=TOP)
            print("Pizza not found")

        CustomPizzaListTitle = tk.Label(self, text="Build your own option")
        CustomPizzaListTitle.pack(side=TOP)

        self.mainloop()


class PizzaStore:
    def __init__(self, store_name: str) -> None:
        self.__store_name = store_name
        self.__pizzaManager = PizzaManager()

    @property
    def pizza_store_name(self):
        return self.__store_name

    def store_name(self):
        print(self.__store_name)

    def pizza_menu(self):
        print("DeliWork Feature Combinations")
        for i, pizzaItem in enumerate(self.__pizzaManager.get_pizzaList()):
            print(f"{i+1}) {pizzaItem.name}({pizzaItem.size.value}) - {pizzaItem.description} - {pizzaItem.get_price_based_on_size()}")
        # pizzaSelectionChoice = input

    def menu(self):
        print(f"Chose your Pizzas, call, fax or bring this order to {self.__store_name} voice or Fax 510-555-7777")
        print("minimum suggested notice 48 hours")
        print("\n=====Menu=====")
        print("1. Chose from the pre combined pizzas")
        print("2. Build your own pizzas")
        print("3. Side dishes")
        print("4. Exit")


def main():
    application = PizzaStore("SFBU")
    while True:
        application.menu()
        mainMenuChoice = input("Select your choice: ")
        if mainMenuChoice.isdigit():
            mainMenuChoice = int(mainMenuChoice)
            if mainMenuChoice <= 0:
                print("Print Select proper choice")
            elif mainMenuChoice == 1:
                application.pizza_menu()
            elif mainMenuChoice == 4:
                break
            else:
                print("Print Select proper choice")
    # mainWindow = MainWindow()
    # mainWindow.show_window()

# def main():
#     try:
#         quantity = int(input("Enter quantity to buy: "))
#         return quantity
#     # except ValueError:
#     #     print("Invalid integer. Please try again.")
#     except Exception as e:
#         print(type(e))
#         print("Invalid integer. Please try again.",e)


if __name__ == "__main__":
    main()
