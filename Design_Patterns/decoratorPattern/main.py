from margherita import Margherita
from basePizza import BasePizza
from extraCheese import ExtraCheese
from chickenBalls import ChickenBalls


def main():

    margPizza: BasePizza = Margherita()
    addExtraCheese: BasePizza = ExtraCheese(margPizza)
    addChickenBallsCheese: BasePizza = ChickenBalls(addExtraCheese)
    print(f"Total Cost: {addChickenBallsCheese.cost()}")


if __name__ == "__main__":
    main()
