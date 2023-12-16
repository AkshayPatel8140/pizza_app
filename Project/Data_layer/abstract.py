from abc import ABC, abstractmethod
from enum import Enum


class Display(ABC):
    @abstractmethod
    def display(self):
        pass


class Repository(ABC):
    @abstractmethod
    def create_file(self):
        pass

    @abstractmethod
    def save_items(self, items):
        pass

    @abstractmethod
    def get_items(self):
        pass


class IngredientCategory(Enum):
    TOPING = "toping"
    BASE = "base"


class SideDishesCategory(Enum):
    APPETIZERS = "appetizers"
    DESSERTS = "desserts"
    BEVERAGES = "beverages"


class PizzaCategory(Enum):
    VEGETARIAN = "vegetarian"
    MEAT_LOVERS = "meat lovers"
    SPECIALTY = "specialty"


class PizzaSize(Enum):
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"
    EXTRA_LARGE = "Extra_Large"


def is_number_float(string: str):
    if string.replace(".", "").isdigit():
        return True
    else:
        return False
