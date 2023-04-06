from typing import List

class Bicycle():
    def __init__(self, name:str, price:float, is_sold:bool = False):
        self.name = name
        self.price = price
        self.is_sold = is_sold

stock = [
        Bicycle("Specialized", 200000),
        Bicycle("Santa Cruz ", 100000, True),
        Bicycle("Bianchi", 900000)
    ]

def sum_stock_value(bicycles: List[Bicycle]):
    total = 0
    for bike in bicycles:
        if not bike.is_sold:
            total = total + bike.price
    return total

current_stock_value = sum_stock_value(stock)
print(current_stock_value)
