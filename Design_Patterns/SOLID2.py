# Open-Closed Principle
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size
# ----------- BAD APPROACH ----------------------------------------------
# OCP = Open for extension, closed for modification
# N.B. state space explosion
class ProductFilter:
    def filter_by_color(self, products, color):
        for product in products:
            if product.color == color: yield product
    
    def filter_by_size(self, products, size):
        for product in products:
            if product.size == size: yield product

    def filter_by_size_and_color(self, products, size, color):
        for product in products:
            if product.size == size and product.color == color: yield product
# ---------------------------------------------------------------------------

# Specification
class Specification:
    def is_satisfied(self, item):
        pass
    
    # operator overloading
    def __and__(self, other):
        return AndSpecification(self, other)

class Filter:
    def filter(self, items, specification):
        pass

class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color
    

class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda specification: specification.is_satisfied(item), self.args
        ))

class BetterFilter(Filter):
    def filter(self, items, specification):
        for item in items:
            if specification.is_satisfied(item):
                yield item

if __name__ == '__main__':
    apple = Product('Apple', Color.RED, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.MEDIUM)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]
    pf = ProductFilter()
    print('Green Products (old):')
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f' - {p.name} is Green')

    bf = BetterFilter()
    print('Red Products (new): ')
    red = ColorSpecification(Color.RED)
    for p in bf.filter(products, red):
        print(f' - {p.name} is Red')

    print('Large Products ')
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f' - {p.name} is large')

    print('Large & Blue Products ')
    blue = ColorSpecification(Color.BLUE)
    # large_blue = AndSpecification(large, blue)
    large_blue = large & blue
    for p in bf.filter(products, large_blue):
        print(f' - {p.name} is large and blue')