import datetime
import mysql.connector
import pizzaManager
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
        self.__pizzaManager = pizzaManager.PizzaManager()

    def show_window(self):
        row_index = 0
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
        pizzaListTitle.pack(side="top")

        pizzaListFrame = Frame(self)
        pizzaListFrame.pack(side=TOP)

        pizzaList = self.__pizzaManager.get_pizzaList()
        for pizzaListItem in pizzaList:
            print(pizzaListItem)

        self.mainloop()


class PizzaStore:
    def __init__(self, store_name: str) -> None:
        self.__store_name = store_name

    @property
    def pizza_store_name(self):
        return self.__store_name

    def store_name(self):
        print(self.__store_name)

    def menu(self):
        print(f"Chose your Pizzas, call, fax or bring this order to {self.__store_name} voice or Fax 510-555-7777")
        print("minimum suggested notice 48 hours")
        print("\n=====Menu=====\n")
        print("1. Chose from the pre combined pizzas")
        print("2. Build your own pizzas")


def main():
    # application = PizzaStore("SFBU")
    # application.menu()
    mainWindow = MainWindow()
    mainWindow.show_window()


if __name__ == "__main__":
    main()
