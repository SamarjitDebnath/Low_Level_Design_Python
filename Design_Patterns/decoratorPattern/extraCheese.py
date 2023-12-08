from abc import ABC, abstractmethod
from basePizza import BasePizza
from toppings import ToppingsDecorator


class ExtraCheese(ToppingsDecorator):
    def __init__(self, pizza: BasePizza):
        self.base_pizza: BasePizza = pizza

    def cost(self) -> int:
        return (self.base_pizza.cost() + 10)
